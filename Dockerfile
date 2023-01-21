FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code \
  && mkdir /var/log/jin_prof
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/