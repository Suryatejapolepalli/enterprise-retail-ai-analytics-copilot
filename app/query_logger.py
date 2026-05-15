import boto3
import uuid
import pandas as pd

from datetime import datetime

dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-east-1"
)

table = dynamodb.Table("query_history")


def save_query(question, sql, insight, query_type="analytics"):

    table.put_item(
        Item={
            "query_id": str(uuid.uuid4()),
            "question": question,
            "generated_sql": sql,
            "insight": insight,
            "query_type": query_type,
            "timestamp": datetime.now().isoformat()
        }
    )


def get_query_history():

    response = table.scan()

    items = response.get("Items", [])

    while "LastEvaluatedKey" in response:
        response = table.scan(
            ExclusiveStartKey=response["LastEvaluatedKey"]
        )
        items.extend(response.get("Items", []))

    if not items:
        return pd.DataFrame()

    df = pd.DataFrame(items)

    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df["date"] = df["timestamp"].dt.date

    return df