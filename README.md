# stock_changes_german_news
Another project on stock price changes using news in german
## Contents
* folder "telegram_parser" contains a .py code which scrapes our news data in real time
* file "german_news_EDA.ipynb" fransforms raw data into more convenient and do EDA (only on NEWS)
* file "prices_EDA.ipynb" downloades raw data for each company and do some graphs for EDA
* file "EDA reddit news.ipynb" fransforms raw data into more convenient and do EDA (NEWS) and comes to the conclusion that this data is not enough
## Data
You can find the data we used by the following link
https://drive.google.com/drive/folders/1iYTfCtGxxwqtZiHwnPGdvTE1YnG_Ck2N?usp=drive_link
* channel_messages.json and channel_messages_1.json contain raw news data from German Wallspapers
* companies_new.xlsx contains prices on stocks for our chosen companies
* RedditNews.csv contins raw news data from r/worldnews on Reddit

## Milestone 3
* We tried to use both news data from **Telegram** and **Reddit**. Turned out that Reddit data is not suitable for our analysis since there is a really limited number of news about each of the chosen german companies. You can see the EDA for both news data sources in notebooks **"german_news_EDA.ipynb"** (for Telegram) and **"EDA reddit news.ipynb"** (for Reddit)
* We did EDA for both **daily** and **weekly** prices for stocks of corresponding germany companies. It is now not obvious which prices data sample we should use for our analysis so we'll try to use both
* **Further steps:** we want to join prices and news datasets and try to see how negative/positive news affects stock price changes. After it is done, we'll try to convert news data into TF-IDF matrics and run some predictive models. IF we have time, we also want to check if the predictions **with** news are more powerful comparing to the predictions **without** news.
