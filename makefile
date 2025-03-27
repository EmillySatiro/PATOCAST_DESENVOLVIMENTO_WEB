all:
	@docker-compose --file 'docker-compose.yml' --project-name 'web-i-tela_home-html' down 
	@docker-compose up --build

.PHONY: backend

backend:
	@python backend/app.py

front: frontend

frontend:
	@cd front && npm install && npm start
