"""
Description:
    Entry point for fausser



TODO:
    - one file or multiple on input?
"""
import os
import sys
import argparse

# local modules
import wave_io


def resolve_path(filepath):
    """A function to return the absolute path given a 
    file path. No exception handling right now.

    Args:
        - filepath (str): a path
    
    Returns:
        - path (str): absolute path
    """
    return os.path.abspath(filepath)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A command line interface tiling utility.")

    parser.add_argument("-i", "--input_path", nargs="?", 
                        default='fausser/input/', help="path to directory.")

    parser.add_argument("-size", "--output_size",  nargs="?", 
                        default=1000, help="number of timesteps outthe output.")

    parser.add_argument("-n", "--n_in",  nargs="?", 
                        default=1000, help="number of timesteps outthe output.")

    # parser.add_argument("-n", "--sample_size", nargs="?", default=None, 
    #                     help="number of images to randomly sample. If not specified, all tiles returned.")

    # parser.add_argument("-o", "--output_dir", nargs="?", default='tilerUtility/outputs', 
    #                     help="output directory for saving images. no slash `/` at the end. ")

    args = parser.parse_args()
    input_path = resolve_path(args.input_path)
    output_size = int(args.output_size)

    # make waver
    waves = wave_io.WaverIn(dirpath=input_path, size=output_size)
    waves.load_samples()

    

