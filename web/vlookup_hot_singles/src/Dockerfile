FROM python:3.11
RUN groupadd -r jelly && useradd --no-log-init -r -d /app -M -g jelly jelly
USER jelly
WORKDIR /app
ENV PATH="/app/.local/bin:$PATH"

COPY Pipfile Pipfile.lock /app/
RUN pip install --user pipenv && pipenv install --deploy --ignore-pipfile

COPY --chown=jelly:jelly . /app/

CMD ["pipenv", "run", "python", "vlookup_hot_singles.py"]