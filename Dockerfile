############################################################
# Dockerfile to build Genropy container images
# Based on Ubuntu
############################################################

FROM public.ecr.aws/genropy/genropy:0.0.2i

ADD . /home/genropy_projects/sandbox
ADD supervisord.conf /home/supervisord.conf

EXPOSE 8080
ENV GNR_LOCALE en_EN
ENV GNR_CURRENT_SITE sandbox
ENV GNR_WSGI_OPT_remote_edit t
ADD nginx.conf /home/nginx.conf
ADD mime.types /home/mime.types

ENTRYPOINT ["/usr/bin/supervisord" ,"-c" ,"/home/supervisord.conf"]

