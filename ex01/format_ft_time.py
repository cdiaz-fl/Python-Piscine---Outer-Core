import time
from datetime import datetime

# Get the seconds since epoch (January 1, 1970) (this is known as Unix timestamp)
epoch_seconds = time.time()

# Convert the Unix timestamp to a human-readable date
date_format = datetime.fromtimestamp(epoch_seconds).strftime('%b %d %Y')

print(f"Seconds since January 1, 1970: {epoch_seconds:.4f}")
print(date_format)