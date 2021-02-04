
def print_a(results, start_date):
    print("The upswing in Apple stock price started {} and lasted {} measurements.".format(start_date.date(), results))


def print_b(results):
    print("{}\t\t{}\t\t{} ($)".format('date', 'volume', 'price change'))
    print("-------------------------------------------------------")

    for i in results:
        print("{}\t{}\t{}".format(i['date'].date(), i['volume'], round(i['change'], 2)))

def print_c(results):
    print("{}\t\t{} (%)".format('date', 'price change'))
    print("--------------------------------------")
    for i in results:
      print("{}\t{}".format(i['date'].date(), round(i['price_change_percentages'], 2)))