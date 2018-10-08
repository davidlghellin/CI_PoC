FROM bootstrap-sec.labs.stratio.com:5000/java-ms-dockerbase:v1

ADD target/hello-world-host-2.0-SNAPSHOT.jar app.jar

RUN touch /data/app.jar && \
    adduser -D -u 1000 user && \
    chown -R user /data && \
    echo "hellouda!"
USER user

ENV JAVA_OPTS=""
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar /data/app.jar --server.port=$PORT0 " ]
