## Async Movie API service

## Description
This is an API for searching information by movies, persons and genres.

## Instruction
Link to repository: https://github.com/VladOS95-cyber/Async_API_sprint_2

- clone project
    ```
    git clone https://github.com/VladOS95-cyber/Async_API_sprint_2
    ```
- rename the file with environment variables for testing
    ```
    mv envs/.fastapi.env.sample envs/.fastapi.env
    ```
- build Docker containers
    ```
    docker-compose build --no-cache
    ```
- run containers
    ```
    docker-compose up -d
    ```

## Testing
### In a container
- tests run automatically when the container starts. To restart:
    ```
    docker-compose start tests
    ```
### Local
- activate the virtual environment
- install the necessary libraries
    ```
    pip install -r requirements.txt
    ```
- create image according to instruction [above](#Установка)
- run containers
    ```
    docker-compose -f docker-compose_local_test.yml up -d
    ```
- run tests
   ```
   pytest tests
   ```
### Additional features
- viewing logs
    ```
    docker-compose logs -f
    ```

## Usage
### Documentation is available at
-    http://localhost/api/openapi
### Query examples
- get a list of films by genre
    ```
    /api/v1/film?filter[genre]=<comedy-uuid>&sort=-imdb_rating&page[size]=50&page[number]=1
    ```
    ```
    GET /api/v1/film?filter[genre]=<uuid:UUID>&sort=-imdb_rating&page[size]=50&page[number]=1

    [
        {
          "uuid": "524e4331-e14b-24d3-a156-426614174003",
          "title": "Ringo Rocket Star and His Song for Yuri Gagarin",
          "imdb_rating": 9.4
        },
        {
          "uuid": "524e4331-e14b-24d3-a156-426614174003",
          "title": "Lunar: The Silver Star",
          "imdb_rating": 9.2
        },
        ...
    ] 
    ```
- get complete information on the film
    ```
    /api/v1/film/<uuid:UUID>/
    ```
    ```
    {
    "uuid": "b31592e5-673d-46dc-a561-9446438aea0f",
    "title": "Lunar: The Silver Star",
    "imdb_rating": 9.2,
    "description": "From the village of Burg, a teenager named Alex sets out to become the fabled guardian of     the goddess Althena...the Dragonmaster. Along with his girlfriend Luna, and several friends they meet     along the journey, they soon discover that the happy world of Lunar is on the verge of Armageddon. As     Dragonmaster, Alex could save it. As a ruthless and powerful sorceror is about to play his hand, will     Alex and company succeed in their quest before all is lost? And is his girlfriend Luna involved in these     world shattering events? Play along and find out.",
    "genre": [
      {"name": "Action", "uuid": "6f822a92-7b51-4753-8d00-ecfedf98a937"},
      {"name": "Adventure", "uuid": "00f74939-18b1-42e4-b541-b52f667d50d9"},
      {"name": "Comedy", "uuid": "7ac3cb3b-972d-4004-9e42-ff147ede7463"}
    ],
    "actors": [
      {
        "uuid": "afbdbaca-04e2-44ca-8bef-da1ae4d84cdf",
        "full_name": "Ashley Parker Angel"
      },
      {
        "uuid": "3c08931f-6138-46d1-b179-1bd076b6a236",
        "full_name": "Rhonda Gibson"
      },
      ...
    ],
    "writers": [
      {
        "uuid": "1bd9a00b-9596-49a3-afbe-f39a632a09a9",
        "full_name": "Toshio Akashi"
      },
      {
        "uuid": "27fc3dc6-2656-43cb-8e56-d0dfb75ea0b2",
        "full_name": "Takashi Hino"
      },
      ...
    ],
    "directors": [
      {
        "uuid": "4a893a97-e713-4936-9dd4-c8ca437ab483",
        "full_name": "Toshio Akashi"
      },
      ...
    ],
    }
    ```
