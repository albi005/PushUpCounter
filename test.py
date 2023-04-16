from datetime import datetime
import dateutil.tz

utc = datetime.now(dateutil.tz.tzutc())
print('UTC TIME: ' + str(utc))

local = utc.astimezone(dateutil.tz.tzlocal())
print('Local TIME: ' + str(local))