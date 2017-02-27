FROM qa.stratio.com/alpine:3.5


RUN apk update && \
    apk add python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install xlsxwriter && \
    rm -r /root/.cache

COPY helloServer.py /

EXPOSE 8080

CMD python3 /helloServer.py && tail -f /var/log/*
