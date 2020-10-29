FROM python:latest
WORKDIR /alireza
COPY requirements.txt .
COPY one.py .
RUN pip install -r requirements.txt
CMD python ./one.py