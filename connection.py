import requests
import json
import pandas as pd

#returns JSON response from api with custom extention to URL
def get_json(extention):
    endpoint = f'https://covid19-api.org/api/{extention}'
    req = requests.get(endpoint)
    return json.loads(req.text)

### JSON returns ###

#returns JSON all time data about a country
def status(country):
    return get_json(f'status/{country}')

#returns JSON all time data about a country from a specific date (formatted YYYY-MM-DD)
def status_date(country, date):
    return get_json(f'status/{country}?date={date}')

#returns JSON latest daily data for a country
def latest(country):
    return get_json(f'diff/{country}')

#returns JSON list of supported countries and their acronyms
def countries():
    return get_json('countries')

#returns JSON of total stats every day since february 5 2020
def timeline(country):
    return get_json(f'timeline/{country}')

### PANDAS returns ###

#returns df of total case count since february 5 2020
def cases_alltime_pd(country):
    cases = [i['cases'] for i in timeline(country)]
    data = {'dates' : dates(), 'cases' : cases}
    return pd.DataFrame(data = data)

#returns df of total death count since february 5 2020
def deaths_alltime_pd(country):
    deaths = [i['deaths'] for i in timeline(country)]
    data = {'dates' : dates(), 'deaths' : deaths}
    return pd.DataFrame(data = data)

def cases_deaths_pd(country):
    cases = [i['cases'] for i in timeline(country)]
    deaths = [i['deaths'] for i in timeline(country)]
    data = {'dates' : dates(), 'cases' : cases, 'deaths' : deaths}
    return pd.DataFrame(data = data)

### SINGLE returns ###

#returns today's case count
def cases(country):
    return get_json(f'diff/{country}')['new_cases']

#returns today's death count
def deaths(country):
    return get_json(f'diff/{country}')['new_deaths']

#returns the list of dates spanning from february 5 2020 to today
def dates():
    return [i['last_update'][:10] for i in timeline('us')]


if __name__ == '__main__':
    cases_deaths_pd('us').to_csv('dataaa.csv')
