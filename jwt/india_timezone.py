import datetime
from datetime import timezone, timedelta

# Create a timezone object for Indian Standard Time (UTC+5:30)
indian_timezone = timezone(timedelta(hours=5, minutes=30))

# Get the current UTC time
current_utc_time = datetime.datetime.now(tz=timezone.utc)

# Convert the UTC time to Indian Standard Time
indian_time = current_utc_time.astimezone(indian_timezone)

# Print the Indian Standard Time
print(indian_time)
