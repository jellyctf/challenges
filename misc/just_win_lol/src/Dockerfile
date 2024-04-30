FROM golang:1.22 AS build
WORKDIR /app
COPY go.mod go.sum /app/
RUN go mod download
COPY *.go /app/
RUN CGO_ENABLED=0 GOOS=linux go build -o /just-win-lol

FROM alpine:latest AS run
WORKDIR /app
RUN adduser -S jelly
USER jelly
COPY --chown=jelly assets /app/assets
COPY --from=build --chown=jelly /just-win-lol /app/
EXPOSE 8080
ENTRYPOINT ["/app/just-win-lol"]