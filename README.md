# Listen Attend and Spell

![apm](https://img.shields.io/apm/l/vim-mode.svg)

PyTorch implementation of Listen Attend and Spell Automatic Speech Recognition (ASR).
[paper](https://arxiv.org/abs/1508.01211).
```
@article{chan2015las,
title={Listen, Attend and Spell},
author={William Chan, Navdeep Jaitly, Quoc V. Le, Oriol Vinyals},
journal={arXiv:1508.01211},
year={2015}
}
```
## DataSet

### Introduction
Aishell is an open-source Chinese Mandarin speech corpus published by Beijing Shell Shell Technology Co.,Ltd.

400 people from different accent areas in China are invited to participate in the recording, which is conducted in a quiet indoor environment using high fidelity microphone and downsampled to 16kHz. The manual transcription accuracy is above 95%, through professional speech annotation and strict quality inspection. The data is free for academic use. We hope to provide moderate amount of data for new researchers in the field of speech recognition.

```
@inproceedings{aishell_2017,
  title={AIShell-1: An Open-Source Mandarin Speech Corpus and A Speech Recognition Baseline},
  author={Hui Bu, Jiayu Du, Xingyu Na, Bengu Wu, Hao Zheng},
  booktitle={Oriental COCOSDA 2017},
  pages={Submitted},
  year={2017}
}
```

### Obtain
Create a data folder then run:
```bash
$ wget http://www.openslr.org/resources/33/data_aishell.tgz
```

## Dependencies
- python 3.8.5
- pytorch 1.9.0
- cudatoolkit 11.1.1
- cudnn 8.2.1.32

## Usage

### Data wrangling
Extract data_aishell.tgz, then extract all xxx.tar.gz as xxx.wav files into train/dev/test folders:
```bash
$ python extract.py
```

Scan transcript data, generate features:
```bash
$ python pre_process.py
```

Now the folder structure under data folder is sth. like:

<pre>
data/
    data_aishell.tgz
    data_aishell/
        transcript/
            aishell_transcript_v0.8.txt
        wav/
            train/
            dev/
            test/
    aishell.pickle
</pre>

### Train
```bash
$ python train.py
```

To visualize the training process：
```bash
$ tensorboard --logdir=runs
```

### Demo
```bash
$ python demo.py
```

## Results

## Reference
[1] W. Chan, N. Jaitly, Q. Le, and O. Vinyals, “Listen, attend and spell: A neural network for large vocabulary conversational speech recognition,” in ICASSP 2016. (https://arxiv.org/abs/1508.01211v2)