FROM python:3.8
RUN useradd -m python
USER python
WORKDIR /home/python
COPY * .
RUN pip install -r requirements.txt
CMD ["python", "myapp.py"]