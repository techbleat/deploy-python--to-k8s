FROM python:3.11

WORKDIR /code

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["uvicorn","app:app","--host","0.0.0.0","--reload"]
#CMD ["fastapi", "run", "app.py", "--port", "8000" ]
