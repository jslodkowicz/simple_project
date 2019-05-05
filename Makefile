SERVICE_NAME=wea_project

MY_DOCKER_NAME=$(SERVICE_NAME)

.PHONY: test deps

deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt

run:
	PYTHONPATH=. FLASK_APP=weather flask run

test:
	python -m pytest test/test_fun.py

test_cov:
	python -m pytest --verbose -s --cov=weather test/

test_xunit:
	python -m pytest --verbose -s --cov=weather test/ --cov-report xml

test_code_complexity:
	radon cc weather

test_smoke:
	curl --fail 127.0.0.1:5000

docker_build:
	docker build -t $(MY_DOCKER_NAME) .

docker_run: docker_build
	docker run \
		--name $(SERVICE_NAME)_dev \
			-p 5000:5000 \
			-d $(MY_DOCKER_NAME)

docker_stop:
	docker stop $(SERVICE_NAME)_dev

USERNAME=jslodkowicz
TAG=$(USERNAME)/$(MY_DOCKER_NAME)

docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \

	docker tag $(MY_DOCKER_NAME) $(TAG); \
	docker push $(TAG); \
	docker logout;
