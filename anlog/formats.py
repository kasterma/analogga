import re


class LogFormat:
    pass


class DateLevelMisc(LogFormat):
    """
    Example log line:

        [2019-04-19 12:46:00,020] INFO Registered kafka:type=kafka.Log4jController MBean (kafka.utils.Log4jControllerRegistration$)
    """
    regexp_raw = r"\[(.*)\] ([A-Z]*) (.*)"
    regexp = re.compile(regexp_raw)

    def __init__(self):
        pass
