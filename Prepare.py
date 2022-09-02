def basic_clean(string):
    
    string = string.lower()
    
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    
    string = re.sub(r"[^a-z0-9\s']", '', string)
    
    return string


def tokenize(string):
    
    tokenizer = ToktokTokenizer()
    
    return tokenizer.tokenize(string, return_str=True)


def stem(string):
    
    ps = nltk.porter.PorterStemmer()
    
    stems = [ps.stem(word) for word in string.split()]
    
    stemmed_string = ' '.join(stems)
    
    return stemmed_string


def lemmatize(string):
    
    wnl = nltk.stem.WordNetLemmatizer()
    
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    
    lemmatized_string = ' '.join(lemmas)
    
    return lemmatized_string

def remove_stopwords(string, extra_words=None, exclude_words=None):
    
    stopword_list = stopwords.words('english')
    
    if exclude_words:
        
        stopword_list = stopword_list + exclude_words
        
    if extra_words:
        
        for word in extra_words:
            
            stopword_list.remove(word)
            
    words = string.split()
    
    filtered_words = [word for word in words if word not in stopword_list]
    
    filtered_string = ' '.join(filtered_words)
    
    return filtered_string





