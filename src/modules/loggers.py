import logging
from src.global_params import system_config_params
from logging import StreamHandler
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import datetime

def create_logger(name,
                level_log = logging.INFO,
                level_handle = logging.DEBUG, 
                formatter = None,
                log_dir = None, 
                stream=True):

    logger = logging.getLogger(name)
    logger.setLevel(level_log)

    if stream:
        stream_handler = StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(level_handle)
        logger.addHandler(stream_handler)
        if formatter is None:
            stream_handler.setFormatter(formatter)

    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, datetime.now().strftime("%Y-%m-%d.txt"))
        file_handler = TimedRotatingFileHandler(
            filename=log_path,
            when="midnight",
            interval=1,
            backupCount=7,
            encoding='utf-8',
            utc=False
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level_handle)
        logger.addHandler(file_handler)
    return logger

console_formatter = logging.Formatter('%(levelname)s - %(message)s')
console_logger = create_logger(name='app',level_log=logging.DEBUG if system_config_params.debug else logging.INFO,formatter=console_formatter)



history_operation_formatter = logging.Formatter(
    fmt='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
operation_history_log = create_logger('history',level_handle=logging.INFO,formatter=history_operation_formatter,log_dir=rf'{system_config_params.log_dir}\operation')




