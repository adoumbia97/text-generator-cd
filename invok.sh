#!/bin/bash
curl -X 'POST' \
  'https://rrurcqhypf.us-east-1.awsapprunner.com/generate/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "https://cor.stanford.edu/curriculum/collections/cor-for-the-history-classroom/"
}'