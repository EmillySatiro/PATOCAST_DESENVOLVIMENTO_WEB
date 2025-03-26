INSERT INTO users (nome, sobrenome, email, senha) 
VALUES 
  ('Jonas', 'Cesar', 'jonasbo66@gmail.com', crypt('jonas123', gen_salt('bf'))),
  ('Maria', 'Oliveira', 'maria.oliveira@example.com', crypt('senha456', gen_salt('bf'))),
  ('Carlos', 'Santos', 'carlos.santos@example.com', crypt('senha789', gen_salt('bf')));

INSERT INTO transactions (idUser, estabelecimento, categoria, valor, data)
VALUES 
  (1, 'Mercado', 'Alimentação', 100.00, '2021-01-01'),
  (1, 'Farmácia', 'Saúde', 50.00, '2021-01-02'),
  (1, 'Posto de gasolina', 'Transporte', 200.00, '2021-01-03'),
  (1, 'Restaurante', 'Alimentação', 150.00, '2021-01-04'),
  (1, 'Cinema', 'Entretenimento', 30.00, '2021-01-05');