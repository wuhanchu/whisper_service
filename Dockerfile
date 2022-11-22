FROM docker.io/bitnami/pytorch:1.13.0
USER root
COPY "./" "./"
RUN chmod 777 run.sh

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list 
RUN apt update 
RUN apt install -y git 
RUN pip3 install  -r ./requirements.txt   -i https://mirrors.aliyun.com/pypi/simple/ --extra-index-url  https://pypi.org/simple/
RUN apt install -y ffmpeg
CMD ./run.sh
