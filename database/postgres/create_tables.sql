
-- Create the t_shirts table
CREATE TYPE brand_type AS ENUM('Van Huesen', 'Levi', 'Nike', 'Adidas');
CREATE TYPE color_type AS ENUM('Red', 'Blue', 'Black', 'White');
CREATE TYPE size_type AS ENUM('XS', 'S', 'M', 'L', 'XL');

CREATE TABLE t_shirts (
   t_shirt_id SERIAL PRIMARY KEY,
   brand brand_type NOT NULL,
   color color_type NOT NULL,
   size size_type NOT NULL,
   price INT CHECK (price BETWEEN 10 AND 50),
   stock_quantity INT NOT NULL,
   UNIQUE (brand, color, size)
);

-- Create the discounts table
CREATE TABLE discounts (
  discount_id SERIAL PRIMARY KEY,
  t_shirt_id INT NOT NULL,
  pct_discount NUMERIC(5,2) CHECK (pct_discount BETWEEN 0 AND 100),
  FOREIGN KEY (t_shirt_id) REFERENCES t_shirts(t_shirt_id)
);
