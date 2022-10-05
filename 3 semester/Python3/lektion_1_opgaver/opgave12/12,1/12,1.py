import logging
import mymodule

logger = logging.getLogger('myLogger')

logging.basicConfig(filename='lektion_1_opgaver/12,1/log12.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s\%(module)s %(lineno)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.warning('Watch out')
warningvar = "Shits on fire"
logging.warning(warningvar)
logging.debug('My debugging message')

mymodule.myFunc()


