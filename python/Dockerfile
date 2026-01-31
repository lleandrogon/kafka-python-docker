FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    kafka-python \
    jupyter

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]