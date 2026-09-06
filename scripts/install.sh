#!/usr/bin/env bash
set -euo pipefail

# Codex Meat Proxy - Skills Installer
# Symlinks or copies skills into your local Codex skills directory (~/.codex/skills).

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills"
TARGET_DIR="${CODEX_SKILLS_DIR:-$HOME/.codex/skills}"

MODE="link" # default to symlink

for arg in "$@"; do
  case "$arg" in
    --copy)
      MODE="copy"
      ;;
    --link)
      MODE="link"
      ;;
    --help|-h)
      echo "Usage: $0 [--link | --copy]"
      echo "  --link : Create symbolic links to skills in $TARGET_DIR (default)"
      echo "  --copy : Copy skill folders into $TARGET_DIR"
      exit 0
      ;;
    *)
      echo "Unknown option: $arg"
      exit 1
      ;;
  esac
done

echo "=========================================="
echo "Codex Meat Proxy - Skill Installer"
echo "=========================================="
echo "Source: $SKILLS_DIR"
echo "Target: $TARGET_DIR"
echo "Mode:   $MODE"
echo ""

# 1. Validate skills first
echo "--> Validating skills before install..."
if command -v python3 &>/dev/null; then
  python3 "$SCRIPT_DIR/validate.py"
else
  echo "Python 3 not found, skipping validation."
fi
echo ""

# 2. Ensure target directory exists
mkdir -p "$TARGET_DIR"

# 3. Install each skill
echo "--> Installing skills..."
COUNT=0
for skill_path in "$SKILLS_DIR"/*; do
  [ -d "$skill_path" ] || continue
  skill_name="$(basename "$skill_path")"
  dest_path="$TARGET_DIR/$skill_name"

  if [ "$MODE" = "link" ]; then
    if [ -L "$dest_path" ]; then
      rm -f "$dest_path"
    elif [ -d "$dest_path" ]; then
      echo "  [SKIP] $skill_name already exists as a non-symlink directory in target. Use --copy or remove manually."
      continue
    fi
    ln -s "$skill_path" "$dest_path"
    echo "  [LINK] $skill_name -> $dest_path"
  else
    rm -rf "$dest_path"
    cp -R "$skill_path" "$dest_path"
    echo "  [COPY] $skill_name -> $dest_path"
  fi
  COUNT=$((COUNT + 1))
done

echo ""
echo "Successfully installed $COUNT skills to $TARGET_DIR."
echo "Restart or reload your Codex agent to detect new skills."
