FROM python:3.11
RUN groupadd -r jelly && useradd --no-log-init -m -r -g jelly jelly
USER jelly
WORKDIR /app
ENV PATH="/home/jelly/.local/bin:$PATH"

COPY Pipfile Pipfile.lock /app/
RUN pip install --user pipenv && pipenv install --deploy --ignore-pipfile

COPY --chown=nobody:nobody --chmod=555 . /app/

EXPOSE 8081
CMD ["pipenv", "run", "python", "bros_site.py"]