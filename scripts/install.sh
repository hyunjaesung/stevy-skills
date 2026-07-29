#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_root="$repo_root/skills"
install_target="${1:-both}"

case "$install_target" in
  codex|claude|both) ;;
  *)
    echo "Usage: $0 [codex|claude|both] [all|skill-name ...]" >&2
    exit 2
    ;;
esac

shift || true
if [[ "$#" -eq 0 || "$1" == "all" ]]; then
  selected_skills=()
  while IFS= read -r skill_dir; do
    selected_skills+=("$(basename "$skill_dir")")
  done < <(find "$skills_root" -mindepth 1 -maxdepth 1 -type d | sort)
else
  selected_skills=("$@")
fi

destinations=()
if [[ "$install_target" == "codex" || "$install_target" == "both" ]]; then
  codex_root="${CODEX_HOME:-$HOME/.codex}"
  destinations+=("$codex_root/skills")
fi
if [[ "$install_target" == "claude" || "$install_target" == "both" ]]; then
  destinations+=("$HOME/.claude/skills")
fi

for skill_name in "${selected_skills[@]}"; do
  source_dir="$skills_root/$skill_name"
  if [[ ! -f "$source_dir/SKILL.md" ]]; then
    echo "Unknown skill: $skill_name" >&2
    exit 2
  fi

  for destination_root in "${destinations[@]}"; do
    destination_dir="$destination_root/$skill_name"
    mkdir -p "$destination_dir"
    cp -R "$source_dir/." "$destination_dir/"
    echo "Installed $skill_name -> $destination_dir"
  done
done
