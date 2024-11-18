CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";
-- Configurações de locale
ALTER SYSTEM
SET client_encoding = 'UTF8';
ALTER SYSTEM
SET default_text_search_config = 'pg_catalog.portuguese';