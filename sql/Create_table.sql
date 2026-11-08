DROP TABLE IF EXISTS bronze_sysco_orders;

CREATE TABLE bronze_sysco_orders
(
    id SERIAL PRIMARY KEY,
    order_no VARCHAR(20),
    customer_no VARCHAR(20),
    order_date TIMESTAMP,
    delivery_date DATE,
    supplier VARCHAR(20),
    category VARCHAR(100),
    item_no VARCHAR(20),
    case_qty INTEGER,
    split_qty INTEGER,
    pack_size VARCHAR(50),
    brand VARCHAR(100),
    description TEXT,
    manufacturer_no VARCHAR(50),
    per_lb_flag VARCHAR(10),
    case_price NUMERIC(10,2),
    each_price NUMERIC(10,2),
    delivery_status VARCHAR(50),
    source_file VARCHAR(255),
    load_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);