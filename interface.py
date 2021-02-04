import calculation
import print_results

def A(s, e):
  result, ed = calculation.longest_bullish(s, e)
  print_results.print_a(result, ed)

def B(s, e):
  result = calculation.greatest_price_change(s, e)
  print_results.print_b(result)

def C(s, e):
  result = calculation.calculate_sma(s, e)
  print_results.print_c(result)
