FROM python:3.9
ENV DATABASE_URL=your_database_url_here
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]