# 🚀 Enterprise Retail AI Analytics Copilot

AI-powered enterprise analytics platform built using **AWS Athena, AWS Glue, Amazon S3, OpenAI, Streamlit, Plotly, and RAG-based metadata search**.

This project enables business users to ask natural language questions and receive:

- AI-generated Athena SQL
- Interactive Plotly visualizations
- AI business insights
- SQL explanations
- RAG-based metadata responses
- Query history
- Downloadable analytics results

---

## 🌐 Live Demo

https://enterprise-retail-ai-analytics-copilot-amecggjsprkhai987fhfej.streamlit.app/

---

## ✨ Features

### ✅ Natural Language to SQL

Converts business questions into Athena SQL using OpenAI.

```text
Show top 5 states by revenue
```

---

### ✅ RAG-Based Metadata Assistant

Answers metadata and glossary questions without running Athena.

```text
What is dim_customer_scd2?

What does reorder_level mean?

Explain fact_orders table
```

---

### ✅ Intelligent Query Routing

Routes questions into:

```text
Metadata Question → RAG Metadata Assistant

Analytics Question → OpenAI SQL → Athena → Charts + Insights
```

---

### ✅ AI Business Insights

Generates executive-style business summaries after Athena query execution.

---

### ✅ SQL Explanation Layer

Explains generated SQL in simple business language.

---

### ✅ Interactive Plotly Visualizations

Supports:

- Bar charts
- Line charts
- Pie charts
- Zoom in / zoom out
- Hover analytics
- Export image

---

### ✅ Query History and CSV Export

Tracks recent questions and allows users to download query results.

---

## 🧠 AI Workflow

```text
User Question
      ↓
Question Classifier
      ↓
Metadata Route OR Analytics Route
      ↓
RAG Metadata Search OR OpenAI NL2SQL
      ↓
Athena Query Execution
      ↓
Results + Plotly Charts + AI Insights
```

---

## 🏗️ Enterprise Architecture

<p align="center">
  <img src="architecture/architecture_diagram.png" width="1000"/>
</p>

---

## 🛠️ My Implementation

<p align="center">
  <img src="architecture/implementation_proof.png" width="1000"/>
</p>

---

## 📸 Application Screenshots

### Dashboard

<p align="center">
  <img src="screenshots/dashboard.png" width="1000"/>
</p>

---

### AI Visualization

<p align="center">
  <img src="screenshots/chart.png" width="1000"/>
</p>

---

### SQL Explanation

<p align="center">
  <img src="screenshots/sql_explanation.png" width="1000"/>
</p>

---

### AI Business Insights

<p align="center">
  <img src="screenshots/ai_business_insights.png" width="1000"/>
</p>

---

### RAG Metadata Assistant

<p align="center">
  <img src="screenshots/metadata_assistant.png" width="1000"/>
</p>

---

### Query History

<p align="center">
  <img src="screenshots/query_history.png" width="350"/>
</p>

---

## ☁️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon S3 | Raw and curated data lake storage |
| AWS Glue | PySpark ETL processing |
| AWS Lambda | Event-driven orchestration |
| Amazon Athena | Serverless SQL analytics |
| AWS Glue Data Catalog | Metadata catalog |
| CloudWatch | Monitoring and logging |
| SNS | Alerts and notifications |
| IAM | Access management |

---

## 🤖 AI and Analytics Stack

| Component | Tool |
|---|---|
| NL2SQL | OpenAI |
| Metadata RAG | OpenAI Embeddings + FAISS |
| Dashboard | Streamlit |
| Charts | Plotly |
| Query Engine | Amazon Athena |
| Data Processing | AWS Glue PySpark |
| Storage | Amazon S3 |

---

## 🔄 Data Engineering Pipeline

```text
Retail CSV Files
      ↓
Amazon S3 Raw Layer
      ↓
AWS Lambda Trigger
      ↓
AWS Glue PySpark ETL
      ↓
Validation + Reject Handling
      ↓
SCD Type 1 and Type 2 Processing
      ↓
Fact and Dimension Loading
      ↓
Audit and Reconciliation
      ↓
Curated S3 Parquet Warehouse
      ↓
Amazon Athena
      ↓
AI Analytics Copilot
```

---

## 🧱 Data Warehouse Design

### Fact Tables

#### fact_orders

```text
Grain = 1 row per order
```

Used for:

- Revenue analytics
- Product sales analysis
- Customer analytics
- Regional reporting
- Payment analytics

#### fact_inventory

```text
Grain = 1 row per product per warehouse
```

Used for:

- Inventory monitoring
- Low stock detection
- Reorder-level analysis

---

### Dimension Tables

#### dim_customer_scd2

Tracks historical customer changes using SCD Type 2 logic.

#### dim_product_scd1

Stores latest product attributes using SCD Type 1 overwrite logic.

---

## 🏢 Enterprise ETL Features

- Data validation framework
- Reject handling framework
- Audit logging
- Reconciliation checks
- SCD Type 1 processing
- SCD Type 2 processing
- Curated Parquet output
- Crawler-based Glue Catalog integration

---

## 🧪 Example Questions

### Analytics Questions

```text
Show top 5 states by revenue

Show monthly revenue trend

Show payment status distribution

Top 3 products by sales

Which city has highest revenue?
```

### Metadata Questions

```text
What is dim_customer_scd2?

What does reorder_level mean?

Explain fact_orders table

How is revenue calculated?
```

---

## ▶️ Run Locally

```bash
git clone https://github.com/Suryatejapolepalli/enterprise-retail-ai-analytics-copilot.git

cd enterprise-retail-ai-analytics-copilot

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

streamlit run app/streamlit_app.py
```

---

## 🔐 Security

- OpenAI API keys are stored as environment variables
- AWS credentials are managed using AWS CLI or Streamlit secrets
- No secrets are hardcoded in source code
- `.gitignore` prevents local environment files from being pushed

Example:

```bash
setx OPENAI_API_KEY "your_api_key_here"
```

---

## 📂 Project Structure

```text
enterprise-retail-ai-analytics-copilot/
│
├── app/
│   ├── streamlit_app.py
│   ├── athena_client.py
│   ├── llm_agent.py
│   ├── prompts.py
│   ├── insight_generator.py
│   ├── sql_explainer.py
│   ├── metadata_assistant.py
│   ├── metadata_documents.py
│   ├── rag_metadata.py
│   └── question_classifier.py
│
├── architecture/
│   ├── architecture_diagram.png
│   └── implementation_proof.png
│
├── screenshots/
│   ├── dashboard.png
│   ├── chart.png
│   ├── sql_explanation.png
│   ├── ai_business_insights.png
│   ├── metadata_assistant.png
│   └── query_history.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Technical Skills Demonstrated

### AWS and Data Engineering

- Amazon S3
- AWS Glue PySpark
- AWS Lambda
- Amazon Athena
- AWS Glue Data Catalog
- CloudWatch and SNS
- Data warehousing
- SCD Type 1 and Type 2
- Audit and reconciliation frameworks

### AI and Analytics

- OpenAI API
- NL2SQL
- Prompt engineering
- RAG metadata search
- FAISS vector search
- AI business insights
- SQL explanation
- Conversational analytics
- Intelligent routing

### Dashboarding

- Streamlit
- Plotly
- KPI cards
- Query history
- CSV export
- Interactive charts

---

## 📈 Project Impact

This project demonstrates how **enterprise data engineering and generative AI** can be combined to build an intelligent analytics copilot.

It reduces dependency on manual SQL writing and allows business users to explore data through natural language, while still maintaining enterprise data warehouse practices such as validation, audit logging, reconciliation, and dimensional modeling.

---

## 💼 Resume Highlights

- Built and deployed an AI-powered enterprise analytics copilot using AWS Athena, OpenAI, Streamlit, Plotly, and AWS serverless services.
- Implemented NL2SQL, RAG-based metadata search, AI business insights, SQL explanations, query history, and interactive visualizations.
- Designed an AWS data warehouse pipeline using S3, Glue PySpark, Lambda, Athena, CloudWatch, and SNS.
- Implemented SCD Type 1 and SCD Type 2 dimensional modeling with audit, reconciliation, and reject handling frameworks.

---

## ⚠️ Limitations

- Query history is currently session-based
- Metadata RAG is lightweight and file-based
- Complex SQL edge cases may require stronger validation
- Authentication and role-based access control are not yet implemented

---

## 🚀 Future Enhancements

- LangGraph agent workflow
- Persistent query history using DynamoDB or PostgreSQL
- Role-based access control
- Advanced semantic layer
- SQL auto-correction and retry
- AWS Bedrock integration
- Docker deployment
- Terraform infrastructure
- CI/CD with GitHub Actions

---

## 👨‍💻 Author

### Surya Teja Polepalli

GitHub:  
https://github.com/Suryatejapolepalli

Project Repository:  
https://github.com/Suryatejapolepalli/enterprise-retail-ai-analytics-copilot

---

## ⭐ Project Highlights

✅ Deployed GenAI analytics application  
✅ AWS serverless data engineering  
✅ OpenAI-powered NL2SQL  
✅ RAG-based metadata assistant  
✅ Athena query execution  
✅ Plotly interactive dashboards  
✅ AI-generated business insights  
✅ Enterprise data warehouse design  
✅ Resume and interview-ready project