BUSINESS_METADATA = """
fact_orders:
Contains retail transaction-level order data.

Columns:
- order_id: unique order identifier
- customer_id: customer identifier
- product_name: purchased product
- category: product category
- quantity: quantity ordered
- total_amount: total order revenue
- payment_status: payment completion status
- state: customer state
- city: customer city

fact_inventory:
Contains warehouse inventory information.

Columns:
- warehouse_id: warehouse identifier
- product_name: inventory product
- stock_quantity: available stock quantity
- reorder_level: minimum threshold before replenishment

Business KPIs:
- Revenue = SUM(total_amount)
- Best Selling Product = highest SUM(quantity)
- Top State Revenue = state with highest revenue
"""