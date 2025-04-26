-- \c patocash  -- Conecta ao banco de dados 'patocash'

CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Criação da tabela 'users'
CREATE TABLE IF NOT EXISTS users (
  idUser SERIAL PRIMARY KEY,  -- Auto incremento
  nome VARCHAR(255) NOT NULL,
  sobrenome VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  senha TEXT NOT NULL,
  criado TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  -- Data e hora de criação
  atualizado TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP  -- Data e hora da última atualização
);

-- Criação da tabela 'transactions'
CREATE TABLE IF NOT EXISTS transactions (
  idTransaction SERIAL PRIMARY KEY,  -- Auto incremento
  idUser INT NOT NULL,
  estabelecimento VARCHAR(255) NOT NULL,
  categoria VARCHAR(255) NOT NULL,
  valor DECIMAL(10, 2) NOT NULL,
  data DATE NOT NULL,
  CONSTRAINT fk_user FOREIGN KEY (idUser) REFERENCES users (idUser) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Criação da tabela 'cartao'
CREATE TABLE IF NOT EXISTS cartao (
  idCartao SERIAL PRIMARY KEY,  -- Auto incremento
  idUser INT NOT NULL,
  numero VARCHAR(255) NOT NULL,
  nome VARCHAR(255) NOT NULL,
  meta DECIMAL(10, 2) NOT NULL,
  tipo VARCHAR(255) NOT NULL,
  CONSTRAINT fk_cartao_user FOREIGN KEY (idUser) REFERENCES users (idUser) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Criação da tabela 'perguntas'
CREATE TABLE IF NOT EXISTS perguntas (
  resposta JSONB NOT NULL,
  idUser INT NOT NULL PRIMARY KEY,
  CONSTRAINT fk_pergunta_user FOREIGN KEY (idUser) REFERENCES users (idUser) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Criação da tabela 'posso_te_ajudar'
CREATE TABLE IF NOT EXISTS posso_te_ajudar (
  idPossoTeAjudar SERIAL PRIMARY KEY,  -- Auto incremento
  titulo VARCHAR(255) NOT NULL,
  descricao TEXT NOT NULL
);

-- Criação da tabela 'ajuda_content'
CREATE TABLE IF NOT EXISTS ajuda_content (
  idAjudaContent SERIAL PRIMARY KEY,  -- Auto incremento
  idPossoTeAjudar INT NOT NULL,
  header_text JSONB NOT NULL,
  modal_cards JSONB NOT NULL,
  CONSTRAINT fk_ajuda_content_posso_te_ajudar FOREIGN KEY (idPossoTeAjudar) REFERENCES posso_te_ajudar (idPossoTeAjudar) ON DELETE CASCADE ON UPDATE CASCADE
);