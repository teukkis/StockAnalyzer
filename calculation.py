import csv
import datetime
from itertools import islice
import sys

# read the csv file into a list of dictionarys
# edit all the fields for further processing
def read_file(start_date, end_date):
  with open("appleStock.csv", "r") as infile:
    reader = csv.reader(infile, delimiter=',')

    stock_information = []

    # form a list of dictionaries
    # convert strings to numbers
    for row in islice(reader, 1, None):
      d = {
        'date': datetime.datetime.strptime(str(row[0]), '%m/%d/%Y'),
        'close_price': float(row[1].replace('$', '')),
        'volume': int(row[2]),
        'open_price': float(row[3].replace('$', '')),
        'highest_price': float(row[4].replace('$', '')),
        'lowest_price': float(row[5].replace('$', ''))
      }
      
      # add only dates withing given dates
      a = d.copy()
      if a['date'] >= start_date and a['date'] <= end_date:
        stock_information.append(a)
      
    return stock_information


# return the max amount of days the stock price was increasing in a row, and the end date
def longest_bullish(start_date, end_date):
  stock_information = read_file(start_date, end_date)
  
  try:
    tomorrow_price = stock_information[0]['close_price']
  except IndexError as e:
    print("No results for the time range {} - {}".format(start_date.strftime('%d.%m.%Y'), end_date.strftime('%d.%m.%Y')))
    sys.exit()

  record = 1  # contains the number of days the stock price has increased
  counter = 1 # keeps track of the upswing
  sd = ""     # start date of record upswing

  # start from the second item
  # find out the longest upswing
  for row in islice(stock_information, 1, None):

    if row['close_price'] > tomorrow_price:
      counter = 1
    else: 
      counter = counter + 1
    if counter >= record:
      record = counter
      sd = row['date']
    
    tomorrow_price = row['close_price']

  

  return record, sd


#return a list containing the greates price change within a day
def greatest_price_change(start_date, end_date):
  stock_information = read_file(start_date, end_date)

  try:

    # calculate the greatest price change of the day
    for row in stock_information:
      abs_change = abs(row['highest_price'] - row['lowest_price']) 
      row['change'] = abs_change

    # order the list by volume, and then change
    ordered_by_volume_and_change = sorted(stock_information, key=lambda i: (i['volume'], i['change']), reverse=True)
  except IndexError as e:
    print(e)

  return ordered_by_volume_and_change


#return a list containing difference of SMA-5 percentage and a close_price of the day
def calculate_sma(start_date, end_date):
  stock_information = read_file(start_date, end_date)

  try:
    # calculate the average of the last five days
    for index, x in enumerate(stock_information):
      
      temp_list = []
      for y in islice(stock_information, index+1, index+6):
        temp_list.append(y['close_price'])

      if len(temp_list) < 5:
         x['price_change_percentages'] = 0

      else:
        avg = sum(temp_list) / len(temp_list)
        difference = (1 - ( x['open_price'] / avg ) ) * 100
        x['price_change_percentages'] = difference

    ordered_by_price_change_percentages = sorted(stock_information, key=lambda i: (i['price_change_percentages']), reverse=True)

  except IndexError as e:
    print(e)

  except ZeroDivisionError as e:
    print(e)

  return ordered_by_price_change_percentages

