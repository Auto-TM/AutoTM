import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("AutoTM")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

handler = RotatingFileHandler('../log/run.log', maxBytes=1 * 1024 * 1024, backupCount=150)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)
