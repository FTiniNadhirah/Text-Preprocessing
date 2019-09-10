import PyPDF2  #pdf library
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import string
from nltk.stem import WordNetLemmatizer 
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
    f = text.replace("\n", " ") 
print("---------------------------------------------------------------------")

# -------------------------------------------------------------------------------------
# Tokenizations
print("Tokenizations")
tokenization_words = word_tokenize(f)

print(tokenization_words)


# -------------------------------------------------------------------------------------
# Removed punctuation
punctuation_words = [word for word in tokenization_words if word.isalpha()]
print(punctuation_words)

# convert to lower case
normalization = [w.lower() for w in punctuation_words]
print("---------------------------------------------------------------------")

# -------------------------------------------------------------------------------------
print("---------------------------------------------------------------------")
print("Stopwords")
stop_words = set(stopwords.words('english'))
result = [word for word in normalization if not word in stop_words]
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
with open("Stemmed.txt", "w") as text_file:
    text_file.write("{0}".format(stemmed).encode('utf8'))

with open("Tokenization.txt", "w") as text_file:
    text_file.write("{0}".format(result).encode('utf8'))

with open("Stopwords.txt", "w") as text_file:
    text_file.write("{0}".format(normalization).encode('utf8'))

with open("Tag.txt", "w") as text_file:
    text_file.write("{0}".format(tag).encode('utf8'))

with open("Lemmatization.txt", "w") as text_file:
    text_file.write("{0}".format(lemmatize).encode('utf8'))

print("successfully saved!")

print("---------------------------------------------------------------------")

# -------------------------------------------------------------------------------------
