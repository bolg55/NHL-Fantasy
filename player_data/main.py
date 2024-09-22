from data_fetcher import get_nst_player_data
from config import YEAR
from db_utils import create_db_engine
import pandas as pd
from datetime import datetime, timedelta
import pickle
import os

def load_game_dates(year):
    cache_file = 'game_dates.pkl'
    if os.path.exists(cache_file):
        with open(cache_file, 'rb') as f:
            game_dates = pickle.load(f)
        print("Loaded game dates from cache")
    else:
        dates_url = f"https://www.hockey-reference.com/leagues/NHL_{year}_games.html"
        dfs = pd.read_html(dates_url)
        df = dfs[0]
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        game_dates = df['Date'].dt.date.dropna().unique()
        with open(cache_file, 'wb') as f:
            pickle.dump(game_dates, f)
        print("Fetched and cached game dates")
    return game_dates

def main():
    # Set the season year
    year = YEAR

    # Load game dates
    game_dates = load_game_dates(year)

    # Determine the target date (e.g., yesterday)
    target_date = datetime.now() - timedelta(days=1).date()

    # Check if the target date is in the list of game dates
    if target_date in game_dates:
        date_str = target_date.strftime('%Y-%m-%d')
        player_data = get_nst_player_data(date_str)
        if not player_data.empty:
            engine = create_db_engine()

            try:
                player_data.to_sql('player_data', con=engine, if_exists='append', index=False)
                print(f"Successfully inserted data for {date_str}")
            except Exception as e:
                print(f"Failed to insert data for {date_str}")
                print(e)
        else:
            print(f"No data found for {date_str}")
    else:
        print(f"No game data available for {target_date}")

if __name__ == '__main__':
    main()
