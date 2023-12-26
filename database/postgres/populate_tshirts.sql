CREATE OR REPLACE FUNCTION PopulateTShirts()
RETURNS VOID AS $$
DECLARE
   counter INT := 0;
   max_records INT := 20;  -- Reduce the number of iterations to 20
   brand brand_type;
   color color_type;
   size size_type;
   price INT;
   stock INT;
BEGIN
   -- Seed the random number generator
   PERFORM setseed(random());

   WHILE counter < max_records LOOP
       -- Generate random values
       brand := CASE floor(1 + random() * 4)
                   WHEN 1 THEN 'Van Huesen'
                   WHEN 2 THEN 'Levi'
                   WHEN 3 THEN 'Nike'
                   WHEN 4 THEN 'Adidas'
                END;

       color := CASE floor(1 + random() * 4)
                   WHEN 1 THEN 'Red'
                   WHEN 2 THEN 'Blue'
                   WHEN 3 THEN 'Black'
                   WHEN 4 THEN 'White'
                END;

       size := CASE floor(1 + random() * 5)
                   WHEN 1 THEN 'XS'
                   WHEN 2 THEN 'S'
                   WHEN 3 THEN 'M'
                   WHEN 4 THEN 'L'
                   WHEN 5 THEN 'XL'
                END;

       price := floor(10 + random() * 41);
       stock := floor(10 + random() * 91);

       -- Attempt to insert a new record
       -- Duplicate brand, color, size combinations will be ignored due to the unique constraint
       BEGIN
           -- Handle duplicate key error
           BEGIN
               INSERT INTO t_shirts (brand, color, size, price, stock_quantity)
               VALUES (brand, color, size, price, stock);
               counter := counter + 1;
           EXCEPTION
               WHEN unique_violation THEN NULL;
           END;
       END;
   END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Call the stored procedure to populate the t_shirts table
SELECT PopulateTShirts();


