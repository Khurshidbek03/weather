# Weather Information Microservice

## Project Introduction

This project is a Django microservice that collects and stores weather data. The weather data is updated every 10 minutes and stored in a PostgreSQL database.

## Requirements

- Python 3.8 or higher
- PostgreSQL
- Django 4.x
- Django Rest Framework
- `psycopg2-binary`

## External API

The project uses the [FREE WEATHER API](https://www.weatherapi.com/) to get weather data. This API allows you to retrieve real-time weather information.

## API Documentation

### CRUD API

#### Adding Weather Information

- **URL:** `/weather/`
- **Method:** `POST`
- **Description:** Creates new weather data.
- **Request Body:**
  ```json
  {
    "city": "City Name",
    "temperature": 25,
    "humidity": 60,
    "description": "Clear sky",
    "timezone": "UTC",
    "timestamp": "2024-09-01T12:00:00Z"
  }

- **URL:** `/weather/`
- **Method:** `GET`
- **Description:** Gets weather information.
- **Request Body:**
  ```json
  {
    "city": "City Name",
    "temperature": 25,
    "humidity": 60,
    "description": "Clear sky",
    "timezone": "UTC",
    "timestamp": "2024-09-01T12:00:00Z"
  }


- **URL:** `/weather/<id>/`
- **Method:** `PUT`
- **Description:** Updates data.
- **Request Body:**
  ```json
  {
    "city": "Updated City",
    "temperature": 26,
    "humidity": 55,
    "description": "Partly cloudy",
    "timezone": "UTC",
    "timestamp": "2024-09-01T12:30:00Z"
  }

- **URL:** `/weather/<id>/`
- **Method:** `DELETE`
- **Description:** Deletes data.


