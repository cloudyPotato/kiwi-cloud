FROM alpine:3.10 

LABEL maintainer="Katie Gamanji"

RUN apk add --update \
    python \
    python-dev \
    py-pip \
  && rm -rf /var/cache/apk/*

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./app /app

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
