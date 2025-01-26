file = open("input.txt", "r")
text = file.read()
word_list = text.split()
print(word_list)

total_words = len(word_list)
print(total_words)

end_punctuation = ['.', '!', '?', ';', ':']
total_sentences = 0
current_sentence_fragment = ""


for character in text:
    if character in end_punctuation:  
        if current_sentence_fragment.strip():  
            total_sentences += 1
        current_sentence_fragment = ""  
    else:
        current_sentence_fragment += character  

if current_sentence_fragment.strip():
    total_sentences += 1

print("Sentence count:", total_sentences)

vowel_letters = "aeiou"
total_syllables = 0

for single_word in word_list:
    single_word = single_word.lower()  
    if len(single_word) <= 3:
        total_syllables += 1
        continue

    syllables_in_word = 0
    index = 0
    while index < len(single_word):
        if single_word[index] in vowel_letters:
            if index + 1 < len(single_word) and single_word[index + 1] in vowel_letters:
                syllables_in_word += 1
                index += 2  
            else:
                syllables_in_word += 1
                index += 1
        else:
            index += 1

    if single_word.endswith("es") or single_word.endswith("ed"):
        syllables_in_word -= 1
    elif single_word.endswith("e") and not single_word.endswith("le"):
        syllables_in_word -= 1
    if syllables_in_word < 1:
        syllables_in_word = 1

    total_syllables += syllables_in_word

print("Syllable count:", total_syllables)

flesch_index = round(206.835 - 1.1015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words))
print("Flesch Reading Ease Index:", flesch_index)

flesch_grade_level = round(0.39 * (total_words / total_sentences) + 11.8 * (total_syllables / total_words) - 15.59)
print("Flesch-Kincaid Grade Level:", flesch_grade_level)


if flesch_grade_level >= 0 and flesch_grade_level <= 30:
    print("College level")
elif flesch_grade_level >= 50 and flesch_grade_level <= 60:
    print("School level")
elif flesch_grade_level >= 90 and flesch_grade_level <= 100:
    print("4th grade")
