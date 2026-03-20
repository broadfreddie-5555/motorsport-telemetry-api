from app import app
from models import db, TelemetrySession

SEED_DATA = [
    {
        "driver_name": "Verstappen",
        "track": "Silverstone",
        "session_type": "Qualifying",
        "lap_number": 1,
        "tyre_compound": "Soft",
        "sector1": 27.123,
        "sector2": 28.456,
        "sector3": 26.771,
        "top_speed": 331.2,
        "weather": "Dry",
    },
    {
        "driver_name": "Hamilton",
        "track": "Silverstone",
        "session_type": "Qualifying",
        "lap_number": 1,
        "tyre_compound": "Soft",
        "sector1": 27.340,
        "sector2": 28.620,
        "sector3": 26.910,
        "top_speed": 328.6,
        "weather": "Dry",
    },
    {
        "driver_name": "Norris",
        "track": "Silverstone",
        "session_type": "Qualifying",
        "lap_number": 1,
        "tyre_compound": "Soft",
        "sector1": 27.280,
        "sector2": 28.500,
        "sector3": 26.860,
        "top_speed": 329.8,
        "weather": "Dry",
    },
    {
        "driver_name": "Leclerc",
        "track": "Monza",
        "session_type": "Qualifying",
        "lap_number": 1,
        "tyre_compound": "Soft",
        "sector1": 26.110,
        "sector2": 22.890,
        "sector3": 19.650,
        "top_speed": 357.8,
        "weather": "Dry",
    },
    {
        "driver_name": "Verstappen",
        "track": "Monza",
        "session_type": "Race",
        "lap_number": 14,
        "tyre_compound": "Medium",
        "sector1": 26.430,
        "sector2": 23.120,
        "sector3": 19.940,
        "top_speed": 354.4,
        "weather": "Dry",
    },
]

def seed():
    with app.app_context():
        db.drop_all()
        db.create_all()

        for row in SEED_DATA:
            session = TelemetrySession(**row)
            db.session.add(session)

        db.session.commit()
        print("Seeded telemetry comparison data successfully.")


if __name__ == "__main__":
    seed()