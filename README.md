# Flask microservices with Traefik example
Deploy [Flask](https://github.com/pallets/flask) microservices with [Traefik](https://github.com/containous/traefik) as reverse proxy and load balancer.

### How to run
You need to install **docker** and **docker-compose** first.

#### Clone this repository
```bash
git clone https://github.com/goldenrati0/flask-with-traefik-example.git
```

#### Change working directory
```bash
cd flask-with-traefik-example/
```

#### Deploy using docker
```bash
docker-compose up -d
```

### Test
Test with curl to verify microservices are running

##### User Service
```bash
curl -H "Host:user.localhost" http://localhost/hello
```
You should receive a response like
```json
{"msg":"Hello from User Service"}
```

##### Payment Service
```bash
curl -H "Host:payment.localhost" http://localhost/hello
```
You should receive a response like
```json
{"msg":"Hello from Payment Service"}
```

You can browse [http://localhost:8080/](http://localhost:8080/) to view the Traefik dashboard.
