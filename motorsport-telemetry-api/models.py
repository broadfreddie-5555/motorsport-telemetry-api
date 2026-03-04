from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from datetime import datetime

class Telemetry(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # context
    driver_name = db.Column(db.String(100), nullable=False)
    track = db.Column(db.String(100), nullable=False)
    lap_number = db.Column(db.Integer, nullable=False)
    tyre_compound = db.Column(db.String(20), nullable=False)

    # telemetry
    sector1 = db.Column(db.Float, nullable=False)
    sector2 = db.Column(db.Float, nullable=False)
    sector3 = db.Column(db.Float, nullable=False)
    top_speed = db.Column(db.Float, nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @property
    def lap_time(self):
        # derived (not stored)
        return round(self.sector1 + self.sector2 + self.sector3, 3)

    def to_dict(self):
        return {
            "id": self.id,
            "driver_name": self.driver_name,
            "track": self.track,
            "lap_number": self.lap_number,
            "tyre_compound": self.tyre_compound,
            "sector1": self.sector1,
            "sector2": self.sector2,
            "sector3": self.sector3,
            "lap_time": self.lap_time,      # derived
            "top_speed": self.top_speed,
            "created_at": self.created_at.isoformat() + "Z"
        }