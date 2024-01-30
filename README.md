# GPTuesday 'Agents' exploration

The accompanying repo for the GPTuesday 'Agents' event on 1-30-2024

## Setting Python Interpreter...

- poetry env info

## Setting up OPENAI_API_KEY

```.sh
export OPENAI_API_KEY=`sk-***`
```

## Installing the psycopg2-binary

poetry add psycopg2-binary

## Connecting to dockerized PostgreSQL instance

docker run -it --rm --network bridge postgres psql -h 172.17.0.5 -U postgres

## Running the flask server

poetry run flask run -p 5000 --debug

## Testing the agent with a cURL

'''test cURL
curl -XPOST --header "Content-Type: application/json" -d "{\"prompt\":\"What is the greatest country in the history of mankind?\"}" localhost:5000/query_open_ai 
curl -XPOST --header "Content-Type: application/json" -d "{\"prompt\":\"What are the hottest cities in America?\"}" localhost:5000/query_open_ai 
'''

## Test prompts for Agent

Coming soon...