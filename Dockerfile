FROM alpine:latest

RUN apk update && apk add py-pip && apk add python3 && apk add --no-cache python3 py3-pip

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

EXPOSE 5000

CMD ["python3","/app/Flask.py"]



