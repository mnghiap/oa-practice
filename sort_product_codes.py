from functools import cmp_to_key

def sort_product_codes(order, product_codes):
    def cmp(a, b):
        for i in range(min(len(a), len(b))):
            if order.index(a[i]) < order.index(b[i]):
                return -1
            elif order.index(a[i]) > order.index(b[i]):
                return 1
        # loop is over, one string is prefic of the other
        return len(a) - len(b)

    return sorted(product_codes, key=cmp_to_key(cmp))

print(sort_product_codes("abcdefghijklmnopqrstuvwxyz", ["adc", "abc", "bhafadf", "poip", "lullmfao"]))
