import logging.config
from util import jieba_test
from util.jieba_test import correct_cut
from pythonProject import main

def test_logging(logger_=None):
    if logger_:
        logger_.info("test_log")
        logger_.info("test_log2")
    else:
        return None


def basic_config():
    logging.basicConfig(level=logging.INFO)
    return logging


def basic_config_with_format():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] line %(lineno)d %(message)s')
    return logging


def using_logger():
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] line %(lineno)d %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


def time_rotate_logger():
    logger = logging.getLogger('timeRotateLogger')
    return logger


def count_rotate_logger():
    logger = logging.getLogger('countRotateLogger')
    return logger


def main():
    # logger = basic_config()
    # logger = basic_config_with_format()
    # logger = using_logger()
    # test_logging(logger)

    # logging.config.fileConfig('logging.conf')
    # logger = time_rotate_logger()
    # logger = count_rotate_logger()
    # test_logging(logger)

    datas = ["NIKON D780 單機身 公司貨", "3M 瞬涼5度抑螨可水洗烘乾涼夏兩用被-星空藍(180x210cm)"]
    for data in datas:
        print("correct: ", correct_cut(data))


if __name__ == '__main__':
    main()
