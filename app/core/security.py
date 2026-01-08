from datetime import datetime, timedelta, timezone

def utcnow() -> datetime:
    """Return current UTC time as timezone-naive datetime for database compatibility."""
    return datetime.now(timezone.utc).replace(tzinfo=None)