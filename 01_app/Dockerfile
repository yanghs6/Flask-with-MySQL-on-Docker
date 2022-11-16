FROM python:3.9-alpine

# WORKDIR /code
COPY . /home/flask/app
WORKDIR /home/flask/app

RUN apk --update --upgrade add --no-cache  gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000

CMD [ "python", "app.py" ]
