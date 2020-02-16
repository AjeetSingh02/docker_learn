FROM continuumio/anaconda
COPY . /app
RUN pip install flask
RUN pip install logging
CMD python /app/main.py