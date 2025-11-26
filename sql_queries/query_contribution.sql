/* Objective: Calculate Profit Contribution % of each Sub-Category within its Category */

-- Step 1: Pre-calculate the "Slices" (Profit per Sub-Category)
WITH SubCategoryStats AS (
    SELECT 
        Category, 
        "Sub-Category" AS SubCategory, 
        SUM(Profit) AS SubCategoryProfit
    FROM Orders
    GROUP BY 1, 2
)

-- Step 2: Calculate the "Whole Pie" and the Percentage
SELECT 
    Category,
    SubCategory,
    SubCategoryProfit,
    
    -- The Magic: Sum up ALL profits for this Category and put it on every row
    SUM(SubCategoryProfit) OVER (PARTITION BY Category) AS TotalCategoryProfit,
    
    -- The Math: Part / Total * 100
    (SubCategoryProfit / SUM(SubCategoryProfit) OVER (PARTITION BY Category)) * 100 AS ContributionPercent
    
FROM SubCategoryStats
ORDER BY Category, ContributionPercent DESC;
