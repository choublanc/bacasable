FROM nvidia/cuda:12.1.0-cudnn8-devel-ubuntu20.04



ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y tzdata curl
RUN echo "Etc/UTC" > /etc/timezone && \
    ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata
RUN apt-get install -y software-properties-common

# Installation de Python 3.10
RUN add-apt-repository ppa:deadsnakes/ppa && apt-get update
RUN apt-get install -y python3.10 python3.10-distutils
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3.10 get-pip.py && \
    rm get-pip.py
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

# Réinitialiser la variable d'environnement DEBIAN_FRONTEND
ENV DEBIAN_FRONTEND=


# IDE & ML installation
RUN pip3 install jupyter
RUN pip3 install jupyterthemes
RUN jt -t onedork -T -N -kl  # Remplacez 'chesterish' par le nom du thème de votre choix


RUN pip install openllm
COPY vllm /vllm
WORKDIR /vllm
#RUN pip install -e .
RUN curl -fsSL https://get.docker.com | sh
RUN pip install "bentoml[all]"
