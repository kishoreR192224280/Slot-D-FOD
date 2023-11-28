import pandas as pd
reviews = [
    "This product is amazing! I love how easy it is to use.",
    "I'm not sure I would recommend this product. It's not as good as I thought it would be.",
    "This product is just what I needed. It's perfect for my needs.",
    "I'm very happy with this product. It's exceeded my expectations.",
    "I would not recommend this product. It's not worth the money.",
]
reviews_lowercase = [review.lower() for review in reviews]
import string
punctuation = string.punctuation
reviews_without_punctuation = [''.join(char for char in review if char not in punctuation) for review in reviews_lowercase]
reviews_split = [review.split() for review in reviews_without_punctuation]
word_counts = {}
for review in reviews_split:
    for word in review:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
word_counts_df = pd.DataFrame.from_dict(word_counts, orient='index', columns=['Count'])
word_counts_df = word_counts_df.sort_values(by='Count', ascending=False)
print(word_counts_df)
