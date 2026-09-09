#!/usr/bin/env bash
# Build docs/<skill>.zip for the claude.ai upload path (Settings → Capabilities → Skills).
# claude.ai expects the skill folder (containing SKILL.md) at the zip root.
# Usage: scripts/build-skill-zip.sh [skill-name]   (default: qme-env-audit)
set -euo pipefail
skill="${1:-qme-env-audit}"
root="$(cd "$(dirname "$0")/.." && pwd)"
[ -f "$root/skills/$skill/SKILL.md" ] || { echo "no skills/$skill/SKILL.md" >&2; exit 1; }
out="$root/docs/$skill.zip"
rm -f "$out"
(cd "$root/skills" && zip -qr -X "$out" "$skill" -x '*/.DS_Store')
echo "wrote $out"; unzip -l "$out"
