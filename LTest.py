import sys
import logging

#import ipgetter

LogEntryFormat = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format = LogEntryFormat)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)



logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('PC.log')
fileHandler.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.ERROR)

#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s   %(module)s')
formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)

logger.error("aaa %s", "xxx", extra=d)

logger.warning('Protocol problem: %s', 'connection reset', extra=d)


progress = 555

#sys.stdout.write("Download progress: %d%%   \r" % (progress) )
#sys.stdout.flush()

#myIP = ipgetter.myip()
myIP = '1.2.3.4'

logger.info('IP address: %s', myIP, extra = d)
