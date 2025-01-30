from compression_tool.main import char_counter, build_huffman_tree

def test_character_counts():
    counts = char_counter("aaabbá")
    assert counts == {"a":3, "b":2, "á": 1}

def test_build_simple_tree():
    tree = build_huffman_tree({"a": 1, "b": 2})
    assert tree.weight == 3
    assert tree.key is None
    assert tree.left.weight == 1
    assert tree.left.key == "a"
    assert tree.right.weight == 2
    assert tree.right.key == "b"



