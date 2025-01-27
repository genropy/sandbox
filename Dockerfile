############################################################
# Dockerfile to build Genropy container images
############################################################

FROM ghcr.io/genropy/genropy:latest
USER genro

COPY --chown=genro:genro sandbox-supervisord.conf /etc/supervisor/conf.d/
COPY --chown=genro:genro sandbox-gunicorn.py /home/genro/gunicorn.py
ADD --chown=genro:genro . /home/genro/genropy_projects/sandbox
RUN gnr app checkdep -i sandboxpg
ENTRYPOINT ["/usr/bin/supervisord"]


