FROM python
WORKDIR /docker
COPY . .
CMD ["python", "test.py"]