from sqls import create, drop, insert
from dbInit import accountingDB, baseDB
from datetime import datetime
import os
from utils import logger

logger = logger.set_operate_logger(__name__)


def db_init():
    if not os.path.exists("./data.db"):
        logger.info("START datebase init process")
        create.create_base()
        create.create_accounting()
        create.create_cache()
        insert.insert_cache(['', '', '', '', '', '', '', '', ''])
        try:
            use_list = baseDB.create_init_list()
            for item in use_list:
                insert.insert_base(item)
            accounting_list = accountingDB.create_list()
            for item in accounting_list:
                insert.insert_accounting(item)
            logger.info("DO datebase insert process")
        except:
            logger.info("PASS datebase insert process")
        logger.info("END datebase init process")
