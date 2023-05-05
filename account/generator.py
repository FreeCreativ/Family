from django.utils import timezone

alphabetDictionary = {
    "A": 222,
    "B": 308,
    "C": 449,
    "D": 330,
    "E": 667,
    "F": 228,
    "G": 882,
    "H": 447,
    "I": 193,
    "J": 664,
    "K": 732,
    "L": 885,
    "M": 154,
    "N": 180,
    "O": 176,
    "P": 159,
    "Q": 198,
    "R": 154,
    "S": 290,
    "T": 110,
    "U": 289,
    "V": 132,
    "W": 264,
    "X": 220,
    "Y": 286,
    "Z": 242,
    " ": 289,
    "@": 126,
    "*": 235,
    "#": 222,
    "'": 334,
    ":": 421,
    ",": 256,
    "-": 892,
    "_": 875,
    "+": 987,
}
number_dictionary1 = {
    '1': "z",
    '2': "j",
    '3': "p",
    '4': "c",
    '5': "f",
    '6': "w",
    '7': "u",
    '8': "n",
    '9': "r",
    '0': "t",
    '-': "x",
    '+': "t"
}
number_dictionary2 = {
    '0': "y",
    '1': "a",
    '2': "k",
    '3': "x",
    '4': "d",
    '5': "b",
    '6': "q",
    '7': "e",
    '8': "h",
    '9': "m",
    '-': "x",
    '+': "t"
}
number_dictionary3 = {
    "1": "g",
    "2": "i",
    "3": "l",
    "4": "o",
    "5": "s",
    "6": "v",
    "7": "g",
    "8": "i",
    "9": "l",
    "0": "o",
    '-': "x",
    '+': "t"
}


# transforms a single letter to digit
def num_convert(val):
    val = val.upper()
    select = int(alphabetDictionary[val])
    select = select // 22
    while select > 9:
        select += 7
        select = select // 3
    return str(select)


# converts a single letter to uppercase
def capitalize(val):
    letter = val.upper()
    return str(letter)


# converts the numberString to the password
def generate_id(number):
    select_case = 0
    number_string = str(number)
    identifier = ""
    for n in number_string:

        if select_case == 0:
            alphabet = str(number_dictionary1[n])
            identifier += alphabet
            select_case = select_case + 1
        elif select_case == 1:
            alphabet = str(number_dictionary2[n])
            identifier = identifier + alphabet
            select_case = select_case + 1
        elif select_case == 2:
            alphabet = number_dictionary3[n]
            processed_alphabet = str(num_convert(alphabet))
            identifier = identifier + processed_alphabet
            select_case = select_case + 1
        else:
            alphabet = number_dictionary3[n]
            processed_alphabet = capitalize(alphabet)
            identifier = identifier + processed_alphabet
            select_case = select_case - 3
    return identifier


def duration(time1, time2):
    time = (time1 - time2)
    years = time // timezone.timedelta(days=365.25)
    days = time % timezone.timedelta(days=365.25)
    if days < timezone.timedelta(days=30):
        return f"{years} years, {days} days"
    else:
        months = days // timezone.timedelta(days=30)
        if months == 1:
            return f"{years} years, {months} month"
        else:
            return f"{years} years, {months} months"
