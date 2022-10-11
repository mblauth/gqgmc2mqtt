FROM python:latest
WORKDIR /
COPY main.py ./
RUN pip install --no-cache-dir paho-mqtt pyserial
ENTRYPOINT [ "python", "./main.py" ]
