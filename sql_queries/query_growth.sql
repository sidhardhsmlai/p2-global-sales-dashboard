/* Objective: Calculate Year-Over-Year (YoY) Profit Growth per Category */
WITH YearlyCategoryProfit AS (
    SELECT 
        strftime('%Y', "Order Date") AS OrderYear, 
        Category, 
        SUM(Profit) AS TotalProfit
    FROM Orders
    GROUP BY 1, 2
)
SELECT 
    OrderYear,
    Category,
    TotalProfit,
    LAG(TotalProfit, 1) OVER (PARTITION BY Category ORDER BY OrderYear) AS PreviousYearProfit,
    (TotalProfit - LAG(TotalProfit, 1) OVER (PARTITION BY Category ORDER BY OrderYear)) 
      / ABS(LAG(TotalProfit, 1) OVER (PARTITION BY Category ORDER BY OrderYear)) * 100 
      AS YoY_Growth_Percent
FROM YearlyCategoryProfit
ORDER BY Category, OrderYear;
