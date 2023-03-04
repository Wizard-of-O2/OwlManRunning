FROM python:3.11-slim
RUN mkdir /root/omr_worker
WORKDIR /root/omr_worker
ADD . .

RUN python -m pip install pika pymongo && python -m pip install -r omr_reader/requirements.txt
RUN apt-get update && apt-get -y install libgl1-mesa-glx libglib2.0-0 poppler-utils

ENV UPLOAD_PATH=.
ENV MONGODB_URL=mongodb://root:rootpassw0rd@mongo/test?authSource=admin
ENV AMQP_HOST=rabbitmq
CMD python worker.py