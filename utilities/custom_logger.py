import logging
import os

class LogGen:

    @staticmethod
    def loggen():
        log_path = os.path.abspath("Logs") + "/automation.log"
        logging.basicConfig(filename=log_path,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger