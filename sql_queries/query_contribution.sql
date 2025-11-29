/* Objective: Calculate Profit Contribution % of each Sub-Category */
WITH SubCategoryStats AS (
    SELECT 
        Category, 
        "Sub-Category" AS SubCategory, 
        SUM(Profit) AS SubCategoryProfit
    FROM Orders
    GROUP BY 1, 2
)
SELECT 
    Category,
    SubCategory,
    SubCategoryProfit,
    SUM(SubCategoryProfit) OVER (PARTITION BY Category) AS TotalCategoryProfit,
    (SubCategoryProfit / SUM(SubCategoryProfit) OVER (PARTITION BY Category)) * 100 AS ContributionPercent
FROM SubCategoryStats
ORDER BY Category, ContributionPercent DESC;