-- ==========================================
-- 1. Top 5 Funds by AUM
-- ==========================================

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- ==========================================
-- 2. Average NAV by Fund
-- ==========================================

SELECT
    amfi_code,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;

-- ==========================================
-- 3. Transactions by State
-- ==========================================

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- ==========================================
-- 4. Average Transaction Amount by State
-- ==========================================

SELECT
    state,
    ROUND(AVG(amount_inr),2) AS avg_amount
FROM fact_transactions
GROUP BY state
ORDER BY avg_amount DESC;

-- ==========================================
-- 5. Funds with Expense Ratio < 1%
-- ==========================================

SELECT
    scheme_name,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct;

-- ==========================================
-- 6. Top 5 Funds by Sharpe Ratio
-- ==========================================

SELECT
    amfi_code,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- ==========================================
-- 7. Top 5 Funds by Alpha
-- ==========================================

SELECT
    amfi_code,
    alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 5;

-- ==========================================
-- 8. Average Transaction Amount by Age Group
-- ==========================================

SELECT
    age_group,
    ROUND(AVG(amount_inr),2) AS avg_amount
FROM fact_transactions
GROUP BY age_group
ORDER BY avg_amount DESC;

-- ==========================================
-- 9. Top Fund Houses by AUM
-- ==========================================

SELECT
    fund_house,
    MAX(aum_crore) AS max_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY max_aum DESC
LIMIT 10;

-- ==========================================
-- 10. Risk Category Distribution
-- ==========================================

SELECT
    risk_category,
    COUNT(*) AS total_funds
FROM dim_fund
GROUP BY risk_category
ORDER BY total_funds DESC;