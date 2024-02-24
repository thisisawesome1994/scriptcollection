1. Install docker, and run the following build command:

docker build -t investmentcalculator .

2. Start Container:

docker run -d --name=investmentcalculator -p 5000:5000 --restart=always investmentcalculator

Note: You can change the forwarded port by changing the first 5000 to a different port number...