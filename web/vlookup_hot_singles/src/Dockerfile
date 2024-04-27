FROM python:3.11
RUN groupadd -r jelly && useradd --no-log-init -m -r -g jelly jelly
USER jelly
WORKDIR /app
ENV PATH="/home/jelly/.local/bin:$PATH"

COPY Pipfile Pipfile.lock /app/
RUN pip install --user pipenv && pipenv install --deploy --ignore-pipfile

COPY --chown=jelly:jelly . /app/

EXPOSE 8080
CMD ["pipenv", "run", "python", "vlookup_hot_singles.py"]