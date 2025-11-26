/* Objective: Calculate Year-Over-Year (YoY) Profit Growth per Category
Techniques: Common Table Expression (CTE), Window Function (LAG)
*/

WITH YearlyCategoryProfit AS (
    -- Step 1: Aggregate Profit by Year and Category
    SELECT 
        strftime('%Y', "Order Date") AS OrderYear, 
        Category, 
        SUM(Profit) AS TotalProfit
    FROM Orders
    GROUP BY 1, 2
)

-- Step 2: Calculate Growth using LAG
SELECT 
    OrderYear,
    Category,
    TotalProfit,
    -- LAG looks at the "previous" row (offset 1) within the same Category
    LAG(TotalProfit, 1) OVER (PARTITION BY Category ORDER BY OrderYear) AS PreviousYearProfit,
    
    -- Calculate Percentage Growth: (Current - Previous) / Previous * 100
    (TotalProfit - LAG(TotalProfit, 1) OVER (PARTITION BY Category ORDER BY OrderYear)) 
        / ABS(LAG(TotalProfit, 1) OVER (PARTITION BY Category ORDER BY OrderYear)) * 100 
    AS YoY_Growth_Percent
FROM YearlyCategoryProfit
ORDER BY Category, OrderYear;