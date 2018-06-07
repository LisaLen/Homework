melon_cost = 1.00
def melon_paid(fname):
    fhand = open(fname)
    for line in fhand:
        line = line.rstrip()
        word = line.split('|')
        customer_name = word [1]
        customer_melons = float(word[2])
        customer_paid = float(word[3])
        customer_expected = customer_melons * melon_cost
        if customer_expected != customer_paid:
            print(customer_name, "paid {:.2f}, expected {:.2f}".format(customer_paid, customer_expected))


melon_paid('customer-orders.txt')