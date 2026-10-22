CREATE TABLE IF NOT EXISTS natural_person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    monthly_income REAL,
    age INTEGER,
    full_name TEXT,
    cellphone_number TEXT,
    email TEXT,
    category TEXT,
    balance REAL,
    cpf TEXT
);

CREATE TABLE IF NOT EXISTS legal_person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    revenue REAL,
    age INTEGER,
    front_name TEXT,
    cellphone_number TEXT,
    corporative_email TEXT,
    category TEXT,
    balance REAL,
    cnpj TEXT
);

INSERT INTO natural_person (monthly_income, age, full_name, cellphone_number, email, category, balance, cpf)
VALUES
(5000.00, 35, 'João da Silva', '9999-8888', 'joao@example.com', 'Categoria A', 10000.00, '555-555-555-55'),
(4000.00, 45, 'Maria Oliveira', '7777-6666', 'maria@example.com', 'Categoria B', 15000.00, '444-444-444-44'),
(6000.00, 28, 'Pedro Santos', '5555-4444', 'pedro@example.com', 'Categoria C', 8000.00, '333-333-333-33');

INSERT INTO legal_person (revenue, age, front_name, cellphone_number, corporative_email, category, balance, cnpj)
VALUES
(100000.00, 10, 'Empresa XYZ', '1111-2222', 'contato@empresa.com', 'Categoria A', 50000.00, '55.555.555/0001-55'),
(80000.00, 5, 'Empresa ABC', '3333-4444', 'contato@abc.com', 'Categoria B', 70000.00, '44.444.444/0001-44'),
(120000.00, 8, 'Empresa 123', '5555-6666', 'contato@123.com', 'Categoria C', 90000.00, '33.33.333/0001-33');