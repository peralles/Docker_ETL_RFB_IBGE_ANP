CREATE USER postgres WITH PASSWORD 'Peralles@521452';
CREATE DATABASE $ { DB_NAME };
GRANT ALL PRIVILEGES ON DATABASE $ { DB_NAME } TO postgres;