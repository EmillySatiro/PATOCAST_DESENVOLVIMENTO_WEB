INSERT INTO users (nome, sobrenome, email, senha) 
VALUES 
  ('Jonas', 'Cesar', 'jonasbo66@gmail.com', crypt('jonas123', gen_salt('bf'))),
  ('Kaua', 'Henrique', 'kaua.sbc@gmail.com', crypt('kaua123', gen_salt('bf')));

INSERT INTO transactions (idUser, estabelecimento, categoria, valor, data)
VALUES 
  (1, 'Mercado', 'Alimentação', 100.00, '2025-01-01'),
  (1, 'Farmácia', 'Saúde', 50.00, '2025-01-02'),
  (1, 'Posto de gasolina', 'Transporte', 200.00, '2025-01-03'),
  (1, 'Restaurante', 'Alimentação', 150.00, '2025-01-04'),
  (1, 'Cinema', 'Entretenimento', 30.00, '2025-01-05'),
  (1, 'Cinema', 'Entretenimento', 30.00, '2025-02-05'),
  (1, 'Restaurante', 'Alimentação', 150.00, '2025-02-04'),
  (1, 'Posto de gasolina', 'Transporte', 200.00, '2025-02-03'),
  (1, 'Posto de gasolina', 'Transporte', 200.00, '2025-02-03'),
  (1, 'Posto de gasolina', 'Transporte', 400.00, '2025-04-03'),
  (1, 'Posto de gasolina', 'Transporte', 400.00, '2025-04-03'),
  (1, 'Posto de gasolina', 'Transporte', 400.00, '2025-02-28'),
  (1, 'Posto de gasolina', 'Transporte', 400.00, '2025-03-1');
  
  INSERT INTO cartao (idUser, numero, nome, meta, tipo)
  VALUES
    (1, 12312312312, 'Jonas G P Sousa', 1000.00,'Crédito'),
    (1, 12312312312, 'Jonas G P Sousa', 1000.00,'Débito'),
    (2, 11111111111, 'Kaua H S Almeida', 1000.00,'Crédito'),
    (2, 11111111111, 'Kaua H S Almeida', 1000.00,'Débito');

INSERT INTO perguntas (idUser, resposta) VALUES 
  (1, '{"pergunta1": "resposta1", "pergunta2": "resposta2"}'),
  (2, '{"pergunta1": "resposta1", "pergunta2": "resposta2"}');