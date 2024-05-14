FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt  .
RUN pip install -r requirements.txt


COPY . .

RUN chmod +x run.sh

EXPOSE 9612

CMD ./run.sh