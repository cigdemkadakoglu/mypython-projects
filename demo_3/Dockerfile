FROM python:3.8 as baseimage
WORKDIR /app
COPY * .
RUN pip install --user -r requirements.txt


FROM python:3.8-slim as buildimage
WORKDIR /app
COPY --from=baseimage /app/ ./
COPY --from=baseimage /root/.cache /root/.cache
RUN pip install -r requirements.txt
CMD ["python", "myapp.py"]