-- ============================================================================
-- Pattern Analytics - European Banking Customer Intelligence
-- Production Analytical Views: Aggregations, Risk Indices, & Exposure
-- Target Database: PostgreSQL / Supabase
-- ============================================================================

-- 1. Portfolio Executive KPI Summary
CREATE OR REPLACE VIEW v_executive_portfolio_summary AS
SELECT
    COUNT(*) AS total_customers,
    SUM(exited) AS total_churned,
    ROUND((AVG(exited) * 100.0), 2) AS overall_churn_rate_pct,
    COUNT(*) FILTER (WHERE balance > 50000 AND estimated_salary > 100000) AS total_high_value_customers,
    COUNT(*) FILTER (WHERE balance > 50000 AND estimated_salary > 100000 AND exited = 1) AS high_value_churned_customers,
    ROUND((AVG(exited) FILTER (WHERE balance > 50000 AND estimated_salary > 100000) * 100.0), 2) AS high_value_churn_rate_pct,
    ROUND(SUM(balance), 2) AS total_portfolio_balance,
    ROUND(SUM(balance) FILTER (WHERE exited = 1), 2) AS total_churned_balance_exposure,
    ROUND(AVG(balance) FILTER (WHERE exited = 1), 2) AS avg_balance_churned,
    ROUND(AVG(balance) FILTER (WHERE exited = 0), 2) AS avg_balance_retained
FROM european_bank_customers;

-- 2. Geographic Risk Index & Cross-Country Comparison
CREATE OR REPLACE VIEW v_geographic_risk_index AS
WITH overall_benchmark AS (
    SELECT AVG(exited) AS benchmark_churn_rate
    FROM european_bank_customers
)
SELECT
    c.geography,
    COUNT(*) AS customer_count,
    SUM(c.exited) AS churned_count,
    ROUND((AVG(c.exited) * 100.0), 2) AS churn_rate_pct,
    ROUND((AVG(c.exited) / b.benchmark_churn_rate)::numeric, 2) AS risk_index,
    ROUND(SUM(c.balance), 2) AS total_market_balance,
    ROUND(SUM(c.balance) FILTER (WHERE c.exited = 1), 2) AS market_balance_exposure
FROM european_bank_customers c
CROSS JOIN overall_benchmark b
GROUP BY c.geography, b.benchmark_churn_rate
ORDER BY churn_rate_pct DESC;

-- 3. Age Demographic Segmentation View
CREATE OR REPLACE VIEW v_age_segment_churn AS
SELECT
    CASE
        WHEN age < 30 THEN 'Under 30'
        WHEN age <= 45 THEN '30-45'
        WHEN age <= 60 THEN '46-60'
        ELSE '60+'
    END AS age_group,
    COUNT(*) AS customer_count,
    SUM(exited) AS churned_count,
    ROUND((AVG(exited) * 100.0), 2) AS churn_rate_pct,
    ROUND(AVG(balance), 2) AS avg_balance,
    ROUND(SUM(balance) FILTER (WHERE exited = 1), 2) AS churned_balance_exposure
FROM european_bank_customers
GROUP BY
    CASE
        WHEN age < 30 THEN 'Under 30'
        WHEN age <= 45 THEN '30-45'
        WHEN age <= 60 THEN '46-60'
        ELSE '60+'
    END
ORDER BY churn_rate_pct DESC;

-- 4. Product Bundling Hazard & Penetration View
CREATE OR REPLACE VIEW v_product_penetration_risk AS
SELECT
    num_of_products,
    COUNT(*) AS customer_count,
    SUM(exited) AS churned_count,
    ROUND((AVG(exited) * 100.0), 2) AS churn_rate_pct,
    ROUND(SUM(balance) FILTER (WHERE exited = 1), 2) AS churned_balance_exposure
FROM european_bank_customers
GROUP BY num_of_products
ORDER BY num_of_products ASC;

-- 5. Customer Activity & Engagement Comparison View
CREATE OR REPLACE VIEW v_activity_churn_comparison AS
SELECT
    CASE WHEN is_active_member = 1 THEN 'Active Member' ELSE 'Inactive Member' END AS engagement_status,
    COUNT(*) AS customer_count,
    SUM(exited) AS churned_count,
    ROUND((AVG(exited) * 100.0), 2) AS churn_rate_pct,
    ROUND(AVG(balance), 2) AS avg_balance,
    ROUND(SUM(balance) FILTER (WHERE exited = 1), 2) AS churned_balance_exposure
FROM european_bank_customers
GROUP BY is_active_member
ORDER BY churn_rate_pct DESC;

-- 6. High-Value Customer Capital Exposure View
CREATE OR REPLACE VIEW v_high_value_customer_exposure AS
SELECT
    geography,
    gender,
    COUNT(*) AS total_high_value_accounts,
    SUM(exited) AS high_value_churned_count,
    ROUND((AVG(exited) * 100.0), 2) AS high_value_churn_rate_pct,
    ROUND(SUM(balance), 2) AS total_high_value_balance,
    ROUND(SUM(balance) FILTER (WHERE exited = 1), 2) AS high_value_balance_exposure
FROM european_bank_customers
WHERE balance > 50000 AND estimated_salary > 100000
GROUP BY geography, gender
ORDER BY high_value_balance_exposure DESC;

-- 7. Account Balance Tier Segmentation View
CREATE OR REPLACE VIEW v_balance_tier_churn AS
SELECT
    CASE
        WHEN balance = 0 THEN 'Zero Balance'
        WHEN balance <= 50000 THEN 'Low Balance (1-50k)'
        ELSE 'High Balance (>50k)'
    END AS balance_segment,
    COUNT(*) AS customer_count,
    SUM(exited) AS churned_count,
    ROUND((AVG(exited) * 100.0), 2) AS churn_rate_pct,
    ROUND(SUM(balance) FILTER (WHERE exited = 1), 2) AS total_balance_exposure
FROM european_bank_customers
GROUP BY
    CASE
        WHEN balance = 0 THEN 'Zero Balance'
        WHEN balance <= 50000 THEN 'Low Balance (1-50k)'
        ELSE 'High Balance (>50k)'
    END
ORDER BY churn_rate_pct DESC;
