FROM h3poteto/sbt:0.13.16

USER root

ENV APPROOT /var/opt/app/grpc_example

ADD . ${APPROOT}

WORKDIR ${APPROOT}
RUN chown scala:scala -R ${APPROOT}

ENV SERVER_PORT 9090

EXPOSE 9090

USER scala

WORKDIR ${APPROOT}/server/scala

RUN set -x \
    && cat /dev/null | sbt "compile" \
    && cat /dev/null | sbt "assembly"


CMD java -jar target/scala-2.12/grpcScalasample-assembly-1.0.jar
