#! /usr/bin/env python3

import logging
import logging.config
import logging.handlers
import time

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "socket": {
            "class": "logging.handlers.SocketHandler",
            "host": "localhost",
            "port": logging.handlers.DEFAULT_TCP_LOGGING_PORT,
        },
    },
    "root": {"handlers": ["socket"], "level": "DEBUG"},
}

logging.config.dictConfig(LOGGING)

LOG = logging.getLogger("example-client")

LOG.debug("this is a debug message")
time.sleep(1)
LOG.info("this is an info message")
time.sleep(1)
LOG.warning("this is a warning message")
time.sleep(1)
LOG.error("this is an error message")
time.sleep(1)
LOG.exception("this is an exception message")

