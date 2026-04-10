import json
import logging
import sys


def setup_logger():
    logger = logging.getLogger("pdf-worker")
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


def log_json(logger, level, message, **kwargs):
    log = {
        "message": message,
        **kwargs
    }

    getattr(logger, level)(json.dumps(log))
