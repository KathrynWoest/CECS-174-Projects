def first_e(name):  # 3 - Alexis Lopez-Ortiz
    """description: finds the first 'e' in the name
       parameters: one string (name)
       returns: one integer (index of first e)"""
    e1 = name.find('e')
    if e1 == -1:  # if 'e' doesn't exist in the name
        return 0
    else:
        return e1 + 1


def words(name):  # 4 - Kathryn Woest
    """description: finds the number of words in the name
       parameters: one string (name)
       returns: one integer (number of words)"""
    clean_name = name.strip()
    space_count = clean_name.count(" ")
    return space_count + 1


def word1(name):  # 5 - Kathryn Woest
    """description: finds the first word in the name
       parameters: one string (name)
       returns: one string (first word)"""
    clean_name = name.strip()
    space1 = clean_name.find(" ")
    if space1 == -1:  # if there is only one name/word
        return clean_name
    else:
        word_1 = clean_name[:space1]
        return word_1


def vowels(name):  # 6 - Kathryn Woest
    """description: finds number of vowels in name
       parameters: one string (name)
       returns: one integer (number of vowels)"""
    lower_name = name.lower()
    a = lower_name.count("a")
    e = lower_name.count("e")
    i = lower_name.count("i")
    o = lower_name.count("o")
    u = lower_name.count("u")
    vowel = a + e + i + o + u
    return vowel


def cap_vowels(name):  # 7 - Kathryn Woest
    """description: makes all vowels capital in the name
       parameters: one string (name)
       returns: one string (original parameter with all vowels capitalized)"""
    name = name.replace("a", "A")
    name = name.replace("e", "E")
    name = name.replace("i", "I")
    name = name.replace("o", "O")
    name = name.replace("u", "U")
    return name


def split_in_two(name, name_length):  # 9 - Alexis Lopez-Ortiz
    """description: splits the name between 70 *'s
       parameters: two strings (name, name length)
       returns: one string (name split in half around 70 *'s)"""
    half_point = name_length // 2
    first_half = name[:half_point]
    second_half = name[half_point:]
    with_asterisks = first_half + ("*" * 70) + second_half
    return with_asterisks


def main():  # 1, 2, 8, and Formatting - Alexis Lopez-Ortiz
    user_name = str(input('Please enter your name: '))
    name_len = len(user_name)  # 1
    last_chr = user_name[-1]  # 2
    e_pos = first_e(user_name)
    num_words = words(user_name)
    first_word = word1(user_name)
    vowel_count = vowels(user_name)
    capital_vowels = cap_vowels(user_name)
    in_half = split_in_two(user_name, name_len)

    print(f"\nYour name is {name_len} characters long.")
    print(f"\nThe last character is: {last_chr}")
    print(f"\nThe first 'e' is at position {e_pos}.")
    print(f"\nYour name has {num_words} words.")
    print(f"\nYour first name is {first_word}.")
    print(f"\nYour name contains {vowel_count} vowels.")
    print(f"\nYour name with uppercase vowels is: {capital_vowels}")
    print("\n" + ("+" * 70) + ("~" * 50) + user_name + ("~" * 50) + ("+" * 70))  # 8
    print("\n" + in_half)


if __name__ == "__main__":
    main()
