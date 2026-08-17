#!/bin/sh
set -eu

pages_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
workspace_dir=$(dirname "$pages_dir")
landing_dir=$(mktemp -d)
trap 'rm -rf "$landing_dir"' EXIT HUP INT TERM

usage() {
    cat <<EOF
Usage: $(basename "$0") PROJECT

Build and publish one Sphinx project to GitHub Pages.

Available projects:
  mathematics
  contests
  cryptography
  game-programming
EOF
}

if [ "$#" -ne 1 ]; then
    usage >&2
    exit 2
fi

case $1 in
    mathematics|contests|cryptography|game-programming)
        project=$1
        ;;
    -h|--help)
        usage
        exit 0
        ;;
    *)
        printf 'Unknown project: %s\n\n' "$1" >&2
        usage >&2
        exit 2
        ;;
esac

build_site() {
    site_name=$1
    source_dir="$workspace_dir/$site_name"
    output_dir="$source_dir/_build/html"

    sphinx-build -E -b html -d "$source_dir/_build/doctrees" \
        -W --keep-going "$source_dir" "$output_dir"
    mkdir -p "$pages_dir/$site_name"
    rsync -a --delete --exclude .doctrees/ "$output_dir/" "$pages_dir/$site_name/"
}

sphinx-build -E -b html -d "$landing_dir/doctrees" -W --keep-going \
    "$pages_dir/site-src" "$landing_dir/html"
rsync -a --exclude .doctrees/ "$landing_dir/html/" "$pages_dir/"

build_site "$project"

touch "$pages_dir/.nojekyll"
