#!/usr/bin/env python
# coding: utf-8

# In[1]:


from kafka import KafkaProducer as kp
import random

produtor = kp(
    bootstrap_servers = "kafka:9092"
)


# In[2]:


for x in range(10):
    n = random.random()
    produtor.send(
        "mensagens",
        key = b"Chave %d" % x,
        value = b"Mensagem %f " % n
    )

