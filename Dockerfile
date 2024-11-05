############################################################
# Dockerfile to build Genropy container images
############################################################

FROM ghcr.io/genropy/genropy:latest
USER genro

COPY --chown=genro:genro sandbox-supervisord.conf /etc/supervisor/conf.d/
ADD --chown=genro:genro . /home/genro/genropy_projects/sandbox
RUN gnr app checkdep -i sandbox
RUN gnr db setup sandbox
ENTRYPOINT ["/usr/bin/supervisord"]


