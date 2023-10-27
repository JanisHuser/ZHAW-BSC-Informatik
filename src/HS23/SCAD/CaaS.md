# CaaS

## LXC

**Background**

- vendor neutral,
- linux specified

**Booting**

- from a directory, e.g. unpackaged image

```
/config     -> text file for e.g. mounts, capabilites, networks, ...
/rootfs     -> /bin /dev/ etc /home
```

**Namespacing of system resources**

- file systems, users, processes, network interfaces, ...
- in the linux kernel

**Application integration**

- native python library
- frontends such as Flockport


```python
import lxc

c = lxc.Container("myubuntucontainer")

c.create("download", 0, {
    "dist": "ubuntu",
    "release": "xenial",
    "arch": "amd64
    })
# Downloadint the rootfs... (~400 MB; alpine would be ~7 MB)
# -> True

c.running
# -> False

c.start()
# - True

import os
def f(): os.system("ps waux; ls -l /home")

c.attach_wait(f)
# - pid

```

## Rocket

## Docker

**Background**

- Docker inc
- Silicon Valley

**Booting**

- from a Docker container image with a layered file system
- images created by integration of Dockerfiles

**Namespacing of system resources**

- as processes through central daemon (or daemon-less, e.g. Podman)

**Application integration**

- composition and distributed computing tools (Docker Compose & Swarm)
- diverse networkign models, e.g. host mode, NAT bridge
- pass-through access to hardware via device files, e.g. GPU, USB
- access to local file system through volumes 

```Dockerifile
FROM python:3

RUN pip install requests && \
    rm /usr/lib/python3.6/site-packages/requests/__init__.py && \
    wget https://blalbla.deb && \
    dpkg -i blabla.deb

ADD my-application /srv/my-application
WORKDIR /srv

EXPOSE 8000

ENTRYPORT ["/usr/bin/dumb-init", "--"]
CMD ["/srv/my/application/start.sh]
```

**Build Dockerimage**

```shell
docker build -t mycontainer
```

**View images**

```shell
docker images
```

**Run container**

```shell
docker run -p 8080:8080 -it --rm \
    -v /var/www/html/:/usr/local/tomcat/webapps/news \
    mycontainer
```

**Debug**

- docker ps
- docker logs <instance>
- docker exec <instance>

## Docker Compose

Compose files (docker-compose.yaml) describe

- a set of microservices, implemented as Docker continers
- build and run configuration
- dependencies
- isntance details: replicas, restart policies, placement, networking, volumes

Compose tool

- canonical command: docker-compose up
- in contrast docerk-compose down --volumes
- log merging
- command execution per instance

Helper Tools

- service dependencies (-> V11): shell script wait-for-it