FROM python:3.7

COPY . /code

WORKDIR /code

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./import_list.py"]

