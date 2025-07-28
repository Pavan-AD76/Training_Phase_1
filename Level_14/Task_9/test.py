from match import CricketSeries, CricketSeriesList

example_data = [
    {"year": "2020", "series_type": "ODI", "series_name": "India vs Australia", "series_href": "https://www.cricbuzz.com/india-vs-australia-2020"},
    {"year": "2021", "series_type": "Test", "series_name": "England vs India", "series_href": "https://www.cricbuzz.com/england-vs-india-2021"}
]

cricket_series_list = CricketSeriesList(series=example_data)


for series in cricket_series_list.series:
    print(f"Year: {series.year}")
    print(f"Series Type: {series.series_type}")
    print(f"Series Name: {series.series_name}")
    print(f"Series Link: {series.series_href}")
    print("-" * 40) 