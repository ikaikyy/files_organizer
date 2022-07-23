from pathlib import Path
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("path", type=str, help="the dir you want to organize")

args = parser.parse_args()

for target in list(Path(args.path).iterdir()):
    if Path(target).is_file():
        file_suffix = Path(target).suffixes[len(Path(target).suffixes) - 1].replace(".", "")
        if (Path(args.path) / file_suffix) in list(Path(args.path).iterdir()):
            Path(target).rename(Path(args.path) / file_suffix / Path(target).name)
        else:
            (Path(args.path) / file_suffix).mkdir()
            Path(target).rename(Path(args.path) / file_suffix / Path(target).name)