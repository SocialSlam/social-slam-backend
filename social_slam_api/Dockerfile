FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./settings/requirements_dev.txt /code/
RUN pip install -r requirements_dev.txt
COPY . /code/
