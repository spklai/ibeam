import signal
import sys
import subprocess
import logging

def signal_handler(sig, frame):
    logger = logging.getLogger('ibeam')
    logger.info(f"Received {signal.Signals(sig).name}, performing graceful shutdown...")
    subprocess.run('bash /app/tailscale logout', shell=True)
    sys.exit(0)
