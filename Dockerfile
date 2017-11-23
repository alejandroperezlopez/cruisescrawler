FROM python:3.6-onbuild

ENV DATA_PATH /srv/cruisesdb
VOLUME $DATA_PATH

ENTRYPOINT ["python3", "-m", "cruisescrawler"]