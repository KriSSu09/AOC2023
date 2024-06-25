with open('input.txt') as f:
    letter_values = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    values = []
    for line in f.readlines():
        first_digit, last_digit = None, None
        for idx, c in enumerate(line):
            if c.isdigit():
                first_digit = c
                break
            for key in letter_values.keys():
                if line.find(key, idx, idx + len(key)) != -1:
                    first_digit = letter_values[key]
                    break
            if first_digit is not None:
                break
        for idx, c in enumerate(line[::-1]):
            if c.isdigit():
                last_digit = c
                break
            for key in letter_values.keys():
                if line[::-1].find(key[::-1], idx, idx + len(key)) != -1:
                    last_digit = letter_values[key]
                    break
            if last_digit is not None:
                break
        values.append(int("".join([str(first_digit), str(last_digit)])))
    print(sum(values))
