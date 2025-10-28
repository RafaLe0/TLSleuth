import logging
import logging.config
from os import path, makedirs


def setup_logging(default_path='logging.conf'):
    """Setup logging configuration and ensure log directory exists."""
    log_dir = 'logs'
    if not path.exists(log_dir):
        makedirs(log_dir)
    
    logging.config.fileConfig(default_path)
    logger = logging.getLogger()
    return logger
