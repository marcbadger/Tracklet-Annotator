import argparse

from Annotator.annotator import Annotator

def main(start_dir=None):
	Annotator(start_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Launch annotator with a starting directory.")
    parser.add_argument('--start_dir', type=str, default=None)
    args = parser.parse_args()

    main(start_dir = args.start_dir)