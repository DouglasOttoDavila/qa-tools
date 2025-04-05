bind = "0.0.0.0:8000"  # Bind to all IPs on port 8000
workers = 3  # Number of worker processes
threads = 2  # Number of threads per worker
timeout = 120  # Timeout for requests
loglevel = "info"  # Logging level
accesslog = "-"  # Log access to stdout
errorlog = "-"  # Log errors to stdout
