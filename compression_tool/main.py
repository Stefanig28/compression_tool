import pathlib

def char_counter(content: str):
    frequency = {}

    for char in content:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency


def _cli():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=pathlib.Path)
    args = parser.parse_args()

    print(char_counter(args.file.read_text(encoding="utf-8")))

if __name__ == "__main__":
    _cli()



