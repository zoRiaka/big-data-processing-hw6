docker build --network=host -t hw6 .
docker run --name kafka-producer --network kafka-network --rm hw6

