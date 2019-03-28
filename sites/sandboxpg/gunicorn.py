

bind = 'unix:/Users/fporcari/sviluppo/public/projects/sandbox/sites/sandboxpg/sockets/gunicorn.sock'
pidfile = '/Users/fporcari/sviluppo/public/projects/sandbox/sites/sandboxpg/sandboxpg_pid'
daemon = False
accesslog = '/Users/fporcari/sviluppo/public/projects/sandbox/sites/sandboxpg/logs/access.log'
errorlog = '/Users/fporcari/sviluppo/public/projects/sandbox/sites/sandboxpg/logs/error.log'
logfile = '/Users/fporcari/sviluppo/public/projects/sandbox/sites/sandboxpg/logs/main.log'
workers = 9
loglevel = 'error'
chdir = '/Users/fporcari/sviluppo/public/projects/sandbox/sites/sandboxpg'
reload = False
capture_output = True
worker_class = 'gevent'
max_requests = 300
max_requests_jitter = 50
timeout = 1800
graceful_timeout = 600
