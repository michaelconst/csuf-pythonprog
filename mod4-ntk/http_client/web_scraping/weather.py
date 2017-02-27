import requests
from bs4 import BeautifulSoup
import pandas as pd


# geo-location for Fullerton, CA
URL = "http://forecast.weather.gov/MapClick.php?lat=33.8703&lon=-117.9253"


def scrape(url):
    page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
    soup = BeautifulSoup(page.content, 'html.parser')
    seven_day = soup.find(id="seven-day-forecast")
    period_tags = seven_day.select(".tombstone-container .period-name")
    periods = [pt.get_text() for pt in period_tags]
    short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
    temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
    descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

    wheather_data = pd.DataFrame(
        {
            "desc": descs,
            "period": periods,
            "short_desc": short_descs,
            "temp": temps
        }
    )
    return wheather_data


def main():
    print(scrape(URL))


if __name__ == '__main__':
    main()