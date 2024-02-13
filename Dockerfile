FROM python:3.9-alpine3.19
RUN addgroup  app -g 1001 && adduser -S -G app app
WORKDIR /app
RUN chown -R app:app /app
USER app
COPY --chown=app:app *requirements.txt .
RUN pip install -r /app/requirements.txt
COPY --chown=app:app . .
EXPOSE 8000
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"] 