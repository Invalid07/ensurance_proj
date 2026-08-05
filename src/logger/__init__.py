import logging 
import os 
from logging.handlers import RotatingFileHandler    
from from_root import from_root
from datetime import datetime   


# LOG CONFIGURATION
LOG_DIR ="logs"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_FILE_SIZE = 5* 1024 * 1024  # 10 MB
BACKUP_COUNT =3


# Create the log directory if it doesn't exist
log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)
log_dir_path = os.path.join(log_dir_path, LOG_FILE)


# Configure the logger
def configure_logger():
    logger =logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # formate 
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # file handler with roation 
    file_handler = RotatingFileHandler(log_dir_path, maxBytes=MAX_LOG_FILE_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # console handler 
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # Adding handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


# calling object 
configure_logger()