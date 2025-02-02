import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fmtr = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")

dbg_handler = logging.FileHandler('.dbg.log')
dbg_handler.setLevel(logging.DEBUG)
dbg_handler.setFormatter(fmtr)
logger.addHandler(dbg_handler)

wrn_handler = logging.FileHandler(".warn.log")
wrn_handler.setLevel(logging.WARNING)
wrn_handler.setFormatter(fmtr)
logger.addHandler(wrn_handler)

if __name__ == "__main__":
    logger.info("info")
    logger.debug("dbg")
    logger.warning("warning")
    logger.critical("critical")
    logger.exception("exception")