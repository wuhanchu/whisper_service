FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

#FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime

USER root

ENV MODEL="base"
ENV TEMP_FOLDER="/var/whipser"

EXPOSE 5000
VOLUME ["/.cache/whisper","/var/whipser"]


COPY "./" "./"
RUN chmod 777 run.sh

RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt update 
RUN apt install -y git 
RUN pip uninstall -y torch
RUN pip install -r requirements.txt  -i https://mirrors.aliyun.com/pypi/simple/
RUN pip cache purge
RUN apt install -y ffmpeg
RUN apt clean
CMD ./run.sh
