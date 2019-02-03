#!/bin/sh
echo "start"
echo "hugo -s myblog"

hugo -s myblog/ --baseUrl="https://wlxyz.github.io/" --theme=maupassant

echo "fix image path by hugoImgPath.py"
python3 hugoImgPath.py

echo "copy from myblog/public/ to wlxyz.github.io/"
cp -r myblog/public/* wlxyz.github.io/

cd wlxyz.github.io/
echo "add and commit"
git add *
git commit

echo "committed"
echo "input 'git push'"
