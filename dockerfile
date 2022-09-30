FROM python:3

WORKDIR /usr/src/warehouse

COPY req.txt ./
RUN pip install --no-cache-dir -r req.txt

COPY app/ .

CMD flask run -h 0.0.0.0 -p 9000
