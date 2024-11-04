FROM python:3

WORKDIR /pyt

COPY . /pyt

RUN pip install -r requirements.txt

CMD [ "python3", "/pyt/main.py"]