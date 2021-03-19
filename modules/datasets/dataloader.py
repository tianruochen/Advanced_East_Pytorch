#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :dataloader.py.py
# @Time     :2021/3/19 下午4:36
# @Author   :Chang Qing

from torch.utils.data import DataLoader

class NormDataLoader(DataLoader):
    pass

class LmdbDataLoader(DataLoader):
    pass



LOADER_MAP = {
    "normdataloader": NormDataLoader,
    "lmdbdataloader": LmdbDataLoader
}

def get_dataloader(loader_cfg):
    type = loader_cfg.type
    image_fmt = loader_cfg.image_fmt
    n_workers = loader_cfg.n_workers
    pin_memory = loader_cfg.pin_memory
    batch_size = loader_cfg.batch_size
    train_cfg_node = loader_cfg.train_loader
    valid_cfg_node = loader_cfg.valid_loader
    tarin_dataset, valid_dataset = get_datasets()

    train_loader = LOADER_MAP[type](dataset=train_data_set,
                                    shuffle=)


