#list of library
import PyPDF2  #pdf library
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import string
from nltk.stem import WordNetLemmatizer 
from matplotlib import pyplot
import regex as re
#--------------------------------------------------------------------#
# creating a pdf file object 
pdfFileObj = open('combined_example.pdf', 'rb') 
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
#  ---------------------------------------------------------------------- 

# printing number of pages in pdf file 
# print(pdfReader.numPages) 

# creating a page object 
# pageObj = pdfReader.getPage(0) 
  
# extracting text from page 
# print(pageObj.extractText()) 
print("---------------------------------------------------------------------")
print("Page contents")

for i in range(pdfReader.numPages):
      page_to_print = pdfReader.getPage(i)
      print(page_to_print.extractText().encode('utf8'))

num_pages = pdfReader.numPages
count = 0
text = ""
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
print("---------------------------------------------------------------------")

# -------------------------------------------------------------------------------------
# Tokenizations
print("Tokenizations")
tokenization_words = word_tokenize(text)
print(tokenization_words)

# -------------------------------------------------------------------------------------
#normalization
# Removed punctuation
punctuation_words = [word for word in tokenization_words if word.isalpha()]

# convert to lower case
lower_case = [w.lower() for w in punctuation_words]

# removes spaces
remove_spaces = [w.strip() for w in lower_case]

# removes number
remove_num = [''.join(x for x in w if x.isalpha()) for w in remove_spaces] 
# -------------------------------------------------------------------------------------
print("---------------------------------------------------------------------")

print("Stopwords")
stop_words = set(stopwords.words('english'))
result = [word for word in remove_num if not word in stop_words]
print(result)

print("---------------------------------------------------------------------")
# -------------------------------------------------------------------------------------
print("POS Tag")
tag = nltk.pos_tag(result)
print(tag)

print("---------------------------------------------------------------------")
# -------------------------------------------------------------------------------------

print("Stemming")
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in result]
print(stemmed)

print("---------------------------------------------------------------------")
# -------------------------------------------------------------------------------------
#Lemmmatization
print("Lemmatization")
wordnet_lemmatizer = WordNetLemmatizer()
lemmatize = [wordnet_lemmatizer.lemmatize(word) for word in result]
print(lemmatize)

print("---------------------------------------------------------------------")
# -------------------------------------------------------------------------------------

#write the contents in text file 
with open("Tokenization.txt", "w") as text_file:
    text_file.write("{0}".format(tokenization_words).encode('utf8'))

with open("Stopwords.txt", "w") as text_file:
    text_file.write("{0}".format(result).encode('utf8'))

with open("Tag.txt", "w") as text_file:
    text_file.write("{0}".format(tag).encode('utf8'))

with open("Lemmatization.txt", "w") as text_file:
    text_file.write("{0}".format(lemmatize).encode('utf8'))

with open("Stemmed.txt", "w") as text_file:
    text_file.write("{0}".format(stemmed).encode('utf8'))

print("successfully saved!")

print("---------------------------------------------------------------------")
# -------------------------------------------------------------------------------------
