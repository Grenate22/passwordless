FROM python:3.9-alpine3.19
RUN addgroup app && adduser -S -G app app
USER app
WORKDIR /app
COPY *requirements.txt .
RUN pip install -r /app/requirements.txt
COPY . .
EXPOSE 8000
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]