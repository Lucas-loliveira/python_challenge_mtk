build up:
	docker-compose up --build -d

create data:
	docker-compose exec app bash -c "python src/scripts/create_tc_data.py "

up:
	docker-compose up -d

down:
	docker-compose down 