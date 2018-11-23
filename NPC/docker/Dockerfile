FROM python:3.6-slim

SHELL ["/bin/bash", "-c"]

RUN apt-get update -qq && \
  apt-get install -y --no-install-recommends \
  build-essential \
  wget \
  openssh-client \
  graphviz-dev \
  pkg-config \
  git-core \
  openssl \
  libssl-dev \
  libffi6 \
  libffi-dev \
  libpng-dev \
  curl && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
  mkdir /app

  WORKDIR /app 

  COPY requirements.txt .

  RUN pip install -r requirements.txt --no-cache-dir

  COPY . .

  RUN pip install rasa_core==0.12.00

  VOLUME ["/app/data"]

  EXPOSE 5005

  CMD ["python", "socketio_server.py"]

