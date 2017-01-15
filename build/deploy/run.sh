#/bin/bash

echo $CI_COMMIT_ID > /dreamsuite_tag
echo -e $PRIVATE_SSH_KEY > /root/.ssh/id_rsa
chmod 400 /root/.ssh/id_rsa

if [ "$CI_BRANCH" = "master" ]
then
  HOST=tinyhandsdreamsuite.org
else
  HOST=staging.tinyhandsdreamsuite.org
fi

echo $CI_BRANCH
echo copy over dreamsuite tag $CI_COMMIT_ID to $HOST
scp -v /dreamsuite_tag thi@$HOST:/home/thi/tinyhands/dreamsuite_tag

echo execute run script
ssh thi@staging.tinyhandsdreamsuite.org 'tinyhands/run.sh'
