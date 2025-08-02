POSTGRES_USER=tg-user
POSTGRES_PASSWORD=password
CONTAINER_NAME=tg-gifts-n-stickers
VOLUME_NAME=tg-gifts-n-stickers-data
POSTGRES_IMAGE=postgres:17-alpine


postgresinit:
	docker volume create $(VOLUME_NAME)
	docker run --name $(CONTAINER_NAME) \
		-e POSTGRES_USER=$(POSTGRES_USER) \
		-e POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) \
		-d -p 5432:5432 \
		-v $(VOLUME_NAME):/var/lib/postgresql/data \
		$(POSTGRES_IMAGE)


postgres:
	docker exec -it $(CONTAINER_NAME) psql --username=$(POSTGRES_USER)

destroy:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true
	docker volume rm $(VOLUME_NAME) || true
	@echo "PostgreSQL container and volume permanently deleted."

remove-container:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true
	@echo "PostgreSQL container $(CONTAINER_NAME) deleted. Data preserved in volume: $(VOLUME_NAME)"

restart:
	$(MAKE) remove-container
	$(MAKE) postgresinit

.PHONY: postgresinit postgres destroy remove-container restart

