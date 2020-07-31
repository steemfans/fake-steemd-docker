FROM alpine:3.9
WORKDIR /usr/local/bin
RUN apk --no-cache add python3
ADD steemd.py /usr/local/bin/steemd
ADD steem /steem
ENV BASE_STEEM_PATH=/steem
CMD ["/usr/local/bin/steemd"]
