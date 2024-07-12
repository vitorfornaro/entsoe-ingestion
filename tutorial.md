## Detalhamento Airflow

![Alt text](image.png)


## Entrar no container para visualizar as DAGs de exemplo

Entrar no container para verificar as DAGs:

1- Obtenha o container id do `scheduler` atraves do comando: 

```
docker container ls
```

O exemplo de output:

```
CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS                   PORTS                              NAMES
20ad86939ed4   apache/airflow:2.9.2   "/usr/bin/dumb-init …"   4 minutes ago   Up 3 minutes (healthy)   0.0.0.0:8080->8080/tcp             airflow-docker-airflow-webserver-1
ef0a50279860   apache/airflow:2.9.2   "/usr/bin/dumb-init …"   4 minutes ago   Up 3 minutes             8080/tcp                           airflow-docker-airflow-scheduler-1
7129bc81508b   apache/airflow:2.9.2   "/usr/bin/dumb-init …"   4 minutes ago   Up 3 minutes (healthy)   0.0.0.0:5555->5555/tcp, 8080/tcp   airflow-docker-flower-1
a6e718e58d70   apache/airflow:2.9.2   "/usr/bin/dumb-init …"   4 minutes ago   Up 3 minutes             8080/tcp                           airflow-docker-airflow-worker-1
d44c63ec15c5   postgres:13            "docker-entrypoint.s…"   4 minutes ago   Up 4 minutes (healthy)   5432/tcp                           airflow-docker-postgres-1
1f412e4b38c5   redis:latest           "docker-entrypoint.s…"   4 minutes ago   Up 4 minutes (healthy)   0.0.0.0:6379->6379/tcp             airflow-docker-redis-1
```

Acesse o container executando o seguinte comando:

```
docker exec -it <container_id>
```

Caminho para as DAGs de exemplo:

```
cd /home/airflow/.local/lib/python3.12/site-packages/airflow/example_dags
```

