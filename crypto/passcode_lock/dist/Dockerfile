FROM gcc AS build
WORKDIR /app/
COPY passcode_lock.c Makefile /app/
RUN make

FROM debian AS run
RUN apt-get update && apt-get install -y socat
WORKDIR /app/
COPY --from=build /app/passcode_lock /app/
EXPOSE 6000
ENTRYPOINT ["socat", "-dd", "TCP4-LISTEN:6000,fork,reuseaddr", "EXEC:\"/app/passcode_lock\",pty,echo=0,stderr"]
