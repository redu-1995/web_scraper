from bs4 import BeautifulSoup
import requests
from telegram import Bot
import asyncio  

bot_token = "6768782528:AAExptoutbM0qhbhLwhiEymandyyvsC19sU"
bot = Bot(token=bot_token)

async def send_data_to_telegram_bot(data):
    chat_id = "-1001997214271"
    await bot.send_message(chat_id, data)


def scrape_and_send_data():
    url = 'https://harmeejobs.com/jobs/' 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

  
    data_div = soup.find('div', class_='job_listings')
    data_ul = data_div.find('ul', class_ ='job_listings job-list full grid-layout new-layout')

    data = data_ul.text if data_div else 'No data found'

    asyncio.run(send_data_to_telegram_bot(data))

if __name__ == "__main__":
    scrape_and_send_data()