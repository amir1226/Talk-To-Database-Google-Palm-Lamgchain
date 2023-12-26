few_shots = [
    {
        "question": "How many t-shirts do we have left for Nike in XS size and white color?",
        "sql_query": "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
        "sql_result": "Result of the SQL query",
        "answer": "93",
    },
    {
        "question": "How much is the total price of the inventory for all S-size t-shirts?",
        "sql_query": "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
        "sql_result": "Result of the SQL query",
        "answer": "136",
    },
    {
        "question": "If we have to sell all the Levi's T-shirts today with discounts applied. How much revenue  our store will generate (post discounts)?",
        "sql_query": "SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from\n(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi'\ngroup by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id\n ",
        "sql_result": "Result of the SQL query",
        "answer": "8614.1",
    },
    {
        "question": "If we have to sell all the Levi's T-shirts today. How much revenue our store will generate without discount?",
        "sql_query": "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
        "sql_result": "Result of the SQL query",
        "answer": "9587",
    },
    {
        "question": "How many white color Levi's shirt I have?",
        "sql_query": "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White'",
        "sql_result": "Result of the SQL query",
        "answer": "91",
    },
]
