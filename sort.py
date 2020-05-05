import os
import numpy as np
import argparse
import matplotlib.pyplot as plt
import time
import glob


def parse_args():
    parser = argparse.ArgumentParser(description="SORT demo")
    parser.add_argument('--display', dest='display', help='Display online tracker output (slow) [False]',
                        action='store_true')
    parser.add_argument("--seq_path", help="Path to detections.", type=str, default='data')
    parser.add_argument("--phase", help="Subdirectory in seq_path.", type=str, default='train')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # print("hello world")
    args = parse_args()
    display = args.display
    phase = args.phase
    colours = np.random.rand(32, 3)
    if (display):
        if not os.path.exists('mot_benchmark'):
            print(
                '\n\tERROR: mot_benchmark link not found!\n\n    Create a symbolic link to the MOT benchmark\n    (https://motchallenge.net/data/2D_MOT_2015/#download). E.g.:\n\n    $ ln -s /path/to/MOT2015_challenge/2DMOT2015 mot_benchmark\n\n')
            exit()
        plt.ion()
        fig = plt.figure()
        ax1 = fig.add_subplot(111, aspect='equal')
        print(os.path.exists('mot_benchmark'))
    if not os.path.exists('output'):
        os.makedirs('output')
    pattern = os.path.join(args.seq_path, phase, '*', 'det', 'det.txt')
    # print(pattern)
    for seq_dets_fn in glob.glob(pattern):
        print(seq_dets_fn)
    # print(display)
    # print(phase)
    # print(args)