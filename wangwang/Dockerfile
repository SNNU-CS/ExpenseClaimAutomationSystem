FROM python:3.6
LABEL maintainer="zhaoqi99@outlook.com"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-client gettext \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/wangwang
WORKDIR /usr/src/wangwang
COPY requirements.txt  /usr/src/wangwang
RUN pip install -r requirements.txt
RUN rm -rf /usr/src/wangwang
COPY . /usr/src/wangwang
ENV ENV=pro
RUN python manage.py collectstatic
RUN python manage.py compilemessages
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]