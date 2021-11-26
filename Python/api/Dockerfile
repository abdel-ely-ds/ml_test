FROM python:3.9
ENV HOME="/home/ws"
WORKDIR $HOME
COPY api/requirements.txt ./Python/api/requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./Python/api/requirements.txt
COPY api/ ./Python/api/
COPY simple_python/ ./Python/simple_python/

CMD ["python", "-m", "Python.api.main"]