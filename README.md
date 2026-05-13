# 🚀 Enterprise Retail AI Analytics Copilot  
### AI-Powered Serverless Retail Analytics Platform on AWS

![AWS](https://img.shields.io/badge/AWS-Serverless-orange?logo=amazonaws)
![Python](https://img.shields.io/badge/Python-Analytics-blue?logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-NL2SQL-green?logo=openai)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![Athena](https://img.shields.io/badge/Amazon-Athena-purple?logo=amazonaws)
![Glue](https://img.shields.io/badge/AWS-Glue-yellow?logo=amazonaws)

---

## 📌 Project Overview

Enterprise Retail AI Analytics Copilot is a production-style AI-powered analytics platform built on AWS. It allows users to ask business questions in natural language and receive Athena SQL queries, analytics results, visualizations, CSV downloads, query history, and AI-generated business insights.

This project combines AWS data engineering, enterprise data warehousing, and generative AI to create a lightweight conversational analytics copilot.

---

## 🎯 Business Problem

Business users often depend on data analysts or engineers to write SQL queries and generate insights from enterprise data warehouses. This slows down decision-making and creates dependency on technical teams.

This application solves that problem by allowing users to ask questions like:

```text
Show top 5 states by revenue
Best selling product
Which city has highest revenue
Show payment status distribution
Top 3 products by sales
```

The system automatically converts the question into Athena SQL, runs it against the curated AWS data warehouse, and displays results with charts and insights.

---

## ✨ Live Features

- ✅ Natural Language to SQL using OpenAI
- ✅ Amazon Athena query execution
- ✅ Interactive Streamlit dashboard
- ✅ AI-generated business insights
- ✅ Query history tracking
- ✅ CSV download support
- ✅ KPI cards
- ✅ Auto visualization
- ✅ Generated SQL display
- ✅ AWS Glue + S3 + Athena integration
- ✅ Enterprise data warehouse design
- ✅ SCD Type 1 and SCD Type 2 implementation

---

## 🧠 AI Workflow

```text
Business Question
        ↓
Streamlit Frontend
        ↓
OpenAI GPT Model
        ↓
Schema-Aware Prompt Engineering
        ↓
Athena SQL Generation
        ↓
Amazon Athena Query Execution
        ↓
Curated S3 Data Warehouse
        ↓
Results + Charts + AI Business Insights
```

---

## 🏗️ Architecture Diagram

![Architecture Diagram](architecture/architecture_diagram.png)

---

## 🧾 Implementation Proof

![Implementation Proof](architecture/implementation_proof.png)

---

## ☁️ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon S3 | Raw and curated data lake storage |
| AWS Glue | PySpark ETL processing |
| AWS Lambda | Event-driven ETL orchestration |
| Amazon Athena | Serverless SQL query engine |
| AWS Glue Data Catalog | Metadata catalog |
| Amazon CloudWatch | Monitoring and logs |
| Amazon SNS | Failure alerts and notifications |
| AWS IAM | Access control and permissions |
| OpenAI API | Natural language to SQL generation |
| Streamlit | Interactive web application |

---

## 🧱 System Components

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| AI Layer | OpenAI GPT |
| Prompt Layer | Schema-aware prompt engineering |
| Query Engine | Amazon Athena |
| ETL Layer | AWS Glue PySpark |
| Storage Layer | Amazon S3 |
| Metadata Layer | AWS Glue Data Catalog |
| Orchestration | AWS Lambda |
| Monitoring | CloudWatch + SNS |

---

## 🔄 Enterprise ETL Pipeline Flow

```text
Retail CSV Files
        ↓
Amazon S3 Raw Layer
        ↓
AWS Lambda Trigger
        ↓
AWS Glue PySpark ETL Job
        ↓
Data Validation
        ↓
Reject Handling
        ↓
SCD Type 1 and SCD Type 2 Processing
        ↓
Fact and Dimension Loading
        ↓
Audit and Reconciliation
        ↓
Curated Parquet Warehouse
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

- Revenue analysis
- Product sales analysis
- Customer order analysis
- Payment status analytics
- State and city-level performance

#### fact_inventory

```text
Grain = 1 row per product per warehouse
```

Used for:

- Inventory monitoring
- Low stock detection
- Reorder-level analysis
- Warehouse-level stock tracking

---

### Dimension Tables

#### dim_customer_scd2

Implemented using SCD Type 2 to track customer history.

Includes:

- Customer details
- City and state changes
- Effective start date
- Effective end date
- Current flag
- Historical tracking

#### dim_product_scd1

Implemented using SCD Type 1 overwrite logic.

Includes:

- Product name
- Category
- Price
- Latest product attributes

---

## 🏢 Enterprise Features

### Data Validation Framework

Implemented validation checks for:

- Null values
- Duplicate records
- Invalid datatypes
- Missing required fields
- Business rule violations

---

### Reject Handling Framework

Invalid records are redirected into reject zones with:

- Reject reason
- Rejected timestamp
- Source identification

---

### Audit Logging Framework

Audit logs capture:

- Job name
- Entity name
- Record counts
- Target path
- Load timestamp
- Job status

---

### Reconciliation Framework

Reconciliation checks compare:

- Source record count
- Valid record count
- Reject record count
- Target record count

This ensures data consistency between raw and curated layers.

---

### Monitoring and Alerting

Implemented monitoring using:

- Amazon CloudWatch logs
- CloudWatch alarms
- SNS email alerts
- Glue job failure notifications

---

## 📊 AI Analytics Copilot Features

### Natural Language to SQL

The application converts business questions into Athena-compatible SQL.

Example:

```text
User: Show top 5 states by revenue
```

Generated SQL:

```sql
SELECT
    state,
    SUM(total_amount) AS revenue
FROM retail_enterprise_curated_db.fact_orders
GROUP BY state
ORDER BY revenue DESC
LIMIT 5;
```

---

### Schema-Aware Prompt Engineering

The LLM is guided using table and column context so that it generates SQL only using available warehouse tables.

Prompt rules include:

- Generate Athena-compatible SQL
- Avoid unnecessary columns
- Use only provided schema
- Apply dynamic LIMIT handling
- Select only requested columns
- Use aggregations when needed
- Avoid unsupported SQL syntax where possible

---

### AI-Generated Business Insights

After Athena returns results, OpenAI generates executive-style business insights.

Example insight:

```text
The analysis highlights the top-performing states by revenue.
Revenue is concentrated in a small number of regions, which can help guide
regional marketing, inventory planning, and sales strategy.
```

---

### Query History

The application stores recent user questions during the session.

This helps users review previous analytics requests and supports conversational-style analysis.

---

### CSV Download

Users can download query results directly from the dashboard as a CSV file.

---

### Auto Visualization

If the query returns a numeric metric, the application automatically generates a chart.

Supported examples:

- Revenue by state
- Sales by product
- Payment status distribution
- Inventory metrics
- Top-N ranking results

---

## 📸 Application Screenshots

### Streamlit Dashboard

![Dashboard](screenshots/dashboard.png)

---

### Generated Athena SQL

![Generated SQL](screenshots/generated_sql.png)

---

### Query Results

![Query Results](screenshots/query_results.png)

---

### Visualization

![Visualization](screenshots/chart.png)

---

### AI Business Insights

![AI Business Insights](screenshots/ai_business_insights.png)

---

### AI Query History

![AI Query History](screenshots/query_history.png)

---

## 🧪 Sample Athena Queries

### Revenue by State

```sql
SELECT
    state,
    SUM(total_amount) AS revenue
FROM retail_enterprise_curated_db.fact_orders
GROUP BY state
ORDER BY revenue DESC
LIMIT 5;
```

---

### Best Selling Product

```sql
SELECT
    product_name
FROM retail_enterprise_curated_db.fact_orders
GROUP BY product_name
ORDER BY SUM(quantity) DESC
LIMIT 1;
```

---

### Payment Status Distribution

```sql
SELECT
    payment_status,
    COUNT(*) AS total_count
FROM retail_enterprise_curated_db.fact_orders
GROUP BY payment_status
LIMIT 10;
```

---

### Low Inventory Detection

```sql
SELECT
    product_name,
    warehouse_id,
    stock_quantity,
    reorder_level
FROM retail_enterprise_curated_db.fact_inventory
WHERE stock_quantity < reorder_level;
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

- OpenAI API keys are managed using environment variables
- AWS credentials are configured using AWS CLI profiles
- No secrets or credentials are hardcoded in the repository
- `.gitignore` is used to prevent local environment files from being pushed
- API keys and AWS credentials should never be committed to GitHub

Example environment variable:

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
│   └── insight_generator.py
│
├── architecture/
│   ├── architecture_diagram.png
│   └── implementation_proof.png
│
├── screenshots/
│   ├── dashboard.png
│   ├── generated_sql.png
│   ├── query_results.png
│   ├── chart.png
│   ├── ai_business_insights.png
│   └── query_history.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🛠️ Technical Skills Demonstrated

### AWS and Cloud

- Amazon S3
- AWS Glue
- AWS Lambda
- Amazon Athena
- AWS Glue Data Catalog
- Amazon CloudWatch
- Amazon SNS
- AWS IAM

### Data Engineering

- PySpark ETL
- Data Lake Architecture
- Data Warehousing
- Dimensional Modeling
- SCD Type 1
- SCD Type 2
- Data Validation
- Audit Logging
- Reconciliation
- Reject Handling

### AI and Analytics

- OpenAI API
- Natural Language to SQL
- Prompt Engineering
- AI Business Insight Generation
- Streamlit Dashboarding
- Conversational Analytics
- Automated Visualizations

---

## 📈 Project Impact

This project demonstrates how enterprise data engineering and generative AI can be combined to build intelligent analytics platforms.

It reduces dependency on manual SQL writing and helps business users explore data through natural language questions.

The solution represents a practical example of how AI copilots can sit on top of cloud data warehouses to accelerate analytics and business decision-making.

---

## 💼 Resume Highlights

- Built an AI-powered NL2SQL analytics copilot using AWS Athena, OpenAI, Streamlit, and enterprise data warehousing concepts.
- Developed a serverless retail analytics platform using AWS Glue, Lambda, S3, Athena, CloudWatch, and SNS.
- Implemented SCD Type 1 and SCD Type 2 processing with PySpark for enterprise dimensional modeling.
- Created audit logging, reconciliation, reject handling, and data validation frameworks for production-style ETL pipelines.
- Integrated AI-generated executive insights, query history, CSV download, KPI cards, and automated visualizations.

---

## ⚠️ Limitations

- Current version uses OpenAI SDK directly instead of LangChain or LangGraph
- Complex multi-step analytical questions may require additional SQL validation
- Athena performance depends on partitioning, file format, and query design
- Query history is session-based and not yet persisted in a database
- User authentication and role-based access control are not yet implemented

---

## 🚀 Future Enhancements

- LangChain or LangGraph agent workflow
- RAG-based metadata assistant
- SQL validation and auto-retry layer
- Persistent query history using DynamoDB or PostgreSQL
- Redis caching for faster repeated analytics
- Pre-aggregated KPI tables
- Bedrock model support
- Role-based access control
- Docker deployment
- Terraform Infrastructure as Code
- CI/CD using GitHub Actions
- Live cloud deployment

---

## 👨‍💻 Author

### Surya Teja Polepalli

GitHub:  
https://github.com/Suryatejapolepalli

Project Repository:  
https://github.com/Suryatejapolepalli/enterprise-retail-ai-analytics-copilot

---

## ⭐ Project Highlights

✅ End-to-End AWS Data Engineering Project  
✅ AI-Powered Natural Language Analytics  
✅ Enterprise Retail Warehouse Design  
✅ Serverless AWS Architecture  
✅ Production-Style ETL Framework  
✅ OpenAI-Powered NL2SQL  
✅ Streamlit Interactive Dashboard  
✅ AI Business Insight Generation  
✅ Query History and CSV Export  
✅ Resume and Interview Ready Project