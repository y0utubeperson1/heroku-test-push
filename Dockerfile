FROM heroku/heroku:20
ENV STACK heroku-20

COPY ./bin /tmp/bin
RUN chmod -R +x /tmp/bin

RUN /tmp/bin/compile
CMD [ "/tmp/bin/compile/detect" ]