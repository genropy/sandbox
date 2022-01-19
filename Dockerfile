############################################################
# Dockerfile to build Genropy container images
# Based on Ubuntu
############################################################

FROM public.ecr.aws/genropy/genropy-full
COPY . /home/genro/genropy_projects/sandbox
COPY docker /home/genro/genropy_projects/main
USER root
RUN chown -R genro:genro /home/genro/genropy_projects
USER genro

#ENV GNR_DB_IMPLEMENTATION = "postgres"
#ENV GNR_DB_HOST = "host.docker.internal"
#ENV GNR_DB_NAME = "sandboxpg"
#ENV GNR_ROOTPWD = "sandbox-root"
#
#ENV GNR_DB_IMPLEMENTATION= "postgres"
#ENV GNR_DB_HOST = "host.docker.internal"
#        - GNR_DB_NAME= "sandboxpg",
#        - GNR_ROOTPWD= 'sandbox-root'
#

CMD ["gnrdaemon"]