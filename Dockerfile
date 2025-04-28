FROM python:3.10.14-bookworm
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y poppler-utils
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev ffmpeg mediainfo
RUN pip3 install -r requirements.txt
RUN apt-get install ffmpeg
RUN apt-get update
RUN apt-get install -y libssl-dev aria2 ffmpeg curl unzip
COPY . .
CMD ["python3", "main.py"]