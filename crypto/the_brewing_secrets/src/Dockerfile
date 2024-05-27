FROM gcc AS build
WORKDIR /app/
COPY the_brewing_secrets.c Makefile /app/
RUN make

FROM debian AS run
RUN apt-get update && apt-get install -y socat
WORKDIR /app/
COPY flag.txt /app/
COPY --from=build /app/the_brewing_secrets /app/
EXPOSE 6000
ENTRYPOINT ["socat", "-dd", "TCP4-LISTEN:6000,fork,reuseaddr", "EXEC:\"/app/the_brewing_secrets\",pty,echo=0,stderr"]
