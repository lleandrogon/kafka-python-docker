#!/usr/bin/env python
# coding: utf-8

# In[1]:


from kafka import KafkaConsumer as kc

consumidor = kc(
    "mensagens",
    bootstrap_servers = "kafka:9092",
    consumer_timeout_ms = 1000,
    group_id = "consumidores"
)


# In[3]:


for mensagem in consumidor:
    print("Topic: ", mensagem.topic)
    print("Partição ", mensagem.partition)
    print("Chave ", mensagem.key)
    print("Offset ", mensagem.offset)
    print("Mensagem ", mensagem.value)
    print("------------------")

