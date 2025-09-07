# Elastic search

```
$ docker network create somenetwork
$ docker run -d --name elasticsearch --net somenetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:tag
```

```
version: '3.8'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.1 # Use a specific version
    container_name: elasticsearch
    ports:
      - "9200:9200"
      - "9300:9300"
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false # For development/testing, disable security
    volumes:
      - esdata:/usr/share/elasticsearch/data
volumes:
  esdata:
    driver: local

```