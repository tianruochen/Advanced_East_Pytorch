#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :conf_util.py
# @Time     :2021/3/18 下午7:48
# @Author   :Chang Qing
import os
from typing import Any

import yaml
import logging

logger = logging.getLogger(__name__)


class AttrDict(dict):
    # command + o 重写父类的方法
    def __setattr__(self, key: str, value: Any) -> None:
        self[key] = value

    def __getattr__(self, key: str) -> Any:
        return self[key]


def recursive_convert(attr_dict):
    """
    convert an instance of AttrDict to object recursively
    :param attr_dict: an instance of AttrDict
    :return: an dict like object
    """
    if not isinstance(attr_dict, dict):
        return attr_dict
    obj_dict = AttrDict()
    for key, value in attr_dict.items():
        obj_dict[key] = recursive_convert(value)
    return obj_dict


def parse_config(cfg_file):
    """
    Load a config file into AttrDict
    :param cfg_file: path to model config file
    :return: a instance of AttrDict
    """

    with open(cfg_file, "r") as f:
        #  == yaml_conf = AttrDict(yaml.load(f.read()))
        dict_conf = AttrDict(yaml.load(f, Loader=yaml.Loader))
    obj_conf = recursive_convert(dict_conf)
    return obj_conf


def merge_config(cfg, args_dict):
    loader_cfg_node = getattr(cfg, "LOADER")
    trainer_cfg_node = getattr(cfg, "TRAINER")
    for key, value in args_dict.items():
        if value is None:
            continue
        try:
            if hasattr(loader_cfg_node, key):
                setattr(loader_cfg_node, key, value)
            if hasattr(trainer_cfg_node, key):
                setattr(trainer_cfg_node, key, value)
        except Exception as e:
            # import traceback
            # traceback.print_exc()
            logger.warning(e)
            pass
    if trainer_cfg_node.save_dir and not os.path.exists(trainer_cfg_node.save_dir):
        os.makedirs(trainer_cfg_node.save_dir, exist_ok=True)
    return cfg


def print_config():
    pass


if __name__ == '__main__':
    a = {"c": {"a": 1, "b": 2}, "d": 3}
    a = AttrDict(a)
    a = recursive_convert(a)
    print(a)
    print(a.c)
    print(a.c.a)
    a.c.a = 4
    print(a.c.a)
