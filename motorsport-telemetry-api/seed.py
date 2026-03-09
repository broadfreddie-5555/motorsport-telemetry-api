from app import app
from models import db, Telemetry

SEED_ROWS = [
    # Silverstone
    dict(driver_name="Verstappen", track="Silverstone", lap_number=1, tyre_compound="Soft", sector1=27.123, sector2=28.456, sector3=26.771, top_speed=331.2),
    dict(driver_name="Verstappen", track="Silverstone", lap_number=2, tyre_compound="Soft", sector1=27.050, sector2=28.410, sector3=26.690, top_speed=332.1),
    dict(driver_name="Hamilton",   track="Silverstone", lap_number=1, tyre_compound="Soft", sector1=27.340, sector2=28.620, sector3=26.910, top_speed=328.6),
    dict(driver_name="Hamilton",   track="Silverstone", lap_number=2, tyre_compound="Soft", sector1=27.210, sector2=28.590, sector3=26.840, top_speed=329.4),
    dict(driver_name="Norris",     track="Silverstone", lap_number=1, tyre_compound="Medium", sector1=27.280, sector2=28.610, sector3=26.880, top_speed=330.0),

    # Spa
    dict(driver_name="Verstappen", track="Spa", lap_number=1, tyre_compound="Medium", sector1=34.220, sector2=45.880, sector3=32.410, top_speed=346.9),
    dict(driver_name="Leclerc",    track="Spa", lap_number=1, tyre_compound="Soft", sector1=34.510, sector2=46.020, sector3=32.600, top_speed=344.2),
    dict(driver_name="Norris",     track="Spa", lap_number=1, tyre_compound="Medium", sector1=34.430, sector2=45.990, sector3=32.520, top_speed=345.1),

    # Monza
    dict(driver_name="Leclerc",    track="Monza", lap_number=1, tyre_compound="Soft", sector1=26.110, sector2=22.890, sector3=19.650, top_speed=357.8),
    dict(driver_name="Hamilton",   track="Monza", lap_number=1, tyre_compound="Medium", sector1=26.220, sector2=22.940, sector3=19.720, top_speed=356.1),
]

def seed():
    with app.app_context():
        existing = Telemetry.query.count()
        if existing > 0:
            print(f"Database already has {existing} telemetry rows. Not seeding.")
            print("If you want to reseed: delete instance/telemetry.db then restart app and rerun seed.py")
            return

        for row in SEED_ROWS:
            t = Telemetry(
                driver_name=row["driver_name"],
                track=row["track"],
                lap_number=int(row["lap_number"]),
                tyre_compound=row["tyre_compound"],
                sector1=float(row["sector1"]),
                sector2=float(row["sector2"]),
                sector3=float(row["sector3"]),
                top_speed=float(row["top_speed"]),
            )
            db.session.add(t)

        db.session.commit()
        print(f"Seeded {len(SEED_ROWS)} telemetry rows.")

if __name__ == "__main__":
    seed()