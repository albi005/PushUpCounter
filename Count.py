from datetime import datetime

def save(count):
    with open('log.csv', 'a') as f:
        f.write(format(count))

def format(count):
    return datetime.utcnow().isoformat(timespec='seconds') + ',' + str(count) + '\n'