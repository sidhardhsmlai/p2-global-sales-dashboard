/* Objective: Identify Top Performing Sales Managers in USCA */
SELECT 
    p.Person AS Manager,
    o.Region,
    ROUND(SUM(o.Sales), 2) AS TotalSales,
    ROUND(SUM(o.Profit), 2) AS TotalProfit,
    ROUND(SUM(o.Profit) / SUM(o.Sales) * 100, 2) AS ProfitMargin_Percent
FROM Orders o
INNER JOIN People p ON o.Region = p.Region
WHERE o.Market_Group = 'USCA'
GROUP BY p.Person, o.Region
ORDER BY TotalSales DESC;