import logging
import logging.config
logging.config.fileConfig('S12_02.conf')
logger = logging.getLogger('myLogger')


myvar = 42
logger.warning('My warning. mywar is %d', myvar)
logger.debug('Shit dont work figure it out')

