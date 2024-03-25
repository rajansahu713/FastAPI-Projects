<h2>This Python script is setting up a logging system for an application using the logging module from the Python standard library.</h2>

<h2>Let's break it down:</h2>

* A custom filter called SeverityFilter is defined. This filter can be used to filter log records based on their severity level (e.g. logging.INFO, logging.WARNING, logging.ERROR). The filter only allows log records with the specified severity level to pass through.
The logging module is configured with a base level of logging.NOTSET, which means that all log messages will be processed by the system.

* A formatter is created to specify the format of the log messages. The format includes the timestamp, the name of the logger, the log level, and the message.
Three TimedRotatingFileHandler objects are created, one for each severity level of INFO, WARNING, and ERROR. These handlers will write log messages to separate files, with each file containing logs from a single severity level. The **TimedRotatingFileHandler** will also rotate the log files daily (when="midnight") and keep 7 backups (backupCount=7).
* Each handler is assigned a filter with the corresponding severity level, so that only log records of the appropriate level will be written to the corresponding file.
* A logger is created with the name of the module or application using the getLogger() function. The logger is then added to the three handlers created in the previous step.
* Overall, this logging system will allow for easy tracking and filtering of log messages based on their severity level, and will keep a rolling set of logs for a week.
