FROM python:3.12-slim

WORKDIR /code 

RUN apt-get update && apt-get install git -y && apt-get install curl -y

COPY ./requirements.txt ./
COPY ./run.sh ./
RUN chmod +x ./run.sh && ./run.sh

COPY ./src ./src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
