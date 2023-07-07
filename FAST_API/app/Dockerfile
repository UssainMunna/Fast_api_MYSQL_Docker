FROM python:3.9
RUN pip3 install fastapi uvicorn
RUN pip install mysql-connector-python
COPY . /app
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400" ]
