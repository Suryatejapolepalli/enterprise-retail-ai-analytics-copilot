import pandas as pd
import streamlit as st
import plotly.express as px

from datetime import datetime

from sql_explainer import explain_sql
from athena_client import run_athena_query
from llm_agent import generate_sql
from insight_generator import generate_business_insight
from question_classifier import is_metadata_question
from metadata_assistant import generate_metadata_answer
from query_logger import save_query, get_query_history


st.set_page_config(
    page_title="Enterprise Retail AI Analytics Copilot",
    page_icon="📊",
    layout="wide"
)


# =====================================================
# SESSION STATE
# =====================================================

if "query_history" not in st.session_state:
    st.session_state.query_history = []

if "admin_authenticated" not in st.session_state:
    st.session_state.admin_authenticated = False


# =====================================================
# CACHE
# =====================================================

@st.cache_data(ttl=300)
def cached_athena_query(sql_query):
    return run_athena_query(sql_query)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>
    .main-title {
        font-size: 38px;
        font-weight: 800;
        color: #1f77b4;
    }

    .subtitle {
        font-size: 18px;
        color: #666666;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🚀 Retail AI Copilot")
st.sidebar.write("AI-powered analytics platform using AWS Athena + OpenAI")

st.sidebar.markdown("---")
st.sidebar.subheader("📌 Example Questions")
st.sidebar.write("• Show top 5 states by revenue")
st.sidebar.write("• Best selling product")
st.sidebar.write("• Which city has highest revenue")
st.sidebar.write("• Show payment status distribution")
st.sidebar.write("• Show monthly revenue trend")
st.sidebar.write("• What does reorder_level mean?")

st.sidebar.markdown("---")
st.sidebar.subheader("🕘 Query History")

if st.session_state.query_history:
    for item in reversed(st.session_state.query_history[-5:]):
        st.sidebar.markdown(
            f"""
            **Question:**  
            {item['question']}

            **Time:**  
            {item['time']}
            """
        )
        st.sidebar.markdown("---")
else:
    st.sidebar.info("No queries executed yet.")


# =====================================================
# SIDEBAR ADMIN LOGIN
# =====================================================

st.sidebar.markdown("---")
st.sidebar.subheader("🔐 Admin Login")

if not st.session_state.admin_authenticated:

    admin_password = st.sidebar.text_input(
        "Admin Password",
        type="password",
        key="sidebar_admin_password"
    )

    if st.sidebar.button("Login"):
        if admin_password == st.secrets["ADMIN_PASSWORD"]:
            st.session_state.admin_authenticated = True
            st.sidebar.success("Admin logged in")
            st.rerun()
        else:
            st.sidebar.error("Invalid password")

else:
    st.sidebar.success("Admin access enabled")

    if st.sidebar.button("Logout"):
        st.session_state.admin_authenticated = False
        st.rerun()


# =====================================================
# TITLE
# =====================================================

st.markdown(
    '<div class="main-title">Enterprise Retail AI Analytics Copilot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask business questions in natural language and get AI-generated Athena analytics.</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# =====================================================
# INPUT
# =====================================================

question = st.text_input(
    "Ask a business question",
    placeholder="Example: Show top 5 states by revenue"
)


# =====================================================
# ANALYZE BUTTON
# =====================================================

if st.button("🔍 Analyze", width="stretch"):

    if question.strip():

        # =====================================================
        # METADATA QUESTIONS
        # =====================================================

        if is_metadata_question(question):

            with st.spinner("Generating metadata explanation..."):
                metadata_answer = generate_metadata_answer(question)

            st.session_state.query_history.append(
                {
                    "question": question,
                    "sql": "Metadata assistant response - Athena query not executed",
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            )

            save_query(
                question,
                "Metadata assistant response - Athena query not executed",
                metadata_answer,
                query_type="metadata"
            )

            st.success("Metadata explanation generated successfully")
            st.subheader("🧠 Metadata Assistant")
            st.info(metadata_answer)

        # =====================================================
        # ANALYTICS QUESTIONS
        # =====================================================

        else:

            with st.spinner("Generating SQL using OpenAI..."):
                sql_query = generate_sql(
                    question,
                    st.session_state.query_history
                )

            st.session_state.query_history.append(
                {
                    "question": question,
                    "sql": sql_query,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            )

            with st.spinner("Running Athena query..."):
                df = cached_athena_query(sql_query)

            with st.spinner("Generating SQL explanation..."):
                sql_explanation = explain_sql(sql_query)

            with st.spinner("Generating AI business insights..."):
                ai_insight = generate_business_insight(
                    question,
                    df
                )

            save_query(
                question,
                sql_query,
                ai_insight,
                query_type="analytics"
            )

            st.success("Analysis completed successfully")

            formatted_df = df.copy()

            for column in formatted_df.columns:
                converted = pd.to_numeric(
                    formatted_df[column],
                    errors="coerce"
                )

                if converted.notna().sum() > 0:
                    formatted_df[column] = converted.apply(
                        lambda x: f"{x:,.0f}" if pd.notnull(x) else x
                    )

            kpi1, kpi2, kpi3 = st.columns(3)

            with kpi1:
                st.metric("Records Returned", len(df))

            with kpi2:
                st.metric("Columns Returned", len(df.columns))

            with kpi3:
                st.metric("Query Engine", "Athena")

            tab1, tab2, tab3, tab4 = st.tabs(
                [
                    "📊 Results",
                    "📈 Visualization",
                    "🧠 Generated SQL",
                    "📊 Usage Analytics"
                ]
            )

            # =====================================================
            # RESULTS TAB
            # =====================================================

            with tab1:

                st.subheader("Query Results")

                st.dataframe(
                    formatted_df,
                    width="stretch"
                )

                csv = df.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="📥 Download Results CSV",
                    data=csv,
                    file_name="athena_query_results.csv",
                    mime="text/csv",
                    key=f"download_{len(st.session_state.query_history)}"
                )

                st.subheader("🧠 AI Business Insight")
                st.info(ai_insight)

                st.subheader("Business Insight")
                st.write(
                    f"""
                    The query returned **{len(df)} records**
                    from the curated AWS retail warehouse.
                    """
                )

            # =====================================================
            # VISUALIZATION TAB
            # =====================================================

            with tab2:

                st.subheader("📈 AI Visualization")

                chart_df = df.copy()
                numeric_cols = []

                for column in chart_df.columns:
                    converted = pd.to_numeric(
                        chart_df[column],
                        errors="coerce"
                    )

                    if converted.notna().sum() > 0:
                        chart_df[column] = converted
                        numeric_cols.append(column)

                dimension_cols = [
                    c for c in chart_df.columns
                    if c not in numeric_cols
                ]

                if len(dimension_cols) == 0:
                    if "month" in chart_df.columns:
                        dimension_cols = ["month"]
                    elif "year" in chart_df.columns:
                        dimension_cols = ["year"]

                if len(dimension_cols) > 0 and len(numeric_cols) > 0:

                    dimension_col = dimension_cols[0]

                    preferred_metrics = [
                        c for c in numeric_cols
                        if (
                            "revenue" in c.lower()
                            or "sales" in c.lower()
                            or "amount" in c.lower()
                            or "count" in c.lower()
                            or "total" in c.lower()
                        )
                    ]

                    if len(preferred_metrics) > 0:
                        metric_col = preferred_metrics[0]
                    else:
                        metric_candidates = [
                            c for c in numeric_cols
                            if c not in dimension_cols
                        ]

                        if len(metric_candidates) == 0:
                            metric_col = numeric_cols[0]
                        else:
                            metric_col = metric_candidates[0]

                    lower_question = question.lower()

                    if (
                        "distribution" in lower_question
                        or "percentage" in lower_question
                        or "share" in lower_question
                    ):

                        st.subheader("🥧 Distribution Chart")

                        pie_df = (
                            chart_df[[dimension_col, metric_col]]
                            .dropna()
                        )

                        fig = px.pie(
                            pie_df,
                            names=dimension_col,
                            values=metric_col,
                            title="Distribution Analysis"
                        )

                        st.plotly_chart(
                            fig,
                            width="stretch"
                        )

                    elif (
                        "trend" in lower_question
                        or "over time" in lower_question
                        or "monthly" in lower_question
                        or "daily" in lower_question
                    ):

                        st.subheader("📈 Trend Chart")

                        fig = px.line(
                            chart_df,
                            x=dimension_col,
                            y=metric_col,
                            title="Trend Analysis"
                        )

                        st.plotly_chart(
                            fig,
                            width="stretch"
                        )

                    else:

                        st.subheader("📊 Ranking Chart")

                        fig = px.bar(
                            chart_df,
                            x=dimension_col,
                            y=metric_col,
                            title="Ranking Analysis"
                        )

                        st.plotly_chart(
                            fig,
                            width="stretch"
                        )

                else:
                    st.info(
                        """
                        Visualization available only when
                        result contains numeric metric columns.
                        """
                    )

            # =====================================================
            # SQL TAB
            # =====================================================

            with tab3:

                st.subheader("🧠 SQL Explanation")
                st.info(sql_explanation)

                st.subheader("Generated Athena SQL")
                st.code(sql_query, language="sql")

            # =====================================================
            # USAGE ANALYTICS TAB
            # =====================================================

            with tab4:

                st.subheader("📊 Copilot Usage Analytics")

                if not st.session_state.admin_authenticated:
                    st.warning("Admin access required to view usage analytics.")
                    st.stop()

                history_df = get_query_history()

                if history_df.empty:

                    st.info("No usage history available yet.")

                else:

                    st.subheader("🔎 Usage Filters")

                    filter_col1, filter_col2, filter_col3 = st.columns(3)

                    with filter_col1:
                        query_type_filter = st.selectbox(
                            "Query Type",
                            [
                                "All",
                                "analytics",
                                "metadata"
                            ]
                        )

                    with filter_col2:
                        search_text = st.text_input(
                            "Search Question",
                            placeholder="Search questions..."
                        )

                    with filter_col3:
                        max_rows = st.slider(
                            "Recent Activity Rows",
                            min_value=5,
                            max_value=50,
                            value=10
                        )

                    filtered_df = history_df.copy()

                    if (
                        query_type_filter != "All"
                        and "query_type" in filtered_df.columns
                    ):
                        filtered_df = filtered_df[
                            filtered_df["query_type"] == query_type_filter
                        ]

                    if search_text.strip() and "question" in filtered_df.columns:
                        filtered_df = filtered_df[
                            filtered_df["question"].str.contains(
                                search_text,
                                case=False,
                                na=False
                            )
                        ]

                    total_queries = len(filtered_df)

                    metadata_count = (
                        len(filtered_df[filtered_df["query_type"] == "metadata"])
                        if "query_type" in filtered_df.columns
                        else 0
                    )

                    analytics_count = (
                        len(filtered_df[filtered_df["query_type"] == "analytics"])
                        if "query_type" in filtered_df.columns
                        else 0
                    )

                    metric_col1, metric_col2, metric_col3 = st.columns(3)

                    with metric_col1:
                        st.metric("Total Queries", total_queries)

                    with metric_col2:
                        st.metric("Analytics Queries", analytics_count)

                    with metric_col3:
                        st.metric("Metadata Queries", metadata_count)

                    if "date" in filtered_df.columns and not filtered_df.empty:

                        trend_df = (
                            filtered_df
                            .groupby("date")
                            .size()
                            .reset_index(name="query_count")
                        )

                        fig = px.line(
                            trend_df,
                            x="date",
                            y="query_count",
                            title="Query Trend Over Time"
                        )

                        st.plotly_chart(
                            fig,
                            width="stretch"
                        )

                    st.subheader("Top Questions")

                    if not filtered_df.empty and "question" in filtered_df.columns:

                        top_questions = (
                            filtered_df["question"]
                            .value_counts()
                            .head(5)
                            .reset_index()
                        )

                        top_questions.columns = [
                            "question",
                            "count"
                        ]

                        fig = px.bar(
                            top_questions,
                            x="question",
                            y="count",
                            title="Top 5 Asked Questions"
                        )

                        st.plotly_chart(
                            fig,
                            width="stretch"
                        )

                    else:
                        st.info("No questions available for selected filters.")

                    st.subheader("Recent Activity")

                    display_cols = [
                        col for col in [
                            "question",
                            "query_type",
                            "timestamp"
                        ]
                        if col in filtered_df.columns
                    ]

                    if display_cols and not filtered_df.empty:

                        display_df = filtered_df[display_cols]

                        st.dataframe(
                            display_df.sort_values(
                                "timestamp",
                                ascending=False
                            ).head(max_rows),
                            width="stretch"
                        )

                    else:
                        st.info("No recent activity available for selected filters.")

    else:

        st.warning("Please enter a question.")