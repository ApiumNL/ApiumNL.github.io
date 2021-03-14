if [[ $# -eq 0 ]]; then
    echo 'Missing commit message.'
    exit 0
fi

# Ensure we're on src and commit source files.
git checkout src
git add --all
git commit -m "[Source] $1"

# Build assets
rm -rf dist
mkdir dist

source make_pages.sh
cp README.md dist/README.md

# Deploy to main
pipenv run ghp-import -n -b main -m "[Assets] $1" dist
