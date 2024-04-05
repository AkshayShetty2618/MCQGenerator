import logging
import os
from datetime import datetime 

 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs") # to save the logs in the current working directory

os.makedirs(log_path,exist_ok=True)


LOG_FILEPATH=os.path.join(log_path,LOG_FILE)


logging.basicConfig(level=logging.INFO,  # label of logging for more information look into python logger documentaion
        filename=LOG_FILEPATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s" 
) # asctime current time , line no : number of the line in the log, level name: name of the selected level of the log, messgae: message of the log




