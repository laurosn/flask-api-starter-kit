### DATABASE
# ¯¯¯¯¯¯¯¯


database.connect: ## Connect to database
	docker-compose exec db psql -Upostgres

database.stamp: ## Create alembic migration file
	docker-compose run --rm server python src/server/manage.py db stamp head

database.migrate: ## Create alembic migration file
	docker-compose run --rm server python src/server/manage.py db migrate

database.upgrade: ## Upgrade to latest migration
	docker-compose run --rm server python src/server/manage.py db upgrade

database.downgrade: ## Downgrade latest migration
	docker-compose run --rm server python src/server/manage.py db downgrade

database.all: database.stamp database.migrate database.upgrade
