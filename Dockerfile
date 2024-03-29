############################################################
# Dockerfile to build Genropy container images
# Based on Ubuntu
############################################################

FROM public.ecr.aws/x2x6r1v6/genropy:0.0.2g
MAINTAINER Francesco Porcari - francesco@genropy.org

ADD . /home/genropy_projects/sandbox
EXPOSE 8080

ENV GNR_CURRENT_SITE sandbox
ENV GNR_WSGI_OPT_remote_edit t
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD nginx.conf /home/nginx.conf
ADD mime.types /home/mime.types

ENTRYPOINT ["/usr/bin/supervisord"]

