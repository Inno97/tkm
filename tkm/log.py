############################################################
#    log
############################################################

# Contains the custom logger object to be used.

import logging
import sys
import os

def setup_custom_logger():
    """Setups the custom logger to be used globally.

    The logger object can be referenced via 'root' in logging.getLogger().

    Returns:
        The logger object to be used in the script.
    """
    logging.basicConfig(filename=os.getcwd() + '\\output.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    stdout_handler = logging.StreamHandler(sys.stdout)
    log.addHandler(stdout_handler)
    return log

def get_logger():
    """Returns the logger object to be used.
    """
    log = setup_custom_logger() if not logging.getLogger('root').hasHandlers() \
        else logging.getLogger('root')

    return log
