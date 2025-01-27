import multiprocessing

bind = '127.0.0.1:8080'
pidfile = '/home/genro/gunicorn_sandbox.pid'
daemon = False
workers = multiprocessing.cpu_count()
threads = 8
loglevel = 'error'
chdir = '/home/genro/genropy_projects/sandbox/instances/sandboxpg'
reload = False
capture_output = True
max_requests = 600
max_requests_jitter = 50
timeout = 1800
graceful_timeout = 600
