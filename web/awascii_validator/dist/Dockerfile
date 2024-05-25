FROM python:3.7-slim
COPY --chmod=555 . /app
WORKDIR /app
EXPOSE 8080
RUN pip3 install -r requirements.txt
CMD ["python3", "./main.py"]

