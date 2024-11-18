-- Configurações de performance
ALTER SYSTEM
SET max_connections = '100';
ALTER SYSTEM
SET shared_buffers = '256MB';
ALTER SYSTEM
SET work_mem = '16MB';
ALTER SYSTEM
SET maintenance_work_mem = '256MB';
ALTER SYSTEM
SET effective_cache_size = '1GB';
ALTER SYSTEM
SET synchronous_commit = 'off';