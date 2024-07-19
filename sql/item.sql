/* DDL statements for item table */
CREATE TABLE item (
    id INTEGER NOT NULL,
    name VARCHAR(30) NOT NULL,
    barcode VARCHAR(12) NOT NULL,
    description VARCHAR(1024),
    price FLOAT NOT NULL,
    owner_id INTEGER DEFAULT NULL,
    PRIMARY KEY (id),
    UNIQUE (name),
    UNIQUE (barcode),
    FOREIGN KEY(owner_id) REFERENCES user (id)
);


/* DML statements for item table */
INSERT INTO item (name, barcode, description, price) VALUES
('item1', '11111', 'This is item1', 10.99),
('item2', '22222', 'This is item2', 9.99),
('item3', '33333', 'This is item3', 8.99),
('item4', '44444', 'This is item4', 7.99),
('item5', '55555', 'This is item5', 6.99),
('item6', '66666', 'This is item6', 5.99),
('item7', '77777', 'This is item7', 4.99),
('item8', '88888', 'This is item8', 3.99),
('item9', '99999', 'This is item9', 2.99),
('item10', '101010', 'This is item10', 1.99),
('item11', '111111', 'This is item11', 0.99),
('item12', '12121212', 'This is item12', 30.99);