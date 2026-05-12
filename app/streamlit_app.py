import pandas as pd
import streamlit as st

from athena_client import run_athena_query
from llm_agent import generate_sql


st.set_page_config(
    page_title="Enterprise Retail AI Analytics Copilot",
    page_icon="📊",
    layout="wide"
)

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

st.sidebar.title("🚀 Retail AI Copilot")
st.sidebar.write("AI-powered analytics on AWS retail warehouse")

st.sidebar.markdown("---")
st.sidebar.markdown("### Capabilities")
st.sidebar.write("✅ Natural Language to SQL")
st.sidebar.write("✅ Athena Query Execution")
st.sidebar.write("✅ Business Insights")
st.sidebar.write("✅ Auto Visualization")

st.sidebar.markdown("---")
st.sidebar.markdown("### Example Questions")
st.sidebar.write("• Show top 5 states by revenue")
st.sidebar.write("• Which city has highest revenue")
st.sidebar.write("• Best selling product")
st.sidebar.write("• Show payment status distribution")

st.markdown(
    '<div class="main-title">Enterprise Retail AI Analytics Copilot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask natural language business questions and get Athena SQL, results, insights, and charts.</div>',
    unsafe_allow_html=True
)

st.markdown("---")

question = st.text_input(
    "Ask a business question",
    placeholder="Example: Show top 5 states by revenue"
)

if st.button("🔍 Analyze", use_container_width=True):

    if question.strip():

        with st.spinner("Generating SQL using LLM..."):
            sql_query = generate_sql(question)

        with st.spinner("Running Athena query..."):
            df = run_athena_query(sql_query)

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

        tab1, tab2, tab3 = st.tabs(
            ["📊 Results", "📈 Visualization", "🧠 Generated SQL"]
        )

        with tab1:
            st.subheader("Query Results")
            st.dataframe(
                formatted_df,
                use_container_width=True
            )

            st.subheader("Business Insight")
            st.write(
                f"The query returned **{len(df)} records** from the curated AWS retail warehouse."
            )

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
                    "Visualization is available when the result contains a numeric metric column."
                )

        with tab3:
            st.subheader("Generated Athena SQL")
            st.code(sql_query, language="sql")

    else:
        st.warning("Please enter a question.")