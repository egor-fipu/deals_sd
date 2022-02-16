FROM python:3.7-slim

RUN mkdir /deals

RUN pip install --upgrade pip

COPY requirements.txt /deals
RUN pip3 install -r /deals/requirements.txt --no-cache-dir

COPY . /deals
WORKDIR /deals

COPY ./entrypoint.sh /deals
RUN chmod 755 entrypoint.sh
ENTRYPOINT ["/deals/entrypoint.sh"]