import boto3
import uuid

from datetime import datetime

dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-east-1"
)

table = dynamodb.Table(
    "query_history"
)


def save_query(
    question,
    sql,
    insight
):

    table.put_item(

        Item={

            "query_id":
            str(uuid.uuid4()),

            "question":
            question,

            "generated_sql":
            sql,

            "insight":
            insight,

            "timestamp":
            datetime.now().isoformat()

        }

    )