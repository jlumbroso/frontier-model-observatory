#!/usr/bin/env bash
# Rewrite preparation authorized by QST-HISTORY-CONFORMANCE, Option A.
#
# Outcome:
#   Completed 2026-09-05. Created the verified safety bundle at
#   /home/user/workspace/fmo-safety/pre-history-rewrite.bundle, rewrote 89
#   commits in a disposable mirror, removed TARGET_PATH from every reachable
#   ref, and force-pushed main and v0.1.0 with exact old-SHA leases. Rewritten
#   main is 4ba453b8553f4cf505d90516ab6ec60de12f7022; rewritten v0.1.0 is
#   edce79cced2f8db873b02d8262b8fc3eba4f5756. Local `just verify-complete`
#   passed on the clean rewritten tree; hosted verification run 33986456547
#   and hosted release run 33986456235 both passed.

set -euo pipefail

SOURCE_REPO=${1:?source repository path required}
MIRROR_REPO=${2:?disposable mirror path required}
SAFETY_BUNDLE=${3:?safety bundle path required}
TARGET_PATH='artifacts/sha256/80/805ca645079c287664890bdea737e22ebc8a66aca6e8f0a03d0ffeca86c4d17f/original.pdf'

if [[ -n "$(git -C "$SOURCE_REPO" status --porcelain)" ]]; then
    echo "source working tree is not clean" >&2
    exit 1
fi

mkdir -p "$(dirname "$SAFETY_BUNDLE")"
git -C "$SOURCE_REPO" bundle create "$SAFETY_BUNDLE" --all
git -C "$SOURCE_REPO" bundle verify "$SAFETY_BUNDLE"

rm -rf "$MIRROR_REPO"
git clone --mirror --no-local "$SOURCE_REPO" "$MIRROR_REPO"
git -C "$MIRROR_REPO" filter-repo \
    --force \
    --invert-paths \
    --path "$TARGET_PATH"

if git -C "$MIRROR_REPO" rev-list --all --objects | grep -F "$TARGET_PATH"; then
    echo "target path remains reachable after rewrite" >&2
    exit 1
fi

git -C "$MIRROR_REPO" fsck --full
printf 'rewritten main: %s\n' \
    "$(git -C "$MIRROR_REPO" rev-parse refs/heads/main)"
if git -C "$MIRROR_REPO" show-ref --verify --quiet refs/tags/v0.1.0; then
    printf 'rewritten v0.1.0: %s\n' \
        "$(git -C "$MIRROR_REPO" rev-parse refs/tags/v0.1.0)"
fi
printf 'safety bundle: %s\n' "$SAFETY_BUNDLE"
