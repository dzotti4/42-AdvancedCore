import time
from datetime import datetime

seconds = time.time()
now = datetime.now()

print(f"Seconds since January 1, 1970: {seconds:,.4f} "
      f"or {seconds:.2e} in scientific notation")
print(now.strftime("%b %d %Y"))
