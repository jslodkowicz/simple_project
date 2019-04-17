FROM python:3.6

ARG APP_DIR=/usr/src/wea_project

WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p $APP_DIR
ADD weather/ $APP_DIR/weather
ADD main.py $APP_DIR

CMD PYTHONPATH=$PYTHONPATH:/usr/src/wea_project \
    FLASK_APP=weather flask run --host=0.0.0.0
