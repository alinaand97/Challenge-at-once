# Вызов разом

def apply_all_func(int_list, *functions):
    results = {}
    for items in functions:
        results[items.__name__] = items(int_list)
    return  results



print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))