def order_weight(strng):
    number_list = sorted(strng.split())
    weight_list = [sum(map(int, number)) for number in number_list]
    zipped_lists = zip(weight_list, number_list)
    ordered_list = [number for weight, number in sorted(zipped_lists)]
    return ' '.join(ordered_list)
