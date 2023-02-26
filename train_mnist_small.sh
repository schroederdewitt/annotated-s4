#!/bin/bash

/home/duser/venv/bin/activate
python3 s4/train.py dataset=mnist layer=s4 train.epochs=1000 train.bsz=128 model.n_layers=6 model.d_model=128 model.layer.N=64 model.dropout=0.0 train.lr=5e-3 train.weight_decay=0.01 train.checkpoint=1