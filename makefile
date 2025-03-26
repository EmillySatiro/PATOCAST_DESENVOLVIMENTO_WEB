all:
	@docker-compose --file 'docker-compose.yml' --project-name 'web-i-tela_home-html' down 
	@docker-compose up --build

.PHONY: backend

backend:
	@C:/Users/jonas/anaconda3/python.exe "c:/Users/jonas/Documents/Codigos Curso/WEB/WEB-I-TELA_HOME-HTML/backend/app.py"

front: frontend

frontend:
	@cd front && npm start
