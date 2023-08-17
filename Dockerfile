FROM python:3.9
WORKDIR /ImageHog
COPY ./requirements.txt /ImageHog/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /ImageHog/requirements.txt

COPY ./app /ImageHog/app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

ENV PYTHONPATH="${PYTHONPATH}:/ImageHog"

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]



# FROM python:3.11
# RUN apt-get update && apt-get install -y libgl1-mesa-glx
# WORKDIR /app


# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY app /app

# EXPOSE 8080

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]