/* Objective: Calculate Return Rate and Profit Margin by Market */
SELECT 
    o.Market,
    COUNT(DISTINCT o."Order ID") AS TotalOrders,
    COUNT(DISTINCT r."Order ID") AS ReturnedOrders,
    ROUND((COUNT(DISTINCT r."Order ID") * 1.0 / COUNT(DISTINCT o."Order ID")) * 100, 2) AS ReturnRate,
    ROUND(SUM(o.Profit) / SUM(o.Sales) * 100, 2) AS ProfitMargin
FROM Orders o
LEFT JOIN Returns r ON o."Order ID" = r."Order ID"
GROUP BY o.Market
ORDER BY ReturnRate DESC;