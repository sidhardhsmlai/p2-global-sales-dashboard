/* Objective: Identify Top Performing Sales Managers in the USCA Market */

SELECT 
    p.Person AS Manager,
    o.Region,
    
    -- 1. Calculate Total Sales attributed to this manager
    ROUND(SUM(o.Sales), 2) AS TotalSales,
    
    -- 2. Calculate Profitability to see if they are making money
    ROUND(SUM(o.Profit), 2) AS TotalProfit,
    
    -- 3. Profit Margin (Quality of Sales)
    ROUND(SUM(o.Profit) / SUM(o.Sales) * 100, 2) AS ProfitMargin_Percent
    
FROM Orders o
-- The Magic: Join People table (p) on Region
INNER JOIN People p 
    ON o.Region = p.Region

-- Filter for only the US/Canada market group we defined
WHERE o.Market_Group = 'USCA'

GROUP BY p.Person, o.Region
ORDER BY TotalSales DESC;
