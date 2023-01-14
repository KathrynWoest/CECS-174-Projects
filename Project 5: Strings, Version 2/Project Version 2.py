def find(string, letter):  # L - Alexis Lopez-Ortiz
    """description: takes a character and finds it in the string
       input: two strings (the quote and a character)
       returns: an integer (the location of the character)"""
    return string.find(letter)


def find2(string, letter, start):  # M - Alexis Lopez-Ortiz
    """description: find(), but also starts at a defined index
       input: two strings (the quote and a character) and an integer (start index)
       returns: an integer (the location of the character)"""
    return string.find(letter, start)


def mirror(string):  # A - Alexis Lopez-Ortiz
    """description: takes a quote and mirrors it
       input: one string (the quote)
       returns: one string (the original quote, and it mirrored)"""
    mirror_text = string[-1::-1]  # reads the quote from the last character, moving backward
    both = string + mirror_text  # adds the original quote and the mirrored quote together into one string
    return both


def remove(string, letter):  # B - Alexis Lopez-Ortiz
    """description: removes all instances of a character from the quote
       input: two strings (the quote and a character)
       returns: a string (the original string with the specified character removed)"""
    lower_chr = letter.lower()  # makes the forbidden character lowercase
    first_change = string.replace(lower_chr, "")  # removes the forbidden character
    upper_chr = letter.upper()  # repeat with the uppercase version of the letter
    new_string = first_change.replace(upper_chr, "")
    return new_string


def char_num(string):  # C - Alexis Lopez-Ortiz
    """description: counts the number of alphabetic characters and 'e'
       input: one string (the quote)
       returns: nothing, the function prints the result"""
    num_e = 0  # initialize e count
    alpha_string = ''
    for i in string:  # check every index of 'string'
        if i.isalpha():  # if the character at the index is an alphabetical character
            alpha_string += i  # add the character to alpha_string
        if i == 'e' or i == 'E':  # if the character is 'e'
            num_e += 1  # increment the e count
    percent_e = num_e / len(alpha_string) * 100  # find the percent of the alphabetical characters that are 'e'
    result = f'Your text contains {len(alpha_string)} alphabetic characters, of which {num_e} ({percent_e:.1f}%) are ' \
             f'"e".'
    return result


def chr_num2(string, letter):  # D - Alexis Lopez-Ortiz
    """description: counts how many of one character there are
       input: two strings (the quote and the character)
       returns: an integer (the amount of the character)"""
    num_letter = 0  # repeat char_num code, but with an inputted character rather than 'e'
    alpha_string = ''
    for i in string:
        if i.isalpha():
            alpha_string += i
        if i == letter.lower() or i == letter.upper():
            num_letter += 1
    percent_letter = num_letter / len(alpha_string) * 100
    result = f"Your text contains {len(alpha_string)} alphabetic characters, of which {num_letter} " \
             f"({percent_letter:.1f}%) are '{letter}'."
    return result


def no_e(string):  # E - Alexis Lopez-Ortiz
    """description: determines if the given word has 'e' in it
       input: one string (the word)
       returns: a Boolean value (True if the word doesn't have 'e', False if it does)"""
    if 'e' not in string and 'E' not in string:
        return True
    else:
        return False


def no_letter(word, letter):  # F - Kathryn Woest
    """description: determines if the given word has a specified letter in it
       input: two strings (the word and the letter)
       returns: a Boolean value (True if the word doesn't have the letter in it, False if it does)"""
    lower_letter = find(word, letter.lower())  # uses find() to determine if the word has the letter in upper and lower
    upper_letter = find(word, letter.upper())
    if lower_letter == -1 and upper_letter == -1:  # if both upper and lower don't exist, return True
        return True
    else:
        return False


def no_e_words(quote):  # G - Kathryn Woest
    """description: takes out words with 'e' and reports the percent with none
       input: one string (the quote)
       returns: nothing, the function prints the result"""
    length = len(quote)
    new_quote = quote
    words = 0  # initializes total number of words
    eliminate = 0  # initializes the number of words removed
    word_location = 0  # initializes the location to search for words
    while word_location <= length:
        new_word_loc = quote.find(" ", word_location)  # find the first space after the start (indicates a word before)
        if new_word_loc == -1:  # if no spaces are found, either on the last word or there was only one word
            new_word = quote[word_location:]  # the word is the rest of the string
            words += 1  # add to the total number of words
            word_cap = new_word.find("E")  # see if the word has 'E' or 'e'
            word_low = new_word.find("e")
            if word_cap != -1 or word_low != -1:  # if it has either, remove the word
                new_quote = new_quote.replace(new_word, "")
                eliminate += 1  # add to the eliminate count
            break  # leave the while loop
        new_word = quote[word_location:new_word_loc]  # next word from where you started searching to before the space
        words += 1  # same as earlier
        word_cap = new_word.find("E")
        word_low = new_word.find("e")
        if word_cap != -1 or word_low != -1:
            new_quote = new_quote.replace(new_word, "")
            eliminate += 1
        word_location = new_word_loc + 1  # the new start is where the old space was + 1
    still_in_quote = words - eliminate  # total number of words left after removal
    percent = 100 * (still_in_quote / words)  # percent of words that were left out of the total
    result = f"The percent of words that have no 'e' in them is {percent:.01f}%.\n" + new_quote
    return result


def avoids(word, forbidden):  # H1 - Kathryn Woest
    """description: sees if a word has forbidden characters
       input: two strings (the word and the forbidden characters)
       returns: a Boolean variable (True if the word has none of the forbidden characters, False if it does)"""
    length = len(forbidden)
    letter = 0  # initializes the index of the forbidden string to search the word for that character
    while letter < length:
        no_contains = no_letter(word, forbidden[letter])  # uses no_letter() to see if the word has each character
        if not no_contains:  # if the word contains one of the forbidden characters, return False
            return False
        letter += 1  # add to the count to check the character at the next index
    return True  # if you reach the end without returning False, no forbidden are in the word -> return True


def avoids_user_forbidden(quote, forbidden):  # H2 - Kathryn Woest
    """description: returns the number of words in the quote that don't have the forbidden characters
       input: two strings (the quote and the forbidden characters)
       returns: nothing, the function prints the result"""
    length = len(quote)
    no_forbidden = 0  # initializes how many words have no forbidden characters
    word_location = 0  # initializes the location to search for words
    while word_location <= length:
        new_word_loc = quote.find(" ", word_location)  # same as no_e_words(), finds each word
        if new_word_loc == -1:  # if the word is the last one/only one
            new_word = quote[word_location:]
            no_contains = avoids(new_word, forbidden)  # uses avoids() to see if the word uses forbidden characters
            if no_contains:  # if the word doesn't contain any of the forbidden characters
                no_forbidden += 1  # add to the total of words that don't have forbidden characters
            break  # leave the while loop
        new_word = quote[word_location:new_word_loc]
        no_contains = avoids(new_word, forbidden)
        if no_contains:
            no_forbidden += 1
        word_location = new_word_loc + 1  # change the starting search position to where the last word ends
    result = f"The number of words that don't contain any of the characters in {forbidden} is {no_forbidden}."
    return result


def uses_only(word, use_chr):  # I - Kathryn Woest
    """description: sees if the word only contains letters in the string given
       input: two strings (the word and the only characters that can be used)
       returns: a Boolean value (True if the word only contains the given letters, False if it contains others)"""
    upper_use_chr = use_chr.upper()  # modifies the allowed to upper and lower to check all versions of the letters
    lower_use_chr = use_chr.lower()
    word_len = len(word)
    character_len = len(use_chr)
    a = 0  # initializes count for going through the word
    while a < word_len:
        b = 0  # initializes count for going through the allowed letters
        while b < character_len:
            if word[a] == upper_use_chr[b]:  # if the letter at word[a] is the letter at use_chr[b]
                break  # leave the loop to test the next index letter
            if word[a] == lower_use_chr[b]:
                break
            b += 1  # if not use_chr[b], test use_chr[b+1], etc. until you reach the end of allowed characters
        if b == character_len:  # if you leave the loop with b == the length of allowed characters, then word[a] is not
            return False        # an allowed character and the word contains a forbidden character.  return False
        a += 1
    return True  # if you reach the end, the word only contains allowed characters.  return True


def uses_all(word, use_chr):  # J1 - Kathryn Woest
    """description: sees if the word uses all required letters at least once
       input: two strings (the word and all the letters that must be used)
       returns: a Boolean value (True if the word uses all the required letters, False if it doesn't)"""
    length = len(use_chr)
    letter = 0  # initializes which index of word is being searched
    while letter < length:
        uses = no_letter(word, use_chr[letter])  # uses no_letter() to see if the word uses the letter
        if uses:  # if it doesn't use the letter, all required letters aren't used.  return False
            return False
        letter += 1  # increment the index so that the word is searched for every letter of use_chr
    return True  # if you reach the end, all required letters are used.  return True


def quote_uses_all(quote, use_chr):  # J2 - Kathryn Woest
    """description: returns the number of words in the quote that use all the required letters at least once
       input: two strings (the quote and all the letters that must be used)
       returns: nothing, the function prints the result"""
    length = len(quote)
    use_all_count = 0
    word_location = 0
    while word_location <= length:
        new_word_loc = quote.find(" ", word_location)
        if new_word_loc == -1:
            new_word = quote[word_location:]
            use_all = uses_all(new_word, use_chr)  # uses uses_all() to see if the word uses all the letters
            if use_all:  # if the word uses all the letters
                use_all_count += 1  # increase the total count of words that use all required by one
            break
        new_word = quote[word_location:new_word_loc]
        use_all = uses_all(new_word, use_chr)
        if use_all:
            use_all_count += 1
        word_location = new_word_loc + 1
    result = f"The number of words that use all of the characters in {use_chr} at least once is {use_all_count}."
    return result


def is_abecedarian(word):  # K1 - Kathryn Woest
    """description: sees if the letters in the word are in alphabetical order
       input: one string (the word)
       returns: a Boolean value (returns True if the letters are in alphabetical order, returns False if they aren't)"""
    length = len(word)
    new_word = word.lower()  # puts the word into lowercase so all values can be accurately compared
    letter = 0
    while letter < length - 1:
        if new_word[letter] > new_word[letter + 1]:  # if the letter is greater than the next one (ex. B, then A)
            return False
        letter += 1
    return True  # if you go through the whole word, then all letters are in alphabetical order.  return True


def quote_is_abecedarian(quote):  # K2 - Kathryn Woest
    """description: returns the number of words in the quote that are in alphabetical order
       input: one string (the quote)
       returns: nothing, the function prints the result"""
    length = len(quote)
    is_alpha = 0
    word_location = 0
    while word_location <= length:
        new_word_loc = quote.find(" ", word_location)
        if new_word_loc == -1:
            new_word = quote[word_location:]
            alphabetical = is_abecedarian(new_word)  # uses is_abecedarian() to see if the word is in alpha order
            if alphabetical:  # if the word is in alphabetical order, add to the total count of alphabetical words
                is_alpha += 1
            break
        new_word = quote[word_location:new_word_loc]
        alphabetical = is_abecedarian(new_word)
        if alphabetical:
            is_alpha += 1
        word_location = new_word_loc + 1
    result = f"The number of words that are in alphabetical order is {is_alpha}."
    return result


def is_sorted(string):  # N - Kathryn Woest
    """description: sees if the words are sorted in ascending (SIA)
       input: one string (the string to test)
       returns: a Boolean value (return True if the words are SIA, return False if they aren't)"""
    length = len(string)
    new_string = string.lower().strip()
    word_location = 0
    num_of_spaces = new_string.count(" ")  # determine if there is more than one word
    if num_of_spaces == 0:  # if there is only one word, it is already sorted in ascending, so return True
        return True
    new_word_loc = new_string.find(" ", word_location)
    word1 = new_string[word_location:new_word_loc]  # find the first word in the string
    word_location = new_word_loc + 1
    while word_location <= length:
        new_word_loc = new_string.find(" ", word_location)
        if new_word_loc == -1:
            word2 = new_string[word_location:]  # find the next word in the string
            if word1[0] > word2[0]:  # if the word is greater than the next word (ex. B > A), then not SIA
                return False
            break
        word2 = new_string[word_location:new_word_loc]
        if word1[0] > word2[0]:
            return False
        word1 = word2  # make the second word the new first word, then continue testing the rest of the string
        word_location = new_word_loc + 1
    return True  # if you go through the whole string, the entire thing is SIA.  return True


def is_anagram(word1_og, word2_og):  # O - Kathryn Woest
    """description: sees if the words are anagrams
       input: two strings (the first word and the second word)
       returns: a Boolean value (return True if the words are anagrams, return False if they aren't)"""
    word1 = word1_og.strip()  # strip any spaces at the end so the space isn't counted in the anagram characters
    word2 = word2_og.strip()
    if len(word1) != len(word2):  # if the words aren't the same length, they can't be anagrams.  return False
        return False
    anagram1 = uses_all(word1, word2)  # use uses_all() to see if the word uses all the other word's letters
    anagram2 = uses_all(word2, word1)
    if anagram1 and anagram2:  # if both words use all the other word's letters, they are anagrams.  return True
        return True
    else:
        return False


def has_duplicates(og_string):  # P - Kathryn Woest
    """description: checks to see if the string has any duplicate characters
       input: one string (the original string to be tested)
       returns: a Boolean value (return True if there is a duplicate character, return False if they are all unique)"""
    length = len(og_string)
    char = 0
    while char < length:
        dupl = og_string.count(og_string[char])  # check each character for how many times it occurs in the string
        if dupl != 1:  # if the character occurs more than once, the character is duplicated.  return True
            return True
        char += 1
    return False  # if you go through the whole string, there are no duplicates.  return False


def remove_duplicates(og_string):  # Q - Kathryn Woest
    """description: returns the string with only the unique characters from the original string (ex. mississippi->misp)
       input: one string (the original string)
       returns: nothing, the function prints the result"""
    length = len(og_string)
    char = 0
    while char < length:
        dupl = og_string.count(og_string[char])  # count the number of times the character shows up
        if dupl != 1:  # if the character being tested has duplicates
            new_string = og_string[char + 1:]  # separate the untested string from the untested string
            fixed_string = remove(new_string, og_string[char])  # remove the duplicates from the untested string
            og_string = og_string[:char + 1] + fixed_string  # add the fixed string to the original (no dupl anymore)
            length = len(og_string)  # reset the length of the string for the loop condition
        char += 1
    return og_string


def main():  # Kathryn Woest and Alexis Lopez-Ortiz
    given_quote = open("mobysmall.txt")
    moby_dick = given_quote.read()
    given_quote.close()

    reset = open("Project Version 2 Output File", "w")
    reset.write("")
    reset.close()

    output = open("Project Version 2 Output File", "a")

    # A
    print("Part A:\nThe original quote is printed, followed by the quote being mirrored.")
    print(mirror(moby_dick), "\n")

    output.write("Part A:\nThe original quote is printed, followed by the quote being mirrored.\n")
    output.write(mirror(moby_dick) + "\n")
    output.flush()

    # B
    print("Part B:\nThe function will remove a letter of your choice from the quote.")
    user_letter = input("What letter should be removed? ")
    print(remove(moby_dick, user_letter))

    output.write("\n")
    output.write("Part B:\nThe function will remove a letter of your choice from the quote.\n")
    output.write(f"What letter should be removed? '{user_letter}'\n")
    output.write(remove(moby_dick, user_letter))
    output.flush()

    # C
    print("Part C:\nThe function counts the number of alphabetic characters in the quote"
          " and keeps track of how many are the letter 'e'.")
    print(char_num(moby_dick))
    print()

    output.write("\n")
    output.write("Part C:\nThe function counts the number of alphabetic characters in the quote"
                 " and keeps track of how many are the letter 'e'.\n")
    output.write(str(char_num(moby_dick)))
    output.write("\n")
    output.flush()

    # D
    print("Part D:\nThe function keeps track of the number of times a character of your choice appears in the quote.")
    user_character = input("What character should be counted? ")
    print(chr_num2(moby_dick, user_character))
    print()

    output.write("\n")
    output.write("Part D:\nThe function keeps track of the number of times a character of "
                 "your choice appears in the quote.\n")
    output.write(f"What character should be counted? '{user_character}'\n")
    output.write(str(chr_num2(moby_dick, user_character)))
    output.write("\n")
    output.flush()

    # E
    print("Part E:\nThe function will return 'True' if the given word doesn't have 'e' in it. "
          "Else, it will return 'False'.")
    user_word_e = input("What is the word you would like to test? ")
    print(no_e(user_word_e))
    print()

    output.write("\n")
    output.write("Part E:\nThe function will return 'True' if the given word doesn't have 'e' in it. "
                 "Else, it will return 'False'.\n")
    output.write(f"What is the word you would like to test? '{user_word_e}'\n")
    output.write(str(no_e(user_word_e)))
    output.write("\n")
    output.flush()

    # F
    print("Part F:\nThe function will return 'True' if the given word doesn't have a character of your choice in it. "
          "Else, it will return 'False'.")
    user_word_f = input("What is the word you would like to test? ")
    user_letter_f = input("What character should be looked for? ")
    print(no_letter(user_word_f, user_letter_f))
    print()

    output.write("\n")
    output.write("Part F:\nThe function will return 'True' if the given word doesn't have a character of your choice in"
                 " it. Else, it will return 'False'.\n")
    output.write(f"What is the word you would like to test? '{user_word_f}'\n")
    output.write(f"What character should be looked for? '{user_letter_f}'\n")
    output.write(str(no_letter(user_word_f, user_letter_f)))
    output.write("\n")
    output.flush()

    # G
    print("Part G:\nThe function will only print words that don't contain the letter 'e', "
          "and will compute the percentage of the words that have no 'e'.")
    print(no_e_words(moby_dick))
    print()

    output.write("\n")
    output.write("Part G:\nThe function will only print words that don't contain the letter 'e', "
                 "and will compute the percentage of the words that have no 'e'.\n")
    output.write(str(no_e_words(moby_dick)))
    output.write("\n")
    output.flush()

    # H
    print("Part H:\nFirst, the function will take a word and a string of forbidden letters.  It will return 'True'"
          " if the word doesn't use any of those letters, and 'False' if it does.")
    user_word_h = input("What is the word you would like to test? ")
    user_forbidden_h = input("What are the forbidden letters? ")
    print(avoids(user_word_h, user_forbidden_h))
    print("Now, the function will see how many words in the quote do not contain these forbidden letters.")
    print(avoids_user_forbidden(moby_dick, user_forbidden_h))
    print()

    output.write("\n")
    output.write("Part H:\nFirst, the function will take a word and a string of forbidden letters.  It will return "
                 "'True' if the word doesn't use any of those letters, and 'False' if it does.\n")
    output.write(f"What is the word you would like to test? '{user_word_h}'\n")
    output.write(f"What are the forbidden letters? '{user_forbidden_h}'\n")
    output.write(str(avoids(user_word_h, user_forbidden_h)))
    output.write("\nNow, the function will see how many words in the quote do not contain these forbidden letters.\n")
    output.write(str(avoids_user_forbidden(moby_dick, user_forbidden_h)))
    output.write("\n")
    output.flush()

    # I
    print("Part I:\nThe function will take a word and a string of letters, and will return 'True' if the word "
          "contains only letters in the list provided. \nIt will return 'False' if it contains other letters.")
    user_word_i = input("What is the word you would like to test? ")
    user_letters_i = input("What are the only letters that can be used? ")
    print(uses_only(user_word_i, user_letters_i))
    print()

    output.write("\n")
    output.write("Part I:\nThe function will take a word and a string of letters, and will return 'True' if the word "
                 "contains only letters in the list provided. \nIt will return 'False' if it contains other letters.\n")
    output.write(f"What is the word you would like to test? '{user_word_i}'\n")
    output.write(f"What are the only letters that can be used? '{user_letters_i}'\n")
    output.write(str(uses_only(user_word_i, user_letters_i)))
    output.write("\n")
    output.flush()

    # J
    print("Part J:\nFirst, the function will take a word and a string of required letters.  It will return 'True'"
          " if the word uses all of the required letters, and 'False' if it does not.")
    user_word_j = input("What is the word you would like to test? ")
    user_required_j = input("What are the required letters? ")
    print(uses_all(user_word_j, user_required_j))
    print("Now, the function will return the number of words in the quote that use all the required letters provided.")
    print(quote_uses_all(moby_dick, user_required_j))
    print("Finally, the number of words that contain 'aeiou' or 'aeiouy' in the quote is 0.\n")

    output.write("\n")
    output.write("Part J:\nFirst, the function will take a word and a string of required letters.  It will return "
                 "'True' if the word uses all of the required letters, and 'False' if it does not.\n")
    output.write(f"What is the word you would like to test? '{user_word_j}'\n")
    output.write(f"What are the required letters? '{user_required_j}'\n")
    output.write(str(uses_all(user_word_j, user_required_j)))
    output.write("\nNow, the function will return the number of words in the quote that use all the required letters "
                 "provided.\n")
    output.write(str(quote_uses_all(moby_dick, user_required_j)))
    output.write("\nFinally, the number of words that contain 'aeiou' or 'aeiouy' in the quote is 0.\n")
    output.write("\n")
    output.flush()

    # K
    print("Part K:\nFirst, the function will take a word and return 'True' if the letters in it appear in alphabetical"
          " order. It will return 'False' if they are not.")
    user_word_k = input("What is the word you would like to test? ")
    print(is_abecedarian(user_word_k))
    print("Now, the function will return the number of words in the quote that are in alphabetical order.")
    print(quote_is_abecedarian(moby_dick))
    print()

    output.write("\n")
    output.write("Part K:\nFirst, the function will take a word and return 'True' if the letters in it appear in "
                 "alphabetical order. It will return 'False' if they are not.\n")
    output.write(f"What is the word you would like to test? '{user_word_k}'\n")
    output.write(str(is_abecedarian(user_word_k)))
    output.write("\nNow, the function will return the number of words in the quote that are in alphabetical order.\n")
    output.write(str(quote_is_abecedarian(moby_dick)))
    output.write("\n")
    output.flush()

    # L
    print("Part L:\nThe function will take a character and find the first index where it appears in the quote."
          " If the character is not found, the function will return -1.")
    user_character_l = input("What character should be searched for? ")
    print(find(moby_dick, user_character_l))
    print()

    output.write("\n")
    output.write("Part L:\nThe function will take a character and find the first index where it appears in the quote."
                 " If the character is not found, the function will return -1.\n")
    output.write(f"What character should be searched for? '{user_character_l}'\n")
    output.write(str(find(moby_dick, user_character_l)))
    output.write("\n")
    output.flush()

    # M
    print("Part M:\nThe function will take a character and find the first index of it after the given start index."
          " If the character is not found, the function will return -1.")
    user_character_m = input("What character should be searched for? ")
    user_start_m = int(input("From which index should the function begin searching? "))
    print(find2(moby_dick, user_character_m, user_start_m))
    print()

    output.write("\n")
    output.write("Part M:\nThe function will take a character and find the first index of it after the given start "
                 "index. If the character is not found, the function will return -1.\n")
    output.write(f"What character should be searched for? '{user_character_m}'\n")
    output.write(f"From which index should the function begin searching? '{str(user_start_m)}'\n")
    output.write(str(find2(moby_dick, user_character_m, user_start_m)))
    output.write("\n")
    output.flush()

    # N
    print("Part N:\nThe function will take a string and return 'True' if the string is sorted in ascending order."
          " Else, it will return 'False'.")
    user_string_n = input("What string would you like to test? ")
    print(is_sorted(user_string_n))
    print()

    output.write("\n")
    output.write("Part N:\nThe function will take a string and return 'True' if the string is sorted in ascending "
                 "order. Else, it will return 'False'.\n")
    output.write(f"What string would you like to test? '{user_string_n}'\n")
    output.write(str(is_sorted(user_string_n)))
    output.write("\n")
    output.flush()

    # O
    print("Part O:\nThe function will take two words and return 'True' if they're anagrams and 'False' if they aren't.")
    user_word1 = input("What is word 1? ")
    user_word2 = input("What is word 2? ")
    print(is_anagram(user_word1, user_word2))
    print()

    output.write("\n")
    output.write("Part O:\nThe function will take two words and return 'True' if they're anagrams and 'False' "
                 "if they aren't.\n")
    output.write(f"What is word 1? '{user_word1}'\n")
    output.write(f"What is word 2? '{user_word2}'\n")
    output.write(str(is_anagram(user_word1, user_word2)))
    output.write("\n")
    output.flush()

    # P
    print("Part P:\nThe function will take a string and return 'True' if there is any character that repeats."
          " Else, it will return 'False'.")
    user_string_o = input("What string would you like to test? ")
    print(has_duplicates(user_string_o))
    print()

    output.write("\n")
    output.write("Part P:\nThe function will take a string and return 'True' if there is any character that repeats."
                 " Else, it will return 'False'.\n")
    output.write(f"What string would you like to test? '{user_string_o}'\n")
    output.write(str(has_duplicates(user_string_o)))
    output.write("\n")
    output.flush()

    # Q
    print("Part Q:\nThe function will take a string and return a new string with only"
          " the unique characters from the original.")
    print("For example, if you put in 'mississippi', the function will return 'misp'.")
    user_word_q = input("What is the word you would like to use? ")
    print(remove_duplicates(user_word_q))

    output.write("\n")
    output.write("Part Q:\nThe function will take a string and return a new string with only"
                 " the unique characters from the original.\n")
    output.write("For example, if you put in 'mississippi', the function will return 'misp'.\n")
    output.write(f"What is the word you would like to use? '{user_word_q}'\n")
    output.write(str(remove_duplicates(user_word_q)))
    output.write("\n")
    output.flush()

    output.close()


if __name__ == "__main__":
    main()
