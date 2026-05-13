# 🚀 Enterprise Retail AI Analytics Copilot  
### *AI-Powered Serverless Retail Analytics Platform on AWS*

![AWS](https://img.shields.io/badge/AWS-Serverless-orange?logo=amazonaws)
![Python](https://img.shields.io/badge/Python-Analytics-blue?logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-NL2SQL-green?logo=openai)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![Athena](https://img.shields.io/badge/Amazon-Athena-purple?logo=amazonaws)
![Glue](https://img.shields.io/badge/AWS-Glue-yellow?logo=amazonaws)

---

# 📌 Project Overview

Enterprise Retail AI Analytics Copilot is a **production-style AI-powered analytics platform** built on AWS that enables users to ask **business questions in natural language** and instantly receive:

✅ Athena SQL Queries  
✅ Analytics Results  
✅ Visualizations & Charts  
✅ Business Insights  

This project combines:

- ☁️ AWS Serverless Data Engineering
- 🧠 OpenAI NL2SQL Intelligence
- 📊 Enterprise Data Warehousing
- ⚡ Real-time Analytics Architecture
- 📈 Interactive Streamlit Dashboards

---

# 🎯 Business Problem Solved

Retail organizations generate massive volumes of:

- Orders
- Inventory
- Customer
- Product
- Payment

data daily.

Business users often struggle to:

❌ Write SQL queries  
❌ Access analytics quickly  
❌ Generate insights without technical teams  

This platform solves that problem using **AI-powered Natural Language to SQL (NL2SQL)** generation.

---

# 🧠 AI Copilot Capabilities

Users can ask questions like:

```text
Show top 5 states by revenue

Which city has highest revenue

Best selling products

Show payment status distribution

Top 3 products by sales
```

The system automatically:

```text
Natural Language
        ↓
OpenAI GPT
        ↓
Athena SQL
        ↓
Query Execution
        ↓
Results + Charts + Insights
```

---

# 🏗️ End-to-End Architecture

## 📌 Architecture Diagram

![Architecture Diagram](architecture/architecture_diagram.png)

---


## 📌 Implementation Proof (What I Built)

![Implementation Proof](architecture/implementation_proof.png)

---

# ☁️ AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon S3 | Raw & Curated Data Lake |
| AWS Glue | Enterprise ETL Framework |
| AWS Lambda | Event Trigger Automation |
| Amazon Athena | SQL Analytics Engine |
| Amazon SNS | Failure Notifications |
| Amazon CloudWatch | Monitoring & Logs |
| AWS IAM | Security & Access |
| Streamlit | Interactive Dashboard |
| OpenAI API | NL2SQL AI Engine |

---

# 🧱 Enterprise Data Warehouse Design

## ⭐ Fact Tables

### 📦 fact_orders

```text
Grain = 1 row per order
```

### 🏭 fact_inventory

```text
Grain = 1 row per product per warehouse
```

---

## ⭐ Dimension Tables

### 👤 dim_customer_scd2

Implemented using:

- SCD Type 2
- Historical Tracking
- Effective Dates
- Current Flag Logic

### 🛍️ dim_product_scd1

Implemented using:

- SCD Type 1 Overwrite Logic

---

# 🔄 Enterprise ETL Pipeline Flow

```text
Retail CSV Files
        ↓
Amazon S3 Raw Layer
        ↓
AWS Lambda Trigger
        ↓
AWS Glue PySpark ETL
        ↓
Validation & Reject Handling
        ↓
SCD Type 1 & Type 2 Processing
        ↓
Fact & Dimension Loading
        ↓
Audit & Reconciliation
        ↓
Curated S3 Warehouse
        ↓
Amazon Athena
        ↓
AI Analytics Copilot
```

---

# 🔥 Key Enterprise Features

## ✅ Data Validation Framework

Implemented:

- Null validations
- Duplicate handling
- Data type validation
- Business rule validation
- Invalid record filtering

---

## ✅ Reject Handling Framework

Invalid records redirected into dedicated reject zones with:

- Reject reason
- Timestamp
- Source tracking

---

## ✅ Audit Logging Framework

Audit framework captures:

- Job names
- Record counts
- Load timestamps
- Job status
- Target locations

---

## ✅ Reconciliation Framework

Implemented enterprise reconciliation between:

- Source counts
- Valid counts
- Reject counts
- Curated target counts

---

# ⚡ Event-Driven Serverless Architecture

Implemented automation using:

```text
S3 Upload
    ↓
Lambda Trigger
    ↓
Glue ETL Execution
```

This enables fully automated ETL execution whenever new files arrive.

---

# 📊 AI-Powered Analytics Features

## 🧠 Intelligent SQL Generation

The AI engine automatically:

✅ Generates Athena-compatible SQL  
✅ Applies dynamic LIMIT handling  
✅ Selects only requested columns  
✅ Handles ranking queries  
✅ Supports aggregation logic  
✅ Understands business analytics questions  

---

## 📈 Dynamic Visualization Layer

Automatically generates:

- Bar Charts
- KPI Insights
- Revenue Analytics
- Ranking Visualizations
- Business Summaries

---

# 📸 Application Screenshots

## 🖥️ Streamlit Dashboard

![Dashboard](screenshots/dashboard.png)

---
## 🧠 AI Business Insights

![AI Business Insights](screenshots/ai_business_insights.png)

---

## 🕘 AI Query History

![Query History](screenshots/query_history.png)

---

## 🧠 Generated Athena SQL

![Generated SQL](screenshots/generated_sql.png)

---

## 📊 Query Results

![Query Results](screenshots/query_results.png)

---

## 📈 Visualization Layer

![Visualization](screenshots/chart.png)

---

## Demo Questions

- Show top 5 states by revenue
- Best selling product
- Which city has highest revenue
- Show payment status distribution
- Top 3 products by sales

---

## ✨ Live Features

- ✅ AI-powered NL2SQL generation
- ✅ Amazon Athena query execution
- ✅ Interactive visualizations
- ✅ KPI cards
- ✅ Query history tracking
- ✅ CSV download support
- ✅ Enterprise warehouse architecture
- ✅ SCD Type 1 & Type 2 implementation

---

## 🧠 AI Business Insights

The application automatically generates executive-level business insights using OpenAI after query execution.

Features:

- AI-generated executive summaries
- Trend identification
- Business observations
- Insight generation from Athena query results

Example:

```text
California generated the highest revenue among all states.
Electronics products dominate sales performance.
Revenue concentration indicates strong regional demand.
```
---


# 🧪 Sample Athena Queries

## Revenue by State

```sql
SELECT
    state,
    SUM(total_amount) AS revenue
FROM fact_orders
GROUP BY state
ORDER BY revenue DESC
LIMIT 5;
```

---

## Best Selling Product

```sql
SELECT product_name
FROM fact_orders
GROUP BY product_name
ORDER BY SUM(quantity) DESC
LIMIT 1;
```

---

## Low Inventory Detection

```sql
SELECT
    product_name,
    warehouse_id,
    stock_quantity
FROM fact_inventory
WHERE stock_quantity < reorder_level;
```

---

# 📂 Project Structure

```text
enterprise-retail-ai-analytics-copilot/
│
├── app/
│   ├── streamlit_app.py
│   ├── athena_client.py
│   ├── llm_agent.py
│   └── prompts.py
│
├── architecture/
├── screenshots/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Security

OpenAI API keys and AWS credentials are not hardcoded in the application.  
Credentials are managed securely through environment variables and local AWS CLI configuration.

---

# 🛠️ Technical Skills Demonstrated

## ☁️ AWS & Cloud

- Amazon S3
- AWS Glue
- AWS Lambda
- Amazon Athena
- CloudWatch
- SNS
- IAM

---

## 🧠 AI & Analytics

- OpenAI API
- NL2SQL
- Prompt Engineering
- Business Analytics
- Streamlit Dashboards

---

## 📊 Data Engineering

- PySpark
- Enterprise ETL
- SCD Type 1 & 2
- Data Warehousing
- Audit Frameworks
- Reconciliation Frameworks
- Data Validation

---

# 🚀 Future Enhancements

Planned enterprise upgrades:

- LangChain Agents
- RAG Architecture
- Query History
- Conversational Memory
- KPI Cards
- CSV/PDF Export
- Terraform IaC
- CI/CD Pipelines
- Bedrock Integration
- Role-Based Access Control

---

# 🔐 Security

- OpenAI API keys are managed using environment variables
- AWS credentials are configured using AWS CLI profiles
- No secrets or credentials are hardcoded in the repository

---

# 👨‍💻 Author

## Surya Teja Polepalli

### 🔗 GitHub

https://github.com/Suryatejapolepalli

### 🔗 Project Repository

https://github.com/Suryatejapolepalli/enterprise-retail-ai-analytics-copilot

---


# 🧠 AI Workflow

```text
Business Question
        ↓
OpenAI GPT Model
        ↓
Athena SQL Generation
        ↓
Amazon Athena Query Execution
        ↓
Analytics Results
        ↓
Charts + Business Insights
```

---

# ⭐ Project Highlights

✅ End-to-End AWS Data Engineering Project  
✅ AI-Powered NL2SQL Copilot  
✅ Enterprise Retail Warehouse Design  
✅ Serverless Architecture  
✅ Production-Style ETL Framework  
✅ Real-Time Analytics Thinking  
✅ Interactive Visualizations  
✅ Resume & Interview Ready Project 🚀