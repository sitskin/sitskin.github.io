call pelpub.bat
git add -A
git commit -m "Deploying changes"
git push origin source
pushd output
git init
git add .
git commit -m "Deploying changes"
git remote add origin https://github.com/sitskin/sitskin.github.io.git
git push origin master --force
popd

