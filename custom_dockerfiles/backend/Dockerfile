FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY index.html .
COPY for_excalidraw ./for_excalidraw
COPY requirements.txt ./for_excalidraw
WORKDIR /for_excalidraw
#ENV DJANGO_ALLOWED_HOSTS=backend
#RUN echo "$DJANGO_ALLOWED_HOSTS"
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
