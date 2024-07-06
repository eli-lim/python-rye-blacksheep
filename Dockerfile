FROM python:slim

WORKDIR /app
COPY .python-version ./
COPY pyproject.toml ./
COPY requirements.lock ./

# FIXME: Failing step
RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -r requirements.lock

COPY src .
CMD python main.py
