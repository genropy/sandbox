############################################################
# Dockerfile to build Genropy container images
# Based on Ubuntu
############################################################

FROM genropy/genropy
MAINTAINER Francesco Porcari - francesco@genropy.org

ADD . /home/genropy_projects/sandbox
EXPOSE 8080
CMD ["/usr/local/bin/gnrdaemon"]



