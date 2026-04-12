"""
gen_meshforge_data.py — PlatformIO pre: extra_script for TinyBBS data generation.

Runs as part of the PlatformIO build (before compilation) to generate the
binary data files that MeshForge will sideload onto the device after flashing.

Output: firmware/bbs-data/  (gitignored)
  wordle.bin    — packed Wordle dictionary for binary search on device
  geo_us.bin    — packed US city geocoding index
  survival.bin  — packed emergency survival guide

Referenced by firmware/meshforge.yaml:
  data:
    - bbs-data/*.bin:/ext/bbs/kb
"""

Import("env")  # noqa: F821 — PlatformIO SCons environment

import os
import sys
import subprocess

# Resolve paths relative to the firmware project root (where platformio.ini lives)
PROJECT_DIR = env["PROJECT_DIR"]  # noqa: F821
SCRIPTS_DIR = os.path.join(PROJECT_DIR, "scripts")
OUTPUT_DIR  = os.path.join(PROJECT_DIR, "bbs-data")

os.makedirs(OUTPUT_DIR, exist_ok=True)

python = sys.executable


def run_gen(script: str, *extra_args: str) -> None:
    script_path = os.path.join(SCRIPTS_DIR, script)
    cmd = [python, script_path, *extra_args]
    print(f"[meshforge] Running {script}...")
    result = subprocess.run(cmd, cwd=PROJECT_DIR)
    if result.returncode != 0:
        raise SystemExit(f"[meshforge] {script} failed (exit {result.returncode})")


# Wordle dictionary (source: scripts/wordle_words.txt — plain text, one word per line)
run_gen(
    "gen_wordle_packed.py",
    os.path.join(SCRIPTS_DIR, "wordle_words.txt"),
    os.path.join(OUTPUT_DIR, "wordle.bin"),
)

# US geo index (cities1000.txt lives alongside the script)
run_gen(
    "gen_geo_packed.py",
    os.path.join(SCRIPTS_DIR, "cities1000.txt"),
    os.path.join(OUTPUT_DIR, "geo_us.bin"),
)

# Survival guide
run_gen(
    "gen_survival_packed.py",
    os.path.join(OUTPUT_DIR, "survival.bin"),
)

print(f"[meshforge] Data files generated in {OUTPUT_DIR}/")
