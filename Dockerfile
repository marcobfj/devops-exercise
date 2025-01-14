FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirement.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
