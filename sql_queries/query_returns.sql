/* Objective: Calculate Return Rate and Profit Margin by Market */

SELECT 
    o.Market,
    
    -- 1. Count unique orders (The Denominator)
    COUNT(DISTINCT o."Order ID") AS TotalOrders,
    
    -- 2. Count returned orders (The Numerator)
    -- If the JOIN didn't find a match, r."Order ID" is NULL and won't be counted.
    COUNT(DISTINCT r."Order ID") AS ReturnedOrders,
    
    -- 3. Calculate Return Rate %
    -- Multiply by 1.0 to force decimal math (Integer / Integer = Integer in SQL)
    ROUND((COUNT(DISTINCT r."Order ID") * 1.0 / COUNT(DISTINCT o."Order ID")) * 100, 2) AS ReturnRate,
    
    -- 4. Calculate Profit Margin (Profit / Sales)
    ROUND(SUM(o.Profit) / SUM(o.Sales) * 100, 2) AS ProfitMargin
    
FROM Orders o
-- The Magic: Join Returns table (r) to Orders table (o)
-- LEFT JOIN keeps ALL orders, even if they weren't returned
LEFT JOIN Returns r 
    ON o."Order ID" = r."Order ID"

GROUP BY o.Market
ORDER BY ReturnRate DESC;

