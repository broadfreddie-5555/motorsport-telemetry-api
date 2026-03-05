# Motorsport Telemetry API

A backend API built with Python and Flask for storing and analysing motorsport telemetry data.

This project simulates a simplified telemetry system used in motorsport to record lap performance data such as sector times, tyre compounds, and top speed.

The API allows telemetry data to be stored, queried, and analysed through REST endpoints.

## Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite
- REST API
- Git / GitHub

## Features

- Store telemetry data for racing drivers
- Retrieve all telemetry laps
- Filter telemetry by driver
- Find the best lap for a specific driver
- JSON-based REST API responses


## API Endpoints

### Home

GET /

Returns API status.

Example response:

{
  "message": "Motorsport Telemetry API is running"
}

### Get All Telemetry

GET /telemetry

Returns all recorded telemetry laps stored in the database.

### Filter Telemetry by Driver

GET /telemetry?driver=Verstappen

Returns telemetry laps for a specific driver.

### Create Telemetry Entry

POST /telemetry

Example request body:

{
  "driver_name": "Verstappen",
  "track": "Silverstone",
  "lap_number": 1,
  "tyre_compound": "Soft",
  "sector1": 27.123,
  "sector2": 28.456,
  "sector3": 26.771,
  "top_speed": 331.2
}

### Get Best Lap

GET /telemetry/best?driver=Verstappen

Returns the fastest lap for the selected driver.

## Running the Project Locally

Clone the repository:

git clone https://github.com/broadfreddie-5555/motorsport-telemetry-api.git

Navigate to the project folder:

cd Motorsport-Telemetry-Project/motorsport-telemetry-api

Install dependencies:

pip install flask sqlalchemy

Run the server:

python app.py

The API will start at:

http://127.0.0.1:5000