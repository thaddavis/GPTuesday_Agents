FROM python:3.10
RUN mkdir /app 
COPY . /app
COPY pyproject.toml /app 
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip install poetry==1.7.1
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
EXPOSE 8080

ENV PORT 8080

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0", "-p", "8080"]
