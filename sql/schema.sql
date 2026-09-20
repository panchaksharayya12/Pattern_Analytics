-- ============================================================================
-- Pattern Analytics - European Banking Customer Intelligence
-- Database Schema: Customer Table, Constraints, and Indexes
-- Target Database: PostgreSQL / Supabase
-- ============================================================================

-- 1. Enable UUID extension if needed
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 2. Drop existing table if recreating
DROP TABLE IF EXISTS european_bank_customers CASCADE;

-- 3. Create Main Customer Table
CREATE TABLE european_bank_customers (
    id BIGSERIAL PRIMARY KEY,
    year INT NOT NULL DEFAULT 2025,
    customer_id BIGINT UNIQUE NOT NULL,
    surname VARCHAR(100) NOT NULL,
    credit_score INT NOT NULL,
    geography VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    age INT NOT NULL,
    tenure INT NOT NULL,
    balance NUMERIC(15, 2) NOT NULL DEFAULT 0.00,
    num_of_products INT NOT NULL DEFAULT 1,
    has_cr_card INT NOT NULL DEFAULT 1,
    is_active_member INT NOT NULL DEFAULT 1,
    estimated_salary NUMERIC(15, 2) NOT NULL DEFAULT 0.00,
    exited INT NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW(),

    -- Constraints
    CONSTRAINT chk_credit_score CHECK (credit_score BETWEEN 300 AND 850),
    CONSTRAINT chk_geography CHECK (geography IN ('France', 'Germany', 'Spain')),
    CONSTRAINT chk_gender CHECK (gender IN ('Female', 'Male')),
    CONSTRAINT chk_age CHECK (age >= 18),
    CONSTRAINT chk_tenure CHECK (tenure BETWEEN 0 AND 10),
    CONSTRAINT chk_balance CHECK (balance >= 0.00),
    CONSTRAINT chk_num_of_products CHECK (num_of_products BETWEEN 1 AND 4),
    CONSTRAINT chk_has_cr_card CHECK (has_cr_card IN (0, 1)),
    CONSTRAINT chk_is_active_member CHECK (is_active_member IN (0, 1)),
    CONSTRAINT chk_exited CHECK (exited IN (0, 1))
);

-- 4. High-Performance Query Indexes
CREATE INDEX idx_customers_geography ON european_bank_customers(geography);
CREATE INDEX idx_customers_exited ON european_bank_customers(exited);
CREATE INDEX idx_customers_geo_exited ON european_bank_customers(geography, exited);
CREATE INDEX idx_customers_active_exited ON european_bank_customers(is_active_member, exited);
CREATE INDEX idx_customers_age ON european_bank_customers(age);
CREATE INDEX idx_customers_products ON european_bank_customers(num_of_products);
CREATE INDEX idx_customers_high_value ON european_bank_customers(balance, estimated_salary) WHERE (balance > 50000 AND estimated_salary > 100000);

-- 5. Row-Level Security (Supabase)
ALTER TABLE european_bank_customers ENABLE ROW LEVEL SECURITY;

-- Allow public read access (for dashboard analytics)
CREATE POLICY "Allow public read-only access"
    ON european_bank_customers
    FOR SELECT
    USING (true);

-- 6. Table & Column Documentation
COMMENT ON TABLE european_bank_customers IS 'Retail banking customer dataset covering 10,000 accounts across France, Germany, and Spain with behavioral, financial, and churn indicators.';
COMMENT ON COLUMN european_bank_customers.customer_id IS 'Unique anonymous customer account identifier.';
COMMENT ON COLUMN european_bank_customers.credit_score IS 'FICO-like numerical credit rating (300-850).';
COMMENT ON COLUMN european_bank_customers.geography IS 'Customer market jurisdiction: France, Germany, or Spain.';
COMMENT ON COLUMN european_bank_customers.balance IS 'Current customer account ledger balance in Euros.';
COMMENT ON COLUMN european_bank_customers.num_of_products IS 'Number of active bank products held (1-4).';
COMMENT ON COLUMN european_bank_customers.is_active_member IS 'Binary activity flag: 1 = Active, 0 = Inactive.';
COMMENT ON COLUMN european_bank_customers.exited IS 'Historical churn flag: 1 = Exited bank, 0 = Retained.';
