FROM python:3.8

WORKDIR /app
COPY . .

RUN pip install -r packages.txt

ENTRYPOINT ["python3", "main.py"]
