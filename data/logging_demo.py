import logging
 
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug('Pipeline Started')
logging.info('Pipeline Started')
logging.warning('Pipeline Started')
logging.error('Pipeline Started')
logging.critical('Pipeline Started')

try:
    amount='100'
    total=int(amount) +50
    logging.info(f'Total amount calculated :{total}')
except Exception as e:
    logging.error(f'pipeline failed : {e}')
    
logging.info('pipeline finished')

 