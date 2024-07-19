# sql commands for application's models

you can use the sql commands for create and insert in user and item tables.

for example, you can use sqlite3 command for create and insert into database

```bash
sqlite3 database.db
```

## to create tables and manipulate them

you can use these sql commands

## user table

```sql
/* DDL for the user table */
CREATE TABLE user (
    id INTEGER NOT NULL,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(120) NOT NULL,
    password_hash VARCHAR(60) NOT NULL,
    budget FLOAT NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (username),
    UNIQUE (email)
);


/* DML for the user table */
INSERT INTO user (username, email, password_hash, budget) VALUES
('user1', 'Zt0LQ1@example.com', 'password1', 1000.00),
('user2', 'Zt0LQ2@example.com', 'password2', 2000.00),
('user3', 'Zt0LQ3@example.com', 'password3', 3000.00),
('user4', 'Zt0LQ4@example.com', 'password4', 4000.00),
('user5', 'Zt0LQ5@example.com', 'password5', 5000.00),
('user6', 'Zt0LQ6@example.com', 'password6', 6000.00),
('user7', 'Zt0LQ7@example.com', 'password7', 7000.00),
('user8', 'Zt0LQ8@example.com', 'password8', 8000.00),
('user9', 'Zt0LQ9@example.com', 'password9', 9000.00),
('user10', 'Zt0LQ10@example.com', 'password10', 1650.00);
```

## item table

```sql
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
```