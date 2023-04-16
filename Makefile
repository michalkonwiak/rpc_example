run-all:
	docker compose -f RabbitMQ/docker-compose.yml up -d
	docker compose -f OneApp/docker-compose.yml up -d
	docker compose -f SecondApp/docker-compose.yml up -d

restart-all:
	docker compose -f RabbitMQ/docker-compose.yml restart
	docker compose -f OneApp/docker-compose.yml restart
	docker compose -f SecondApp/docker-compose.yml restart

stop-all:
	docker compose -f RabbitMQ/docker-compose.yml stop
	docker compose -f OneApp/docker-compose.yml stop
	docker compose -f SecondApp/docker-compose.yml stop
