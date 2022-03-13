di_roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
            'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
di_arabic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
arabic_numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

illegal_combinations = ['IIV', 'IIX', 'IIL', 'IIC', 'IID', 'IIM', 'XXL',
                        'XXC', 'XXD', 'XXM', 'CCD', 'CCM', 'VVV', 'LLL',
                        'DDD', 'IIV', 'IIX', 'XXL', 'XXC', 'CCD', 'CCM']


def to_arabic(roman):  # M CM XC V    1995
    i, arabic = 0, 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i + 2] in di_roman:
            arabic += di_roman[roman[i:i + 2]]
            i += 2
        else:
            roman[i] in di_roman
            arabic += di_roman[roman[i]]
            i += 1
    return arabic


def to_roman(arabic):  # 1995 ---> 'M CM XC V'
    i = 0
    roman = ''
    while arabic > 0:
        n = arabic_numbers[i]
        while n <= arabic:
            roman += di_arabic[n]
            arabic -= n
        i += 1
    return roman


def print_spaced(li_tuples, field_width=0):
    i = 0
    for el, v in li_tuples:
        print(f'{el :{field_width}} is {v}')
        i += 1
        if i % 5 == 0:
            print()


def run_to_roman_to_arabic_tests(begin=1, end=100, step=1):
    romans = []
    arabics = []
    for el in range(begin, end, step):
        romans.append((el, to_roman(el)))
    print_spaced(romans)

    for k, v in romans:
        arabics.append((v, to_arabic(v)))
    print_spaced(arabics, field_width=10)


def main():
    run_to_roman_to_arabic_tests(begin=10, end=301, step=10)
    # print(to_roman(1975))
    # print(to_arabic('MMCMXCIV'))
    # print(to_arabic('MMCMLXXV'))


if __name__ == '__main__':
    main()

