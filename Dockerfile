FROM python:3.7
WORKDIR /usr/src/app
COPY . .
ENTRYPOINT ["python3", "stock_analyzer.py"]
