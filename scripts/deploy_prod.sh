cd ..

pip freeze > requirements.txt
git add .
git commit -m "Commit production"
git push origin main

ssh -i C:/Users/bulld/.ssh/id_rsa root@159.65.112.23  'cd ~/production/LabEnv/scripts && sh build.sh'