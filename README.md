# googlenews-dashboard
A google news tool for tracking keywords' news over time

## About
This tool takes a list of keywords as input and shows an interactive table which lists articles according to keywords

![screenshot](https://github.com/shirayasur/googlenews-dashboard/blob/main/screenshots/screenshot.jpg)

## How to Use
1. Set up a mySQL database and run `create_db.sql` into a new database named 'news'
2. Plug your mySQL connection string in `config.py` (DB_CONNECTION_STRING)
3. Select the keywords you would like to track and insert them into `config.py` (KEYWORDS)
4. Choose the sites you would like to blacklist and insert them into `config.py` (SITE_BLACKLIST)
5. Create a schedule run for `news_fetch.py` e.g. using [crontab](https://crontab.guru)
6. Run `news_dashboard.py` to activate dashboard (default port is set to 8054)

## Credits
[GoogleNews for python](https://github.com/Iceloof/GoogleNews)


