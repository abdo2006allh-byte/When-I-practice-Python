import pandas as pd
import re
import warnings
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

warnings.filterwarnings('ignore')

# 1. Load the dataset
df = pd.read_csv("Amazon_Unlocked_Mobile.csv")

# 2. Select relevant columns and drop missing values
df = df[['Rating', 'Reviews']]
df.dropna(inplace=True)

# 3. Sentiment Labeling based on Rating
def label_rating(rating):
    if rating >= 4:
        return 'Positive'
    elif rating <= 2:
        return 'Negative'
    else:
        return 'Neutral'

df['label'] = df['Rating'].apply(label_rating)

# 4. Text Cleaning Function (Regex & Lowercasing)
def clean_text(text):
    # Convert to string and lowercase
    text = str(text).lower()
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove non-alphabetic characters (punctuation/numbers)
    text = re.sub('[^a-z]', ' ', text)
    # Remove extra whitespaces
    text = re.sub(r"\s+", ' ', text).strip()
    return text

# Apply initial cleaning
df['CleanReview'] = df['Reviews'].apply(clean_text)

# 5. Tokenization
df['CleanReview'] = df['CleanReview'].apply(word_tokenize)

# 6. Stopwords Removal
stop_words = set(stopwords.words('english'))
def remove_stopwords(tokens):
    return [item for item in tokens if item not in stop_words]

df['CleanReview'] = df['CleanReview'].apply(remove_stopwords)

# 7. Lemmatization (Returning words to their base/dictionary form)
# 
lemma = WordNetLemmatizer()
def apply_lemmatization(tokens):
    # Lemmatize as verbs ('v')
    return [lemma.lemmatize(w, pos='v') for w in tokens]

df['CleanReview'] = df['CleanReview'].apply(apply_lemmatization)

# 8. Convert list of tokens back to a single string
def convert_to_string(token_list):
    return ' '.join(token_list)

df['CleanReview'] = df['CleanReview'].apply(convert_to_string)

# Final check
print(df[['Reviews', 'CleanReview', 'label']].head())