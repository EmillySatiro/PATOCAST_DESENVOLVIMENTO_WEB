all:
	@docker-compose --file 'docker-compose.yml' --project-name 'web-i-tela_home-html' down 
	@docker-compose up --build

backend:
	@python backend/app.py

frontend:
	@cd front && npm install && npm start
