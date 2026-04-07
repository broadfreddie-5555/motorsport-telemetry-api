# Motorsport Telemetry & Comparison API

Backend-focused project demonstrating API development, database design, and performance analysis using Python, Flask, and SQLAlchemy.

This project simulates a motorsport telemetry system, allowing storage, retrieval, and analysis of lap performance data across drivers and tracks.

---

## Overview

The system is built as a REST API that enables:

- Storing telemetry data (drivers, tracks, sector times, tyre compounds)
- Retrieving and filtering telemetry records
- Calculating fastest laps based on sector timing
- Comparing driver performance using derived lap time metrics

This project focuses on backend fundamentals including data modelling, API design, validation, and performance-based calculations.

---

## Core Features

### Telemetry API

- Store lap data (driver, track, lap number, tyre compound, sector times, top speed)
- Retrieve all telemetry or filter by driver
- Calculate fastest lap per driver
- Identify fastest lap on a given track

### Telemetry Comparison Engine

- Compare drivers using lap time data
- Calculate performance metrics based on sector-derived lap times
- Query telemetry sessions across tracks
- Return structured performance insights via API endpoints

---

## Example Endpoints

### Get all telemetry

    GET /telemetry

### Filter by driver

    GET /telemetry?driver=Verstappen

### Add telemetry data

    POST /telemetry

Example JSON body:

```json
{
  "driver_name": "Verstappen",
  "track": "Silverstone",
  "lap_number": 3,
  "tyre_compound": "Soft",
  "sector1": 27.05,
  "sector2": 28.41,
  "sector3": 26.69,
  "top_speed": 332.1
}
```

### Get best lap for a driver

    GET /telemetry/best?driver=Hamilton

### Get fastest lap on a track

    GET /track/fastest?track=Monza

---

## Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite
- Git / GitHub

---

## Key Concepts Demonstrated

- REST API design
- Database modelling using SQLAlchemy
- Data validation and error handling
- Querying and filtering database records
- Derived data (lap time calculated from sector times)
- Performance-based sorting and analysis

---

## How to Run

```bash
cd motorsport-telemetry-comparison-api
python app.py
```

---

## Future Improvements

- Driver comparison endpoint enhancements (average lap time, tyre analysis)
- Expanded performance analytics
- Frontend integration for data visualisation
- Deployment to a cloud platform
