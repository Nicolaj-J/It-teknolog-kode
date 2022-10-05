import logging

def myFunc():
    logger = logging.getLogger('myLogger')
    logger.warning('This shit is a warning (mymodule')
    logger.debug('Something is wrong we dont know (mymodule)')