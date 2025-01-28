import argparse
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="archivo a procesar", type=pathlib.Path)
args = parser.parse_args()

with open(args.filepath, 'r') as reader:
    reader.read()