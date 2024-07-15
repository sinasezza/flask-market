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