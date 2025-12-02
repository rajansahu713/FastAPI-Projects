## First getting started with FastAPI and GraphQL
This is a simple example of how to set up a FastAPI application with GraphQL using Strawberry. 


Run the application:
```bash
uvicorn main:app --reload
```

You can access the GraphQL playground at `http://localhost:8000/graphql`

A UI will open where you can run the following queries:



```graphql
query {
	hello
}
```

This will return:
```json
{
  "data": {
    "hello": "Welcome to FastAPI and GraphQL!"
  }
}
```

Second:
```
query {
	hello(name: "Rajan")
}
```

This will return:
```json
{
  "data": {
    "hello": "Hello, Rajan! Welcome to FastAPI and GraphQL!"
  }
}
```


