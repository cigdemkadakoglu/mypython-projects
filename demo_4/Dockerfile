FROM python:3.8 as baseimage
WORKDIR /app
COPY * .
RUN pip install --user -r requirements.txt


FROM python:3.8-slim as buildimage
RUN adduser python
USER python
WORKDIR /app
COPY --from=baseimage /app/ ./
COPY --from=baseimage /root/.cache /home/python/.cache
RUN pip install -r requirements.txt
CMD ["python", "myapp.py"]