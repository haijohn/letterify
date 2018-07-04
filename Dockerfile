FROM python:latest




# use a fast source list in China, comment this if not necessary
COPY sources.list /etc/apt/

# install tesseract4, see https://notesalexp.org/tesseract-ocr/
RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-transport-https wget

RUN echo 'deb https://notesalexp.org/tesseract-ocr/stretch/ stretch main' >> /etc/apt/sources.list

RUN wget -O - https://notesalexp.org/debian/alexp_key.asc | apt-key add -
RUN apt-get update
RUN apt-get install -y --no-install-recommends tesseract-ocr

# install python package
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt -i https://pypi.douban.com/simple/

RUN mkdir /code
WORKDIR /code

EXPOSE 80
EXPOSE 5000