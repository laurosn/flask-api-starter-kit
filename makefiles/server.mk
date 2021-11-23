### SERVER
# ¯¯¯¯¯¯¯¯¯¯¯

server.install: ## Install server with its dependencies
#	docker-compose run --rm server pip install --proxy=http://10.1.0.106 -r requirements-dev.txt --user --upgrade --no-warn-script-location
	docker-compose build server
	docker-compose build nginx

server.start: ## Start server in its docker container
	docker-compose up --build --force-recreate server nginx
#	docker-compose up nginx

server.bash: ## Connect to server to lauch commands
	docker-compose exec server bash

server.daemon: ## Start daemon server in its docker container
	docker-compose up -d server
	docker-compose up -d nginx


server.stop: ## Start server in its docker container
	docker-compose stop

server.logs: ## Display server logs
	tail -f server.log

server.upgrade: ## Upgrade pip dependencies
	docker-compose run --rm server bash -c "python vendor/bin/pip-upgrade requirements.txt requirements-dev.txt --skip-virtualenv-check"
