#!/bin/bash

old=$(git tag | awk '/./{line=$0} END{print line}')

if [ $# = 0 ] || [ $# -ge 2 ]; then
    echo "Error: Please add the version number you want to update to"
    echo "Example:"
    echo "    ./scripts/update.sh X.Y.Z"
    exit 1;
fi


echo "The old version was: $old"

echo "You want to update to $1"

read -p "Are you sure that is the right version number? " -n 1 -r
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
fi

if [[ ! $(grep -q "$1" setup.py && echo $?) ]]
then
	echo $1
    sed -i '' 's/'"$old"'/'"$1"'/g' setup.py

    echo "Error: $1 not found in setup.py. I just replaced it, please commit and push then start this script again"
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
fi
echo
if [[ ! $(grep -q "$1" IntraPy/__init__.py && echo $?) ]]
then
    sed -i '' 's/'"$old"'/'"$1"'/g' IntraPy/__init__.py

    echo "Error: $1 not found in IntraPy/__init__.py. I just replaced it, please commit and push then start this script again"
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
fi


echo "\n\nDid you commit and pushed your last changes ? The last commit found is:"
git log | head -n 5
read -p "Is that ok? " -n 1 -r
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
fi


if [ ! -f ~/.pypirc ]; then
    echo "pypirc file not found in $HOME !"
    exit 1
fi

read -p "Are you sure you want to do this ? $old -> $1\n This is your last chance" -n 1 -r
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
fi

last_commit_message=$(git log | head -n 5 | tail -n 1 | awk '$1=$1')

read -p "Do you want to use the last commit message ?" -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
    git tag $1 -m $last_commit_message
else
    echo -n "Please enter the message you'd like to use for the tag"
    read user_commit_message
    git tag $1 $user_commit_message
fi



git push --tags origin master
python setup.py register sdist upload




















