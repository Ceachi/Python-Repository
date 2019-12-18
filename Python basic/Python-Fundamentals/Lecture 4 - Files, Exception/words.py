def fetch_words():

   with open('t.txt') as file:

       file_words = []

       for line in file:

           line_words = line.split()

           for word in line_words:

               file_words.append(word)

   for word in file_words:

       print(word)
       
print(__name__)
if __name__ == '__name__':
    fetch_words()