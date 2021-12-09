FROM python:3.8

WORKDIR /app
COPY . .

RUN pip install -r packages.txt

EXPOSE 5000
CMD ["python3", "main.py"]
