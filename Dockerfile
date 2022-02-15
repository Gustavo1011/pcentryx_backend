FROM python:3.7.4
LABEL maintainer "Herbert Arias <herbert.arsilva@gmail.com>"

RUN apt-get update

# Install GraphViz
RUN apt-get install -y --no-install-recommends graphviz \
  && apt-get install -y --no-install-recommends graphviz-dev \
  && rm -rf /var/lib/apt/lists/*
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=app
ENV FLASK_ENV=development

CMD ["python", "main.py"]
