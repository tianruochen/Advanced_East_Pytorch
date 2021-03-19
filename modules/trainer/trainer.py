#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName :trainer.py
# @Time     :2021/3/19 下午4:17
# @Author   :Chang Qing

from modules.trainer.base_trainer import BaseTrainer


class Trainer(BaseTrainer):
    def __init__(self, config):
        self.config = config

        # set up data loader
        self.train_loader, self.valid_loader, self.train_nums, self.valid_nums = get_dataloader(
            self.config.data_loader
        )
        self.model = ""
        self.loss = ""
        self.metrics = ""
        self.optimizer = ""
        self.train_loader = ""
        self.valid_loader = ""
        self.lr_scheduler = ""
        self.logger = ""

    def train(self):
        pass