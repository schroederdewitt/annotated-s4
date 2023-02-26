#!/bin/bash

/home/duser/venv/bin/activate
python3 s4/train.py dataset=cifar layer=s4 train.epochs=1000 train.bsz=64 train.lr=5e-3 train.lr_schedule=true model.d_model=512 model.n_layers=6 model.dropout=0.0 train.weight_decay=0.05 model.prenorm=true model.embedding=true wandb.mode=offline train.sample=308 train.checkpoint=1