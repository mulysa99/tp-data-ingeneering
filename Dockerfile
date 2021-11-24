FROM python 3.6
WORKDIR /code
ENV NODEJS_APP=app2.py
ENV NODEJS_RUN_HOST=0.0.0.0
COPY * ./
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["nodejs","run"
