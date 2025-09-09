# Data Dictionary — p1_sales_stage

| Column | Type | Null % | Allowed Values / Range | Example | Notes |
|---|---|---:|---|---|---|
| order_id | int64 | 0.0% | 10001 – 11200 | 10001, 10002, 10003 |  |
| order_date | object | 0.0% | Top10: 2024-03-11, 2023-08-31, 2024-04-20, 2023-05-28, 2023-11-14, 2024-07-20, 2024-05-13, 2024-03-16, 2023-06-23, 2024-11-10 | 2023-12-12, 2024-05-01, 2023-10-02 |  |
| ship_date | object | 0.0% | Top10: 2024-04-29, 2024-01-10, 2023-10-16, 2023-02-05, 2023-06-29, 2024-02-12, 2024-11-08, 2023-08-28, 2023-06-10, 2023-05-30 | 2023-12-18, 2024-05-07, 2023-10-03 |  |
| customer_id | int64 | 0.0% | 5000 – 5999 | 5732, 5132, 5643 |  |
| customer_segment | object | 0.0% | corporate, home office, consumer | consumer, corporate, home office |  |
| region | object | 0.0% | central, east, west, south | west, central, south |  |
| product_id | int64 | 0.0% | 2001 – 2999 | 2931, 2317, 2432 |  |
| category | object | 0.0% | technology, office supplies, furniture | technology, office supplies, furniture |  |
| sub_category | object | 0.0% | paper, phones, accessories, tables, binders, chairs | phones, paper, chairs |  |
| product_name | object | 0.0% | Top10: SKU-181, SKU-812, SKU-237, SKU-632, SKU-352, SKU-116, SKU-724, SKU-800, SKU-926, SKU-804 | SKU-573, SKU-689, SKU-687 |  |
| quantity | int64 | 0.0% | 1 – 7 | 1, 6, 5 |  |
| unit_price | float64 | 0.0% | 5.0 – 139.47 | 91.2, 53.69, 69.09 |  |
| discount | float64 | 0.0% | 0.0 – 0.3 | 0.0, 0.1, 0.2 |  |
| revenue | float64 | 0.0% | 4.58 – 810.11 | 91.2, 322.14, 310.91 |  |
| gross_margin_pct | float64 | 0.0% | 0.2 – 0.6 | 0.39, 0.428, 0.326 |  |
| gross_profit | float64 | 0.0% | 1.35 – 396.34 | 35.57, 137.88, 101.36 |  |
| discount_band | object | 0.0% | 0%, 10-20%, 20%+ | 0%, 10-20%, 20%+ |  |
