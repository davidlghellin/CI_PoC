FROM bootstrap-sec.labs.stratio.com:5000/java-ms-dockerbase:v1

VOLUME /tmp

ADD *.jar app.jar

RUN touch /data/app.jar && \
    adduser -D -u 1000 user && \
    chown -R user /data
USER user

ENV JAVA_OPTS=""
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar /data/app.jar --server.port=$PORT0 " ]
