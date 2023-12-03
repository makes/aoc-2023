digit_map = {
    '1': 1, '2': 2, '3': 3,
    '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9,
    'one': 1, 'two': 2, 'three': 3, 
    'four': 4, 'five': 5, 'six': 6,
    'seven': 7, 'eight': 8, 'nine': 9
}

def find_any(s, l, which='first'):
    """Find from string s the first or last occurrence of any string in l."""
    index = -1
    found_item = ""
    for item in l:
        if which == 'first':
            i = s.find(item)
            if i == -1:
                continue
            if i < index or index < 0:
                index = i
                found_item = item
        elif which == 'last':
            i = s.rfind(item)
            if i == -1:
                continue
            if i > index:
                index = i
                found_item = item
        else:
            raise ValueError(f"Invalid search direction which={which}.")
    return index, found_item

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    sum = 0
    for l in lines:
        sum += 10 * digit_map[find_any(l, digit_map, which='first')[1]]
        sum += digit_map[find_any(l, digit_map, which='last')[1]]
    print(sum)

