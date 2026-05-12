import time
import boto3
import pandas as pd

ATHENA_DATABASE = "retail_enterprise_curated_db"
ATHENA_OUTPUT = "s3://retail-curated-surya/athena-results/"
AWS_REGION = "us-east-1"

athena = boto3.client("athena", region_name=AWS_REGION)


def run_athena_query(query):
    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={"Database": ATHENA_DATABASE},
        ResultConfiguration={"OutputLocation": ATHENA_OUTPUT}
    )

    query_execution_id = response["QueryExecutionId"]

    while True:
        status_response = athena.get_query_execution(
            QueryExecutionId=query_execution_id
        )

        state = status_response["QueryExecution"]["Status"]["State"]

        if state in ["SUCCEEDED", "FAILED", "CANCELLED"]:
            break

        time.sleep(2)

    if state != "SUCCEEDED":
        reason = status_response["QueryExecution"]["Status"].get(
            "StateChangeReason",
            "Unknown error"
        )
        raise Exception(f"Athena query failed: {reason}")

    result_response = athena.get_query_results(
        QueryExecutionId=query_execution_id
    )

    rows = result_response["ResultSet"]["Rows"]

    headers = [col.get("VarCharValue", "") for col in rows[0]["Data"]]

    data = []
    for row in rows[1:]:
        values = [item.get("VarCharValue", "") for item in row["Data"]]
        data.append(values)

    return pd.DataFrame(data, columns=headers)