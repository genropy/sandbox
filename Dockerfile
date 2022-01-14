############################################################
# Dockerfile to build Genropy container images
# Based on Ubuntu
############################################################

FROM public.ecr.aws/genropy/genropy-full
COPY . /home/genropy_projects/sandbox
COPY docker /home/genropy_projects/main

CMD [ "supervisord","-c","/home/supervisord.conf"]