#!/usr/bin/env bash
# MeshEnvy commits onto release tag, then TinyBBS on top. Fix conflicts + git rebase --continue as needed.
set -euo pipefail
cd "$(dirname "$0")"

TAG="${TAG:-v2.7.21.1370b23}"
REMOTE="${REMOTE:-meshenvy}"
FEAT="${FEAT:-meshenvy/feat/vfs-ls-and-xmodem-ls}"

git fetch "$REMOTE"
git checkout -B meshenvy-over-tag "$FEAT"
git rebase --onto "$TAG" "$REMOTE/develop" meshenvy-over-tag

git checkout tinybbs
git rebase --onto meshenvy-over-tag "$TAG" tinybbs
