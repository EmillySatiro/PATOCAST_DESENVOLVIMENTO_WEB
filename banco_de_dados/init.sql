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
  CONSTRAINT fk_cartao_user FOREIGN KEY (idUser) REFERENCES users (idUser) ON DELETE CASCADE ON UPDATE CASCADE
);

