FROM python:3.7.9-alpine

ARG PORT=80
ENV PORT=$PORT

ARG HOST=0.0.0.0
ENV HOST=$HOST

ARG FLASK_APP=/app/run.py
ENV FLASK_APP=$FLASK_APP

ARG FLASK_ENV=development
ENV FLASK_ENV=$FLASK_ENV

ENV PYTHONUNBUFFERED=True

WORKDIR /app
COPY . /app

RUN apk add \
    curl

# Create user & group; exec:exec and dev:dev
RUN sed -i '/999/d;' /etc/group && \
    addgroup -S -g 999 exec && adduser -u 999 -s /sbin/nologin -SDHG exec exec && \
    adduser -DH dev && adduser exec dev

# Fixed permissions
RUN chown -R exec:dev \
    /app \
    /usr/local/bin/ \
    /usr/local/lib/python3.7/

# Read only file system
RUN chmod -R a-w \
    /etc \
    /var

VOLUME /app
EXPOSE ${PORT}

HEALTHCHECK CMD curl -f http://${HOST}:${PORT}/ || exit 1

USER exec:dev

ENTRYPOINT ["/app/scripts/startup.sh"]
