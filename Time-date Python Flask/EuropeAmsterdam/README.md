1. Install docker, and run the following build command:

docker build -t timedateamsterdam .

2. Start Container:

docker run -d --name=timedateamsterdam -p 9001:5000 --restart=always timedateamsterdam

Note: You can change the forwarded port by changing the first 5000 to a different port number...
