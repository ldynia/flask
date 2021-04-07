# Description

Plain flask init project.

# Build

```bash
$ git clone git@github.com:ldynia/flask.git
$ cd flask/
$ docker build --tag flask-demo:latest --file docker/Dockerfile app/
$ docker-compose up
```

# Run

```bash
$ docker run -d --rm --name flask-demo flask-demo:latest
$ watch -n1 docker ps
```

# Debug
```bash
$ docker logs -f flask-demo
```