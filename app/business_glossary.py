BUSINESS_GLOSSARY = """

IMPORTANT:
Use warehouse values exactly as stored in source data.
Do not assume abbreviations.

Business Definitions:

Revenue:
SUM(total_amount)

Sales:
SUM(quantity)

Monthly Revenue:
SUM(total_amount)
GROUP BY year, month

Top Products:
GROUP BY product_name

Payment Distribution:
GROUP BY payment_status

Customer:
customer_id

Product:
product_name


Warehouse Values:

States:
Texas
California
Florida
New York

Categories:
Clothing
Electronics
Furniture
Grocery

Rules:

1. Revenue means SUM(total_amount)

2. Sales means SUM(quantity)

3. Use LOWER() for text comparisons

Example:
LOWER(category)=LOWER('Clothing')

Example:
LOWER(state)=LOWER('Texas')

4. Return Athena compatible SQL only

"""