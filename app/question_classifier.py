METADATA_KEYWORDS = [
    "meaning",
    "mean",
    "define",
    "definition",
    "describe",
    "metadata",
    "schema",
    "table",
    "column",
    "what does"
]

ANALYTICS_KEYWORDS = [
    "sum",
    "total",
    "average",
    "avg",
    "count",
    "top",
    "highest",
    "lowest",
    "revenue",
    "sales",
    "profit",
    "distribution",
    "trend",
    "compare"
]


def is_metadata_question(question):

    question = question.lower()

    analytics_match = any(
        keyword in question
        for keyword in ANALYTICS_KEYWORDS
    )

    if analytics_match:
        return False

    metadata_match = any(
        keyword in question
        for keyword in METADATA_KEYWORDS
    )

    return metadata_match