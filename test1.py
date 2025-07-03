import requests
import time
import datetime

def fetch_time_info():
    url = "https://yandex.com/time/sync.json?geo=213"
    response = requests.get(url)
    data = response.json()
    deltas = []

    for i in range(5):

        end = time.time()  

        timestamp = data['time']
        if timestamp > 1e10:
            timestamp = timestamp / 1000

        tz_offset_seconds = int(data['clocks']['213']['offset']) / 1000

        dt_utc = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)

        tz_local = datetime.timezone(datetime.timedelta(seconds=tz_offset_seconds))
        dt_local = dt_utc.astimezone(tz_local)

        print(f"\nTimestamp (сек): {timestamp}")
        print(f"UTC время: {dt_utc.strftime('%Y-%m-%d %H:%M:%S')} (UTC)")
        print(f"Локальное время: {dt_local.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Временная зона: {data['clocks']['213']['offsetString']}")

        delta = abs(end - timestamp)
        deltas.append(delta)
        print(f"Дельта времени: {delta:.6f} сек.")

    average_delta = sum(deltas) / len(deltas)
    print(f"\nСредняя дельта: {average_delta:.6f} сек.")

if __name__ == "__main__":
    fetch_time_info()