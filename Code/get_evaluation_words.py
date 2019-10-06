# This script reads the evaluation dataset files and writes copies of them without the scores

def read_file(filename, skip_lines, index_a=0, index_b=1):
    """ Reads word pairs from files"""
    word_pairs = []

    with open(filename, 'r') as text_file:
        for _ in range(skip_lines):
            next(text_file)
        for line in text_file:
            words = line.split('\t')
            word_pairs.append([words[index_a], words[index_b]])


    return word_pairs

def write_file(filename):
    """ Writes the word pairs to a file"""
    with open(filename, 'w') as text_file:
        for word in word_pairs:
            text_file.write(word[0] + ", " + word[1] + '\n')

if __name__ == "__main__":
    word_pairs = read_file('SimLex-999.txt', 1)
    write_file('cleaned_SimLex-999.txt')

    word_pairs = read_file('wordsim353_agreed.txt', 11, 1, 2)
    write_file('cleaned_wordsim353_agreed.txt')

    word_pairs = read_file('wordsim353_annotator1.txt', 11, 1, 2)
    write_file('cleaned_wordsim353_annotator1.txt')

    word_pairs = read_file('wordsim353_annotator2.txt', 10, 1, 2)
    write_file('cleaned_wordsim353_annotator2.txt')

    word_pairs = read_file('wordsim_relatedness_goldstandard.txt', 0)
    write_file('cleaned_wordsim_relatedness_goldstandard.txt')

    word_pairs = read_file('wordsim_similarity_goldstandard.txt', 0)
    write_file('cleaned_wordsim_similarity_goldstandard.txt')