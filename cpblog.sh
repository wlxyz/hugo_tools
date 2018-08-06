#!/bin/sh
echo "start"
echo "hugo -s myblog"

hugo -s myblog/ --baseUrl="https://wlxyz.github.io/" --theme=maupassant

echo "copy from myblog/public/ to wlxyz.github.io/"
cp -r myblog/public/* wlxyz.github.io/

cd wlxyz.github.io/
echo "add and commit"
git add *
git commit

echo "committed"
