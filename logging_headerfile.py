import logging

logging.basicConfig(level=logging.INFO, filename="log.log" , filemode = "w", format='%(asctime)s - %(levelname)s - %(message)s') #it will be at info and above and skip debug. basicConfig works only once.

# x=2
# logging.debug("debugging")
# logging.info(f"information of x: {x}")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

# try:
#     1/0
# except ZeroDivisionError as e:
#     # logging.error("test",exc_info=True)
#     logging.exception("test")


#creating a custom logger
logger=logging.getLogger(__name__)

handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("test the custom logger")