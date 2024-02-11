FROM python:3.9-alpine3.19
WORKDIR /app
COPY . .
RUN pip install -r /app/requirements.txt
EXPOSE 8000
RUN addgroup app && adduser -S -G app app
USER app