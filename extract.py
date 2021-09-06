import os
from glob import glob
import tarfile


def extract(filename, to_dir):
    print('Extracting {}...'.format(filename))
    tar = tarfile.open(filename, 'r')
    tar.extractall(to_dir)
    tar.close()


if __name__ == "__main__":
    if not os.path.isdir('data/data_aishell'):
        extract(filename='data/data_aishell.tgz', to_dir='data')
    files = glob('data/data_aishell/wav/*.tar.gz')
    for file in files:
        extract(filename=file, to_dir='data/data_aishell/wav')
