from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TelemetrySession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver_name = db.Column(db.String(100), nullable=False)
    track = db.Column(db.String(100), nullable=False)
    session_type = db.Column(db.String(50), nullable=False)  # Practice, Qualifying, Race
    lap_number = db.Column(db.Integer, nullable=False)
    tyre_compound = db.Column(db.String(50), nullable=False)
    sector1 = db.Column(db.Float, nullable=False)
    sector2 = db.Column(db.Float, nullable=False)
    sector3 = db.Column(db.Float, nullable=False)
    top_speed = db.Column(db.Float, nullable=False)
    weather = db.Column(db.String(50), nullable=False)

    @property
    def lap_time(self):
        return round(self.sector1 + self.sector2 + self.sector3, 3)

    def to_dict(self):
        return {
            "id": self.id,
            "driver_name": self.driver_name,
            "track": self.track,
            "session_type": self.session_type,
            "lap_number": self.lap_number,
            "tyre_compound": self.tyre_compound,
            "sector1": self.sector1,
            "sector2": self.sector2,
            "sector3": self.sector3,
            "lap_time": self.lap_time,
            "top_speed": self.top_speed,
            "weather": self.weather,
        }