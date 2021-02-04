

## Stock analyzer

#### Data used
Sample file = appleStock.csv ( apple stock data )

#### Flags
  -sd, start date\
  -ed, end date\
  -o, operation

#### Operations
The program can perform three different tasks:\
  A, a = The longest bullish (upward) trend within a given date range\
  B, b = List of dates, volumes and price changes. The list is ordered by
volume and price change.\
  C, c = List of dates and price change percentages. The list is ordered by
price change percentages.


#### Run program
1. `docker build -t <tag_name> .` 
2. `docker run -it <tag_name> -sd=<dd.mm.yyyy> -ed = <dd.mm.yyyy> -o=<a, b, c>`  

example:
1. `docker build -t stock_analyzer .`
2. `docker run -it stock_analyzer -sd=1.12.2018 -ed=11.1.2020> -o=B`

