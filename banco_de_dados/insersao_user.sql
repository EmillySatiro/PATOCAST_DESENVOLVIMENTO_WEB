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

INSERT INTO perguntas (idUser, pergunta, respostas)
VALUES
  (1, 'Qual seu objetivo?', '[{"id": 1, "resposta": "Se organizar"}, {"id": 2, "resposta": "Economizar"}, {"id": 3, "resposta": "Receber dicas financeiras"}]'),
  (1, 'Você é?', '[{"id": 1, "resposta": "Aposentado"}, {"id": 2, "resposta": "Estudante"}, {"id": 3, "resposta": "CLT"}, {"id": 4, "resposta": "Pessoa Jurídica"}, {"id": 5, "resposta": "CLT (Negativado)"}, {"id": 6, "resposta": "Apenas Negativado"}]'),
  (1, 'Qual sua renda mensal?', '[{"id": 1, "resposta": "R$ 0,00"}]');

INSERT INTO respostas (idUser, resposta) VALUES 
(1, '[{"pergunta": 1, "resposta": "2"}, {"pergunta": 2, "resposta": "2"}, {"pergunta": 3, "resposta": 1111}]'),
(2, '[{"pergunta": 1, "resposta": "2"}, {"pergunta": 2, "resposta": "2"}, {"pergunta": 3, "resposta": 1111}]');

INSERT INTO posso_te_ajudar (titulo, descricao)
VALUES 
  ('Economizar', 'Ajuda para economizar dinheiro e gerenciar despesas.'),
  ('Investir', 'Ajuda para investir dinheiro e aumentar patrimônio.'),
  ('Planejar', 'Ajuda para planejar finanças pessoais e alcançar objetivos.'),
  ('Controlar', 'Ajuda para controlar gastos e evitar dívidas.'),
  ('Entender', 'Ajuda para entender conceitos financeiros e investimentos.'),
  ('Sair das dívidas', 'Ajuda para renegociar dívidas, limpar o nome e recomeçar financeiramente.'),
  ('Construir reserva de emergência', 'Ajuda para formar uma reserva financeira para imprevistos.'),
  ('Planejamento de aposentadoria', 'Ajuda para organizar a aposentadoria e ter uma vida financeira tranquila no futuro.'),
  ('Educação financeira básica', 'Conceitos financeiros fundamentais para iniciantes.'),
  ('Empreender', 'Ajuda para organizar finanças de um negócio próprio.');

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
      '[{"title": "Conceitos financeiros", "description": "Entenda termos como liquidez, rentabilidade e risco para tomar decisões melhores."}, {"title": "Tipos de investimentos", "description": "Explore as características e vantagens de diferentes tipos de aplicações, como renda fixa e variável."}]'),
  (6, '[{"title": "Como sair das dívidas?", "description": "Estratégias práticas para renegociar, quitar dívidas e recuperar seu crédito."}]',
      '[{"title": "Renegociação de dívidas", "description": "Como negociar melhores condições de pagamento."}, {"title": "Limpar seu nome", "description": "Dicas para limpar seu nome nos serviços de proteção ao crédito."}]'),

  (7, '[{"title": "Como construir uma reserva de emergência?", "description": "Passos para formar um fundo financeiro para imprevistos sem comprometer seu orçamento."}]',
      '[{"title": "Reserva de emergência", "description": "Quanto guardar, onde aplicar e como usar."}, {"title": "Disciplina financeira", "description": "Crie hábitos consistentes para formar sua reserva."}]'),

  (8, '[{"title": "Como planejar a aposentadoria?", "description": "Técnicas de organização e investimento para ter uma aposentadoria segura e confortável."}]',
      '[{"title": "Previdência privada e pública", "description": "Entenda as opções para garantir sua renda no futuro."}, {"title": "Quanto preciso guardar?", "description": "Calcule o valor necessário para se aposentar tranquilo."}]'),

  (9, '[{"title": "Aprender educação financeira", "description": "Noções básicas de finanças para tomar melhores decisões no dia a dia."}]',
      '[{"title": "Conceitos básicos", "description": "Orçamento, juros, investimentos e endividamento explicados de forma simples."}, {"title": "Erros comuns", "description": "Principais armadilhas financeiras e como evitá-las."}]'),

  (10, '[{"title": "Como empreender com sucesso?", "description": "Dicas financeiras essenciais para pequenos negócios e MEIs."}]',
       '[{"title": "Gestão financeira para negócios", "description": "Como organizar as finanças da sua empresa."}, {"title": "Separar finanças pessoais e empresariais", "description": "Evite misturar dinheiro do negócio com gastos pessoais."}]');

WITH perfil AS (
  SELECT
    idUser,
    CASE
      WHEN (resposta->0->>'resposta') = '1' THEN 3 -- Planejar
      WHEN (resposta->0->>'resposta') = '2' THEN 1 -- Economizar
      WHEN (resposta->0->>'resposta') = '3' THEN 5 -- Entender
    END AS objetivo,
    
    CASE
      WHEN (resposta->1->>'resposta') = '1' THEN 8 -- Planejamento de aposentadoria (aposentado)
      WHEN (resposta->1->>'resposta') = '2' THEN 9 -- Educação financeira básica (estudante)
      WHEN (resposta->1->>'resposta') = '4' THEN 10 -- Empreender (PJ)
      WHEN (resposta->1->>'resposta') IN ('5', '6') THEN 6 -- Sair das dívidas (negativado)
      ELSE NULL
    END AS perfil,

    CASE
      WHEN (resposta->2->>'resposta')::numeric < 2000 THEN 1 -- Economizar (baixa renda)
      WHEN (resposta->2->>'resposta')::numeric BETWEEN 2000 AND 6000 THEN 7 -- Construir reserva de emergência
      WHEN (resposta->2->>'resposta')::numeric > 6000 THEN 2 -- Investir (alta renda)
      ELSE NULL
    END AS renda
  FROM respostas
  WHERE idUser = 6
)
SELECT DISTINCT ac.idpossoteajudar
FROM perfil p
JOIN posso_te_ajudar pa ON pa.idpossoteajudar IN (p.objetivo, p.perfil, p.renda)
JOIN ajuda_content ac ON ac.idPossoTeAjudar = pa.idpossoteajudar;