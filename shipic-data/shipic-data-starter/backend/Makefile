.PHONY: dev db-up db-down fmt lint

dev:
	uvicorn app.main:app --reload

db-up:
	docker compose up -d

db-down:
	docker compose down

fmt:
	python -m black app || true

lint:
	python -m pip install ruff || true && ruff check app
