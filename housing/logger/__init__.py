import logging
from datetime import datetime
import os
from housing.constant import get_current_time_stamp  
 

LOG_DIR="logs"
# correnttime=f"{datetime.now().strftime('%Y-%M-%D-%H-%M-%S')}"
# logfile='log-{correnttime}.log'
os.makedirs(LOG_DIR,exist_ok=True)

def get_log_file_name():
    return f"log_{get_current_time_stamp()}.log"

LOG_FILE_NAME=get_log_file_name()

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

# logging.basicConfig(filename=LOGGING_DIR.join(logfile),filemode='W',level=logging.INFO)
logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
level=logging.INFO
)