# my-serverless-api

# My Serverless API (AWS Lambda + API Gateway)

A simple cloud-hosted API using AWS Lambda and API Gateway.

## Features

- Serverless deployment (no servers to manage)
- Fast, scalable HTTP endpoint
- Simple Lambda function (edit to add your logic)

## Setup

1. **Clone the repo**


2. **Deploy Lambda**
- Go to AWS Lambda Console
- Create a function, paste code from `src/lambda_function.py`
- Assign the IAM role (`LambdaApiRole`)

3. **Create API Gateway**
- Follow the steps in the [AWS setup](#aws-setup) section above

4. **Deploy and Test**
- Deploy the API to a stage
- Use the Invoke URL to test

## License

MIT
