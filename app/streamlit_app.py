import pandas as pd
import streamlit as st
from datetime import datetime

from athena_client import run_athena_query
from llm_agent import generate_sql
from insight_generator import generate_business_insight
from question_classifier import is_metadata_question
from metadata_assistant import generate_metadata_answer


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

st.sidebar.write(
    "AI-powered analytics platform using AWS Athena + OpenAI"
)

st.sidebar.markdown("---")

st.sidebar.subheader("📌 Example Questions")

st.sidebar.write("• Show top 5 states by revenue")
st.sidebar.write("• Best selling product")
st.sidebar.write("• Which city has highest revenue")
st.sidebar.write("• Show payment status distribution")
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
# ANALYZE
# =====================================================

if st.button("🔍 Analyze", use_container_width=True):

    if question.strip():

        # =====================================================
        # METADATA ASSISTANT ROUTING
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

            st.success("Metadata explanation generated successfully")

            st.subheader("🧠 Metadata Assistant")

            st.info(metadata_answer)

            st.stop()

        # =====================================================
        # GENERATE SQL
        # =====================================================

        with st.spinner("Generating SQL using OpenAI..."):

            sql_query = generate_sql(
                question,
                st.session_state.query_history
            )

        # =====================================================
        # SAVE QUERY HISTORY
        # =====================================================

        st.session_state.query_history.append(
            {
                "question": question,
                "sql": sql_query,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        )

        # =====================================================
        # RUN ATHENA QUERY
        # =====================================================

        with st.spinner("Running Athena query..."):

            df = cached_athena_query(sql_query)

        # =====================================================
        # GENERATE AI INSIGHT
        # =====================================================

        with st.spinner("Generating AI business insights..."):

            ai_insight = generate_business_insight(
                question,
                df
            )

        st.success("Analysis completed successfully")

        # =====================================================
        # FORMAT DATAFRAME
        # =====================================================

        formatted_df = df.copy()

        for column in formatted_df.columns:

            converted = pd.to_numeric(
                formatted_df[column],
                errors="coerce"
            )

            if converted.notna().sum() > 0:

                formatted_df[column] = converted.apply(
                    lambda x: f"{x:,.0f}"
                    if pd.notnull(x)
                    else x
                )

        # =====================================================
        # KPI CARDS
        # =====================================================

        kpi1, kpi2, kpi3 = st.columns(3)

        with kpi1:
            st.metric("Records Returned", len(df))

        with kpi2:
            st.metric("Columns Returned", len(df.columns))

        with kpi3:
            st.metric("Query Engine", "Athena")

        # =====================================================
        # TABS
        # =====================================================

        tab1, tab2, tab3 = st.tabs(
            [
                "📊 Results",
                "📈 Visualization",
                "🧠 Generated SQL"
            ]
        )

        # =====================================================
        # RESULTS TAB
        # =====================================================

        with tab1:

            st.subheader("Query Results")

            st.dataframe(
                formatted_df,
                use_container_width=True
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

            st.subheader("Visualization")

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

            if len(dimension_cols) > 0 and len(numeric_cols) > 0:

                dimension_col = dimension_cols[0]

                metric_col = numeric_cols[0]

                st.bar_chart(
                    chart_df.set_index(dimension_col)[metric_col]
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

            st.subheader("Generated Athena SQL")

            st.code(
                sql_query,
                language="sql"
            )

    else:

        st.warning("Please enter a question.")