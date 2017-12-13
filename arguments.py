import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--simulator', dest='simulator', type=str, help='The name of the simulator', required=True)
    return parser.parse_args()

