from ubuntu as base

WORKDIR /root/

RUN apt update -y
RUN apt upgrade -y
RUN apt update -y

RUN apt install -y socat

WORKDIR "/root/"

COPY main .
COPY flag.txt .

EXPOSE 5002

ENTRYPOINT ["socat", "-dd", "TCP4-LISTEN:5002,fork,reuseaddr", "EXEC:./main,pty,echo=0,raw,iexten=0"]
