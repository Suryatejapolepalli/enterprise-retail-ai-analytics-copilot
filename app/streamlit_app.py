import pandas as pd
import streamlit as st

from athena_client import run_athena_query
from llm_agent import generate_sql


st.set_page_config(
    page_title="Enterprise Retail AI Analytics Copilot",
    layout="wide"
)

st.title("Enterprise Retail AI Analytics Copilot")

st.write(
    "Ask natural language business questions on top of the AWS retail data warehouse."
)

question = st.text_input(
    "Ask a business question",
    placeholder="Example: Show top 5 states by revenue"
)

if st.button("Analyze"):

    if question.strip():

        # =====================================================
        # GENERATE SQL USING LLM
        # =====================================================

        with st.spinner("Generating SQL using LLM..."):

            sql_query = generate_sql(question)

        st.subheader("Generated Athena SQL")

        st.code(sql_query, language="sql")

        # =====================================================
        # EXECUTE ATHENA QUERY
        # =====================================================

        with st.spinner("Running Athena query..."):

            df = run_athena_query(sql_query)

        st.success("Analysis completed successfully")

        # =====================================================
        # FORMAT NUMERIC COLUMNS
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
        # DISPLAY RESULTS
        # =====================================================

        st.subheader("Query Results")

        st.dataframe(
            formatted_df,
            use_container_width=True
        )

        # =====================================================
        # BUSINESS INSIGHT
        # =====================================================

        if not df.empty:

            st.subheader("Business Insight")

            st.write(
                f"The query returned {len(df)} records successfully from the retail warehouse."
            )

            # =====================================================
            # VISUALIZATION
            # =====================================================

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

                st.subheader("Visualization")

                st.bar_chart(
                    chart_df.set_index(dimension_col)[metric_col]
                )

            else:

                st.info(
                    "Visualization is available when the result contains a numeric metric column."
                )

    else:

        st.warning("Please enter a question.")