#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :comm_util.py
# @Time     :2021/3/18 下午4:41
# @Author   :Chang Qing

import os
import sys
import yaml
import logging
import logging.config

import torch


def setup_logger(default_path, default_level=logging.INFO):
    """
    Set up logging configuration
    :param default_path: file to logging configuration
    :param default_level: logging level (default: logging.INFO)
    :return: root logger
    """
    if default_path and os.path.isfile(default_path):
        with open(default_path, "rt") as f:
            logger_conf = yaml.load(f.read())
        file_handler_dir = logger_conf["handlers"]["file_handler"]["file_name"]
        error_handler_dir = logger_conf["handlers"]["error_handler"]["file_name"]
        if not file_handler_dir:
            file_handler_dir = "logs/info.log"

        if error_handler_dir:
            error_handler_dir = "logs/error.log"
        os.makedirs(file_handler_dir, exist_ok=True)
        os.makedirs(error_handler_dir, exist_ok=True)
        logging.config.dictConfig(logger_conf)
    else:
        logging.basicConfig(level=default_level, format="[%(asctime)15s][%(levelname)6s][%(filename)s]: %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S")
    return logging.getLogger("root")


def setup_device(n_gpu_need):
    logger = logging.getLogger("root")
    n_gpu_available = torch.cuda.device_count()
    if n_gpu_need == 0:
        logger.info("run models on CPU.")
    if n_gpu_available == 0 and n_gpu_need > 0:
        logger.warning("Warning: There\'s no GPU available on this machine, training will be performed on CPU.")
    elif n_gpu_need > n_gpu_available:
        n_gpu_need = n_gpu_available
        logger.warining(
            "Warning: The number of GPU\'s configured to use is {}, but only {} are available on this machine.".format(
                n_gpu_need, n_gpu_available))
    else:
        logging.info(f"run model on {n_gpu_need} gpu(s)")
        gpu_list_str = os.environ["CUDA_VISIABLE_DEVICE"]
        gpu_list_ids = [int(i) for i in gpu_list_str.split(",")][:n_gpu_need]
    return n_gpu_need, gpu_list_ids




if __name__ == '__main__':
    logger = setup_logger(None)
    logger.info("hello world")
