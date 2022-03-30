FROM python:3.10.4-bullseye
COPY . .
RUN python -m pip install --upgrade pip \
    && python -m pip install -r ./requirements.txt
CMD ["python", "pgtest.py"]
