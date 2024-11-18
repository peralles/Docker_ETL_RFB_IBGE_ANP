# Use a imagem base Python slim
FROM python:3.11.4-slim

# Define argumentos e variáveis de ambiente em um único layer
ARG DEBIAN_FRONTEND=noninteractive
ARG JAVA_VERSION=default-jre
ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    TZ=America/Sao_Paulo \
    PYTHONDONTWRITEBYTECODE=1 \
    # Configurações pip
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Instala dependências do sistema e limpa cache em um único layer
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    ${JAVA_VERSION} \
    postgresql-server-dev-all \
    gcc \
    build-essential \
    libpq-dev \
    # Dependências científicas necessárias
    libblas-dev \
    liblapack-dev \
    # Dependências de processamento
    ghostscript \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Cria diretório de trabalho
WORKDIR /app

# Cria estrutura de diretórios depois do WORKDIR
RUN mkdir -p /app/files/dados_rfb/{\
    OUTPUT_FILES,\
    EXTRACTED_FILES,\
    EXTRACTED_FILES_CONVERT,\
    OUTPUT_ERROS\
    } && \
    mkdir -p /app/files/dados_ibge/{\
    OUTPUT_FILES,\
    OUTPUT_ERROS\
    } && \
    mkdir -p /app/files/dados_anp/{\
    OUTPUT_FILES,\
    OUTPUT_ERROS\
    } && \
    mkdir -p /app/files/dados_rais/{\
    OUTPUT_FILES,\
    EXTRACTED_FILES,\
    EXTRACTED_FILES_CONVERT,\
    OUTPUT_ERROS\
    } && \
    mkdir -p /app/files/dados_sgi/{\
    OUTPUT_FILES,\
    OUTPUT_FILES_CONVERT,\
    OUTPUT_ERROS\
    } && \
    mkdir -p /app/files/dados_ft/{\
    OUTPUT_FILES,\
    OUTPUT_FILES_CONVERT,\
    OUTPUT_ERROS\
    } && \
    mkdir -p /app/files/dados_var_estruturantes/{\
    OUTPUT_FILES,\
    OUTPUT_FILES_CONVERT,\
    OUTPUT_ERROS\
    }

# Copia requirements e instala dependências Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Cria diretório src e copia o código fonte
RUN mkdir -p /app/src
COPY ./src/* /app/src/

# Define permissões
RUN chmod -R 755 /app && \
    chmod -R 777 /app/files

# Healthcheck mais robusto
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME || exit 1

# Comando para executar a aplicação
CMD ["python", "/app/src/A_Main.py"]