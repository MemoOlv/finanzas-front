FROM python:3

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install \
    black \
    flake8 \
    mypy \
    pylint \
    pytest \
    pytest-cov \
    uvicorn

RUN make install

CMD ["uvicorn", "finance_module.main:app", "--host", "0.0.0.0", "--port", "8000"]
