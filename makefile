all:
	@docker-compose --file 'docker-compose.yml' --project-name 'web-i-tela_home-html' down 
	@docker-compose up --build

.PHONY: backend

backend:
	@docker-compose up -d postgres
	@pip install -r backend/requirements.txt
	@python backend/app.py

front: frontend

frontend:
	@cd front && npm install && npm start