import wx
from dbInit import dbInit
from gui import mainGui
from utils import logger

logger = logger.set_operate_logger(__name__)

dbInit.db_init()
logger.info("START chms")
mainGui.call_mainGui()
logger.info("END chms")
