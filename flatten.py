def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # Eğer item bir listeyse, içindekileri düzleştirip ekler.
        else:
            flat_list.append(item)  # Eğer liste değilse direkt ekler.
    return flat_list

# Test
input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output_list = flatten(input_list)
print(output_list)

def reverse_list(lst):
    reversed_list = []
    for item in reversed(lst):  # Önce listeyi tersine çeviriyoruz.
        if isinstance(item, list):
            reversed_list.append(reverse_list(item))  # Eğer item bir listeyse, o listeyi de tersine çeviriyoruz.
        else:
            reversed_list.append(item)  # Eğer liste değilse direkt ekliyoruz.
    return reversed_list

# Test
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_list(input_list)
print(output_list)
