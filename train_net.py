#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :train.py.py
# @Time     :2021/3/18 下午3:48
# @Author   :Chang Qing


import argparse
import os

from modules.trainer.trainer import Trainer
from utils.comm_util import setup_logger, setup_device
from utils.config_util import parse_config, merge_config, print_config


def parse_args():
    parser = argparse.ArgumentParser(description="Advanced East Training Script")
    parser.add_argument("--model_config", type=str, default="configs/default.yaml", help="path to config file")
    parser.add_argument("--logger_config", type=str, default="configs/logger.yaml", help="path to logger config file")
    parser.add_argument("--batch_size", type=int, default=None, help="training batch size, None to use config setting")
    parser.add_argument("--learning_rate", type=float, default=None,
                        help="training learning rate, None to use config setting")
    parser.add_argument("--pretrain", type=str, default=None, help="path to pretrain weights")
    parser.add_argument("--use_gpu", type=bool, default=True, help="default use gpu")
    parser.add_argument("--epoch", type=int, default=None, help="epoch number, 0 for read from config file")
    parser.add_argument("--save_dir", type=str, default=None,
                        help="directory name to save train snapshoot, None to use config setting")
    parser.add_argument("--valid_interval", type=int, default=1, help="validation epoch interval, 0 for no validation")
    parser.add_argument("--log_interval", type=int, default=1, help="mini batch interval to log")
    parser.add_argument("--fix_random_seed", type=bool, default=False,
                        help="If set True, enable continuous evaluation job")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    # ctrl + shift + enter  自动结束代码， 并智能补充标点符号
    # command + shift + u 大小写转换
    args = parse_args()
    args.n_gpus, args.gpu_ids = setup_device(args.n_gpus)
    setup_logger(args.logger_config)
    config = parse_config(args.model_config)
    print_config(config)
    # vars() 函数返回对象object的属性和属性值的字典对象 将args转换为字典
    config = merge_config(config, vars(args))
    trianer = Trainer(config)
    trianer.trian()
