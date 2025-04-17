
FROM python:3.8.10-slim

RUN useradd -m nonrootuser
USER nonrootuser

WORKDIR /app

COPY --chown=nonrootuser:nonrootuser requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=nonrootuser:nonrootuser . /app/

EXPOSE 5000

ENV FLASK_APP=simple_time_service.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["python","-m","flask","run"]


