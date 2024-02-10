from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Players Rankings Test - ODI - T20i'
sheet.append(['Ranking', 'Player', 'Country' 'Rating'])


try:
    response = requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/bowling")
    soup = BeautifulSoup(response.text, 'html.parser')
    Players = soup.find('div', class_='cb-plyr-tbody').find_all('div', class_='cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')
    # Rankin = soup.find('div', class_='cb-plyr-tbody').find_all('div', class_='cb-col cb-col-67 cb-rank-plyr')

    for Player in Players:
        find_player = Player.find('a', class_='text-hvr-underline text-bold cb-font-16').text
        find_rank = Player.find('div', class_='cb-col cb-col-16 cb-rank-tbl cb-font-16').text
        player_country = Player.find('div', class_='cb-font-12 text-gray').text
        player_ratings = Player.find('div', class_='cb-col cb-col-17 cb-rank-tbl pull-right').text
        print(find_rank, '-', find_player,'-', player_country,'-', player_ratings)
        sheet.append([find_rank,find_player,player_country, player_ratings])

except Exception as e:
    print(e)

excel.save("ICC Rankings.xlsx")