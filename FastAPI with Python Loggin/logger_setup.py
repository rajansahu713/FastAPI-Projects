import logging
from logging.handlers import TimedRotatingFileHandler

# Custom filter to filter log records based on severity level
class SeverityFilter(logging.Filter):
    def __init__(self, severity):
        super().__init__()
        self.severity = severity

    def filter(self, record):
        return record.levelno == self.severity

# Set up logging
logging.basicConfig(level=logging.NOTSET)

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Create a TimedRotatingFileHandler for each level and attach filter
info_handler = TimedRotatingFileHandler(filename="logs/info/info.log", when="midnight", backupCount=7)
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)
info_handler.addFilter(SeverityFilter(logging.INFO))

warning_handler = TimedRotatingFileHandler(filename="logs/warning/warning.log", when="midnight", backupCount=7)
warning_handler.setLevel(logging.WARNING)
warning_handler.setFormatter(formatter)
warning_handler.addFilter(SeverityFilter(logging.WARNING))

error_handler = TimedRotatingFileHandler(filename="logs/error/error.log", when="midnight", backupCount=7)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)
error_handler.addFilter(SeverityFilter(logging.ERROR))

# Create a logger
logger = logging.getLogger()
logger.addHandler(info_handler)
logger.addHandler(warning_handler)
logger.addHandler(error_handler)

