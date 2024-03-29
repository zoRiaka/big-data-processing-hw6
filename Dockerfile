FROM python:3.9-slim

RUN pip install --upgrade pip
COPY requirements.txt /opt/app/requirements.txt
RUN python3 -m pip install -r /opt/app/requirements.txt

COPY ./main.py /opt/app/main.py
COPY ./sample.csv /opt/app/sample.csv

ENTRYPOINT ["python", "/opt/app/main.py"]
