import time
import boto3
import pandas as pd


ATHENA_DATABASE = "retail_enterprise_curated_db"
ATHENA_OUTPUT = "s3://retail-athena-surya/"
AWS_REGION = "us-east-1"


athena = boto3.client(
    "athena",
    region_name=AWS_REGION
)


def run_athena_query(query):

    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            "Database": ATHENA_DATABASE
        },
        ResultConfiguration={
            "OutputLocation": ATHENA_OUTPUT
        }
    )

    query_execution_id = response["QueryExecutionId"]

    while True:

        status = athena.get_query_execution(
            QueryExecutionId=query_execution_id
        )

        state = status["QueryExecution"]["Status"]["State"]

        if state in ["SUCCEEDED", "FAILED", "CANCELLED"]:
            break

        time.sleep(1)

    if state != "SUCCEEDED":

        reason = status["QueryExecution"]["Status"].get(
            "StateChangeReason",
            "Unknown Athena error"
        )

        raise Exception(reason)

    results = athena.get_query_results(
        QueryExecutionId=query_execution_id
    )

    rows = results["ResultSet"]["Rows"]

    headers = [
        col["VarCharValue"]
        for col in rows[0]["Data"]
    ]

    data = []

    for row in rows[1:]:

        values = [
            item.get("VarCharValue", None)
            for item in row["Data"]
        ]

        data.append(values)

    df = pd.DataFrame(
        data,
        columns=headers
    )

    return df