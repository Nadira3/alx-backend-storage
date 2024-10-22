-- script that creates a trigger that decreases the quantity of an item after adding a new order
-- Set a custom delimiter to avoid conflicts with the default statement terminator
DELIMITER //

-- Drop the trigger if it already exists
DROP TRIGGER IF EXISTS decrease_quantity_after_order;

//

-- Create the trigger
CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the quantity in the items table based on the ordered item's name
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name; -- Assuming item_name is the correct column in orders
END;
//

-- Reset the delimiter back to the default
DELIMITER ;
