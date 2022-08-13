#!/usr/bin/make

mypy:
	@mypy . --explicit-package-bases --namespace-packages --exclude venv

build:
	@docker build -t bancho-service:latest .