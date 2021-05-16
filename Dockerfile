FROM ubuntu:latest

MAINTAINER whatwant "whatwant@whatwant.com"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-dev build-essential

RUN ln -s /usr/bin/python3 /usr/bin/python
RUN rm /usr/bin/pip
RUN ln -s /usr/bin/pip3 /usr/bin/pip

RUN pip install --upgrade pip

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]
