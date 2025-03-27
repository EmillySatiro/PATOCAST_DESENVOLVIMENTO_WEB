INSERT INTO users (nome, sobrenome, email, senha, limite) 
VALUES 
  ('Jonas', 'Cesar', 'jonasbo66@gmail.com', crypt('jonas123', gen_salt('bf')), 1000.00),
  ('Maria', 'Silva', 'maria.silva@gmail.com', crypt('maria123', gen_salt('bf')), 1500.00),
  ('Carlos', 'Oliveira', 'carlos.oliveira@gmail.com', crypt('carlos123', gen_salt('bf')), 2000.00),
  ('Ana', 'Souza', 'ana.souza@gmail.com', crypt('ana123', gen_salt('bf')), 1200.00);

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
  