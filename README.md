# Hello World Host

This project is an example of a microservice built with spring boot and all it needs to be to be deployed in Marathon as HOST mode.
The `marathon.json` can be used for deploy it in Marathon.

## Instructions 

- clean the project
`mvn clean` 

- create the jar
`mvn package` 

- build your docker image
`mvn docker:build` 

- build and push image to the registry
`mvn docker:build -DpushImage`

More info of how to use `docker-maven-plugin`: https://github.com/spotify/docker-maven-plugin 

## Run it locally
`docker run -it --rm -e PORT0=1234 -p 80:1234 bootstrap-sec.labs.stratio.com:5000/hello-world-host:1.0-SNAPSHOT`

Open your browswer: `localhost:80` and you should see `Hello World Host!`

## Test it locally

- Pre-reqs:
    python3
    EOS master can be resolved by hostname

- Runing:
    `python test.py yourmaster user paassword`
    `python test.py master-1.node.paas.labs.stratio.com admin 1234`
