import pathlib
from typing import Union


class HuffmanTree:
    def __init__(
        self,
        weight: int,
        left: Union["HuffmanTree", None],
        right: Union["HuffmanTree", None],
        key: str | None,
    ):
        self.key = key
        self.weight = weight
        self.left = left
        self.right = right


def build_huffman_tree(frequencies: dict[str, int]) -> HuffmanTree:
    raise NotImplementedError


def char_counter(content: str) -> dict[str, int]:
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
