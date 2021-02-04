import argparse
import pprint
import datetime
import sys
from typing import Sequence
from typing import Optional
from argparse import RawTextHelpFormatter

import interface

# Handle commandline input
def main(argv: Optional[Sequence[str]] = None) -> int:
  parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)

  # Start date from commanline input
  parser.add_argument(
    '-sd', '--start_date', 
    help='set the start date',
    type=lambda s: datetime.datetime.strptime(s, '%d.%m.%Y')
    )

  # End date from commanline input
  parser.add_argument(
    '-ed', '--end_date', 
    help='set the end date',
    type=lambda s: datetime.datetime.strptime(s, '%d.%m.%Y')
    )

  # function from commanline input
  parser.add_argument(
    '-o','--operation',
    choices=['A','B','C','a','b','c'],
    help='Choose the operation: \n\tA: gives you the longest streak \n\tB something else \n\tC lkjlk'
    )

  args = vars(parser.parse_args(sys.argv[1:]))
  s, e, o = args['start_date'], args['end_date'], args['operation']

  if validate_dates(s, e):
    call_operations(s, e, o)

  else:
    print('You need to pick correct time range')

  return 0


def validate_dates(start_date, end_date):

  try:
    # check that the date is smaller than the current date
    if datetime.datetime.today() < start_date:
      return False

    # check that start_date is smaller than end_date
    if start_date > end_date:
      return False
  except TypeError as e:
    print("Non-valid dates (-sd and -ed)")
    sys.exit()

  return True


def call_operations(s, e, o):  
  try:
    cases = {
      'A': lambda: interface.A(s, e),
      'a': lambda: interface.A(s, e),
      'B': lambda: interface.B(s, e),
      'b': lambda: interface.B(s, e),
      'C': lambda: interface.C(s, e),
      'c': lambda: interface.C(s, e),
    }
    cases[o]()
  
  except KeyError as e:
    print("Choose the operation ( -o or -O)")
    sys.exit()

if __name__ == "__main__":
  exit(main())
