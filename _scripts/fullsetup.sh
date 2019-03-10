DEFAULT_TTL=${1-30}

./scripts/setup.sh
./scripts/configdb.sh $DEFAULT_TTL
./scripts/createuser.sh
