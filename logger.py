import logging  

logger = logging.getLogger('birthday_bot')  
logger.setLevel(logging.INFO)  
handler = logging.FileHandler('bot.log')  
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))  
logger.addHandler(handler)
