FROM ubuntu as base

WORKDIR /root/

RUN apt update -y
RUN apt upgrade -y
RUN apt update -y

RUN apt install -y python3 python3-pip socat

COPY dizzy_fishman.py .
COPY flag.txt .
COPY requirements.txt .

RUN pip3 install -r requirements.txt --break-system-packages
EXPOSE 4000

ENTRYPOINT ["socat", "-dd", "TCP4-LISTEN:4000,fork,reuseaddr", "EXEC:\"python3 ./dizzy_fishman.py\",pty,echo=0,stderr"]

