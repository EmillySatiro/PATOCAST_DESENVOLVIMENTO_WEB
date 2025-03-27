INSERT INTO users (nome, sobrenome, email, senha, limite) 
VALUES 
  ('Jonas', 'Cesar', 'jonasbo66@gmail.com', crypt('jonas123', gen_salt('bf')), 1000.00),
  ('Kaua', 'Henrique', 'kaua.sbc@gmail.com', crypt('kaua123', gen_salt('bf')), 1000.00);

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
  (1, 'Posto de gasolina', 'Transporte', 400.00, '2025-04-03');
  

  INSERT INTO cartao (idUser, numero, nome, meta)
  VALUES
    (1, 12312312312, 'Cartão de Crédito', 1000.00),
    (1, 12312312313, 'Cartão de Crédito', 1000.00),
    (1, 12312312314, 'Cartão de Crédito', 1000.00),
    (1, 12312312315, 'Cartão de Crédito', 1000.00);