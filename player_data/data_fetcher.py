import requests
import pandas as pd
import numpy as np

def get_nst_player_data(date):
    base_url = 'https://naturalstattrick.com/playerteams.php'
    params = {
        'fromseason':'20242025',
        'thruseason':'20242025',
        'stype':'2', # Regular season
        'sit':'all',
        'score':'all',
        'stdoi':'std',
        'rate':'y',
        'team':'ALL',
        'pos':'S',
        'loc':'B',
        'toi':'10',
        'gpfilt':'gpdate',
        'fd':date,
        'td':date,
        'tgp':'410',
        'lines':'single',
        'draftteam':'ALL',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                      'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                      'Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(base_url,params=params, headers=headers)

    response.raise_for_status()

    tables = pd.read_html(response.content)

    for df in tables:
        if 'Player' in df.columns:
            df.columns = df.columns.str.strip()

            if 'Unnamed: 0' in df.columns:
                df = df.drop(columns='Unnamed: 0')

            numeric_cols = df.columns.drop(['Player','Team','Position'])
            df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

            # Replace infinite values with NaN
            df[numeric_cols] = df[numeric_cols].replace([np.inf, -np.inf], np.nan)

            # Add the date to the dataframe
            df['Date'] = date

            return df

    print(f"No player data found in the page for date: {date}")
    return pd.DataFrame()