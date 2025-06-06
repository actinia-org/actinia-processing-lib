#!/usr/bin/env sh

# start valkey server
valkey-server &
sleep 1
valkey-cli ping

TEST_RES=1
if [ "$1" = "dev" ]
then
  echo "Executing only 'dev' tests ..."
  pytest -m 'dev'
  TEST_RES=$?
elif [ "$1" = "integrationtest" ]
then
  pytest -m 'not unittest'
  TEST_RES=$?
else
  pytest
  TEST_RES=$?
fi

# stop valkey server
valkey-cli shutdown

return $TEST_RES
