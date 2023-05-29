# date and time

from datetime import datetime, timedelta
# timedelta хранит секунды, дни, микросекунды

# С какого до какого года 32-битная Unix-эпоха?
dt0 = datetime(1970, 1, 1)

seconds_max = 2**35

dtmin = dt0 - timedelta(seconds=seconds_max)
dtmax = dt0 + timedelta(seconds=seconds_max)
print(dtmin, dtmax)
