import logging
from logging.config import dictConfig

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard": {
            "format": "%(levelname)-10s - %(name)-15s : %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/infos.log",
            "mode": "w",
            "formatter": "verbose"
        }
    },
    "loggers": {
        "bot": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False
        },
        "discord": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False
        }
    }
}

dictConfig(LOGGING_CONFIG)