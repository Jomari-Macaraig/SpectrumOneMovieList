SHELL := /bin/bash

.PHONY:
	clean
	build_base
	build_dev
	build_prod
	deploy_prod
	deploy_dev

help:
	@echo "clean - remove artifacts"
	@echo "build_[base|dev|prod] - Builds environment"
	@echo "deploy_[dev|prod] - Deploy environment"

clean:
	find movielist/ -iname "*.pyc" | xargs rm -Rf
	find movielist/ -iname "*.pyo" | xargs rm -Rf
	find movielist/ -iname "*.pyd" | xargs rm -Rf
	find movielist/ -iname "__pycache__" | xargs rm -Rf

build_base:
	make clean

build_dev:
	make build_base
	pip install -r requirements/dev.pip

build_prod:
	make build_base
	pip install -r requirements/dev.pip

deploy_prod:
	make build_prod
	cd movielist
	python3 manage.py collectstatic --no-input
	python3 manage.py migrate --settings=config.settings.prod
	python3 manage.py runserver 0.0.0.0:8000 --settings=config.settings.prod

deploy_dev:
	make build_dev
	cd movielist
	python3 manage.py collectstatic --no-input
	python3 manage.py migrate --settings=config.settings.dev
	python3 manage.py runserver 0.0.0.0:8000 --settings=config.settings.dev
