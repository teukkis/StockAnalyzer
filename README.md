

## Stock analyzer

#### Data used
Sample file = appleStock.csv ( apple stock data )

#### Flags
  -sd, start date\n
  -ed, end date
  -o, operation

#### Operations
The program can perform three different tasks:
  A, a = The longest bullish (upward) trend within a given date range
  B, b = List of dates, volumes and price changes. The list is ordered by
volume and price change.
  C, c = List of dates and price change percentages. The list is ordered by
price change percentages.


#### Run program
docker build -t <tag_name> . 
  && docker run -it <tag_name> -sd=<dd.mm.yyyy> -ed=<dd.mm.yyyy> -o=<operation>

example:
  docker build -t stock_analyzer . 
    && docker run -it stock_analyzer -sd=1.12.2016 -ed=11.1.2020> -o=B

