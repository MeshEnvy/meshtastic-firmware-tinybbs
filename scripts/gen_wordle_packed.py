#!/usr/bin/env python3
"""
gen_wordle_packed.py — Generate packed Wordle validation dictionary for external flash.

Reads a plain-text word list (one lowercase 5-letter word per line) and writes
a sorted binary file for binary search on the device.

Binary format:
  Header (8 bytes):
    magic   uint32  0x57444C31 ("WDL1")
    count   uint32  number of words

  Words (5 bytes each, sorted, lowercase, no null terminator):
    "aalii"
    "aahed"
    ...

Usage:
    python3 scripts/gen_wordle_packed.py [word_list] [output]

Defaults:
    word_list  → scripts/wordle_words.txt
    output     → data/fs/__ext__/wordle.bin
"""

import os
import struct
import sys

MAGIC = 0x57444C31  # "WDL1"


def load_words(word_list_path):
    words = []
    with open(word_list_path, encoding='utf-8') as f:
        for line in f:
            w = line.strip().lower()
            if len(w) == 5 and w.isalpha():
                words.append(w)
    return sorted(set(words))


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    word_list_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(script_dir, 'wordle_words.txt')
    output_path    = sys.argv[2] if len(sys.argv) > 2 else os.path.join(script_dir, '..', 'data', 'fs', '__ext__', 'wordle.bin')

    if not os.path.exists(word_list_path):
        print(f'ERROR: {word_list_path} not found')
        sys.exit(1)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f'Reading words from {word_list_path}...')
    words = load_words(word_list_path)
    print(f'  {len(words)} unique words')

    with open(output_path, 'wb') as f:
        f.write(struct.pack('<II', MAGIC, len(words)))
        for w in words:
            f.write(w.encode('ascii'))

    size = os.path.getsize(output_path)
    print(f'Output: {output_path}')
    print(f'  {len(words)} words, {size} bytes ({size / 1024:.1f} KB)')


if __name__ == '__main__':
    main()
