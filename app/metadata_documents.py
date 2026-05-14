metadata_docs = [

    {
        "topic": "reorder_level",
        "content": """
        reorder_level represents the minimum stock threshold.
        If inventory goes below reorder_level,
        products need replenishment.
        """
    },

    {
        "topic": "fact_orders",
        "content": """
        fact_orders stores transactional order-level data.
        It contains revenue, quantity, payment status,
        customer, product, and regional analytics information.
        """
    },

    {
        "topic": "dim_customer_scd2",
        "content": """
        dim_customer_scd2 is a slowly changing dimension type 2 table
        used for maintaining historical customer changes.
        """
    },

    {
        "topic": "revenue",
        "content": """
        Revenue is calculated using SUM(total_amount)
        from fact_orders table.
        """
    }

]