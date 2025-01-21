
# Homework

## **Question 1:** Understanding docker first run

To run the python image using Docker, you can use the following command:

```bash
docker run -it --entrypoint bash python:3.12.8
```

At first, Docker will probably failed to run the image because it is not downloaded yet (the image might not be available locally yet). In this case, Docker will download the image from Docker Hub and then run it. After the image is downloaded, you will be in the bash shell of the python image. The prompted result will be similar to the following:

```bash
~> docker run -it --entrypoint bash python:3.12.8
Unable to find image 'python:3.12.8' locally
3.12.8: Pulling from library/python
e474a4a4cbbf: Pull complete 
d22b85d68f8a: Pull complete 
936252136b92: Pull complete 
94c5996c7a64: Pull complete 
c980de82d033: Pull complete 
e05e1469c731: Pull complete 
ded9ddaf4f92: Pull complete 
Digest: sha256:5893362478144406ee0771bd9c38081a185077fb317ba71d01b7567678a89708
Status: Downloaded newer image for python:3.12.8
root@a354907f0f96:/# 
```

Now, to check the pip version, you can use the following command inside the bash shell container:

```bash
pip --version
```

The result, in January 2025, is the next one:

```bash
root@a354907f0f96:/# pip --version
pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
```

ANSWER: The pip version is `24.3.1`.

## **Question 2:** Understanding Docker networking and docker-compose

If you want to access the postgres container by port 5432 from the host machine, you can use `localhost` as the hostname. However, if you plan to use the service within the context of a docker compose infrastructure, you should use the service name as the hostname. In this case, the service name is `postgres`, so that the hostname should be `postgres`. On the other hand, the port keeps the same value, `5432`.

(*) NOTE: to be able to use the postgres service directly from your host machine, you should first define a network, configure as `bridge`, and then attach the postgres service to this network. This way, you can access the postgres service by using the `localhost` hostname and the port `5432`. You can do the same thing to the other service.

ANSWER:
- Hostname: `postgres`
- Port: `5432`