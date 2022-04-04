FROM python:3.8

RUN mkdir /immo_api

WORKDIR /immo_api

COPY . /immo_api

RUN pip install -r requirements.txt

CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0"]

#docker run -p 8000:8000 -v ${PWD}:/immo_api -it immo-api bash