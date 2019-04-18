.PHONY: test

deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt

lint:
	flake8 weather test

run:
	PYTHONPATH=. FLASK_APP=weather flask run

test:
	python3 -m pytest test/test_fun.py

test_smoke:
	curl --fail 127.0.0.1:5000

docker_build:
	docker build -t wea_project .

docker_run: docker_build
	docker run \
		--name wea_project_dev \
			-p 5000:5000 \
			-d wea_project

USERNAME=jslodkowicz
TAG=$(USERNAME)/wea_project

docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
	docker tag wea_project $(TAG); \
	docker push $(TAG); \
	docker logout;
