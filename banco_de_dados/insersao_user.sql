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
(1, '[{"pergunta": 1, "resposta": "1"}, {"pergunta": 2, "resposta": "3"}, {"pergunta": 3, "resposta": 1000}]'),
(2, '[{"pergunta": 1, "resposta": "1"}, {"pergunta": 2, "resposta": "3"}, {"pergunta": 3, "resposta": 1000}]');


INSERT INTO posso_te_ajudar (titulo, descricao)
VALUES 
  ('Economizar', 'Ajuda para economizar dinheiro e gerenciar despesas.'),
  ('Investir', 'Ajuda para investir dinheiro e aumentar patrimônio.'),
  ('Planejar', 'Ajuda para planejar finanças pessoais e alcançar objetivos.'),
  ('Controlar', 'Ajuda para controlar gastos e evitar dívidas.'),
  ('Entender', 'Ajuda para entender conceitos financeiros e investimentos.');

INSERT INTO ajuda_content (idPossoTeAjudar, header_text, modal_cards)
VALUES 
  (1, '[{"title": "Como economizar dinheiro?", "description": "Aprenda estratégias práticas para reduzir gastos no dia a dia e aumentar sua economia de forma consistente."}]', 
      '[{"title": "Dicas de economia", "description": "Descubra hábitos simples para economizar em compras, serviços e lazer."}, {"title": "Planejamento financeiro", "description": "Organize seus ganhos e gastos para alcançar seus objetivos financeiros mais rapidamente."}]'),

  (2, '[{"title": "Como investir dinheiro?", "description": "Entenda as melhores práticas para iniciar no mundo dos investimentos, aumentando seu patrimônio com segurança."}]', 
      '[{"title": "Investimentos seguros", "description": "Conheça opções de investimentos de baixo risco para começar com segurança."}, {"title": "Renda variável", "description": "Aprenda a diversificar seus investimentos e entender o funcionamento do mercado de ações."}]'),

  (3, '[{"title": "Como planejar suas finanças?", "description": "Desenvolva um planejamento financeiro sólido para ter mais controle, segurança e liberdade no futuro."}]', 
      '[{"title": "Orçamento mensal", "description": "Monte um orçamento que equilibre suas necessidades, lazer e investimentos."}, {"title": "Metas financeiras", "description": "Defina metas claras e alcançáveis para transformar seus sonhos em realidade."}]'),

  (4, '[{"title": "Como controlar seus gastos?", "description": "Descubra técnicas para monitorar seus gastos e evitar despesas desnecessárias, mantendo seu orçamento saudável."}]', 
      '[{"title": "Controle de despesas", "description": "Use ferramentas e métodos práticos para registrar e analisar seus gastos diários."}, {"title": "Evitar dívidas", "description": "Implemente estratégias para gastar com consciência e manter sua saúde financeira."}]'),

  (5, '[{"title": "Como entender investimentos?", "description": "Aprenda os conceitos essenciais sobre investimentos e como fazer escolhas inteligentes para o seu dinheiro."}]', 
      '[{"title": "Conceitos financeiros", "description": "Entenda termos como liquidez, rentabilidade e risco para tomar decisões melhores."}, {"title": "Tipos de investimentos", "description": "Explore as características e vantagens de diferentes tipos de aplicações, como renda fixa e variável."}]');
  