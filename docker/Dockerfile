#FROM nvidia/11.8.0-cudnn8-devel-ubuntu22.04
FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04
MAINTAINER ANONYMOUS

# CUDA includes
ENV CUDA_PATH /usr/local/cuda
ENV CUDA_INCLUDE_PATH /usr/local/cuda/include
ENV CUDA_LIBRARY_PATH /usr/local/cuda/lib64

# Ubuntu Packages
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends software-properties-common -y && \
    add-apt-repository -y multiverse && apt-get update -y 
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade --no-install-recommends -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y apt-utils nano vim man build-essential wget sudo && \
    rm -rf /var/lib/apt/lists/*

# Install curl and other dependencies
RUN apt-get update -y 
RUN apt-get install -y curl libssl-dev openssl libopenblas-dev \
    libhdf5-dev hdf5-helpers hdf5-tools libhdf5-serial-dev libprotobuf-dev protobuf-compiler git

# Create local user
# https://jtreminio.com/blog/running-docker-containers-as-current-host-user/
ARG USER_ID
ARG GROUP_ID
RUN groupadd -g ${GROUP_ID} duser
RUN useradd -l -u ${USER_ID} -g duser duser
RUN install -d -m 0755 -o duser -g duser /home/duser
RUN chown --changes --silent --no-dereference --recursive ${USER_ID}:${GROUP_ID} /home/duser
 
#Install python3 pip3
RUN apt-get update
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update && apt-get install -y python3.8 python3.8-dev
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
RUN apt-get install -y python3-pip
RUN apt-get install -y python-apt --reinstall
RUN apt-get install -y htop iotop
RUN python3 -m pip uninstall pip setuptools wheel
RUN apt-get --reinstall install  python3-setuptools python3-wheel python3-pip
RUN apt-get install -y python3.8-venv

# Other system level tools
RUN apt-get install -y htop iotop

####### USER AREA ##########################################
USER duser
WORKDIR /home/duser
RUN mkdir ~/install

# Virtual Env
ENV VIRTUAL_ENV=~/venv
RUN python3 -m venv venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN ~/venv/bin/python3 -m pip install --upgrade pip


# Install JAX
RUN . /home/duser/venv/bin/activate && pip3 install "jax[cuda11_cudnn82]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
# pip3 install --upgrade "jax[cuda]" -f https://storage.googleapis.com/jax-releases/jax_releases.html

ADD ./requirements.txt reqs.txt
RUN . /home/duser/venv/bin/activate && pip3 install -r reqs.txt
RUN chmod +x /home/duser/venv/bin/activate

# make sure virtualenv is activated by default
RUN echo "source ~/venv/bin/activate" >> ~/.bashrc
RUN echo "source ~/venv/bin/activate" >> ~/.profile

EXPOSE 8888
WORKDIR /home/duser/entryfolder
