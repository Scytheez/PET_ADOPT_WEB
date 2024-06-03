import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer

# Define the data
data = {
    'pet_attitude': ['friendly', 'aggressive', 'playful', 'calm', 'affectionate'],
    'owner_attitude': [['patient', 'warm-hearted', 'sociable', 'interactive', 'tolerant'],  # friendly
                        ['patient', 'confident', 'experienced', 'firm', 'understanding', 'nurture'],  # aggressive
                        ['patient', 'energetic', 'interactive', 'tolerable', 'engaging'],  # playful
                        ['patient', 'gentle', 'relaxed', 'tranquil', 'observant'],  # calm
<<<<<<< HEAD
                        ['patient', 'loving', 'gentle', 'relaxed', 'warm-hearted', 'interactive', 'nurture']]  # affectionate
=======
                        ['patient', 'loving', 'gentle', 'relaxed', 'warm-hearted', 'interactive', 'nurture']  # affectionate
                    ]
>>>>>>> bc196a921fccea737c5fd930710533a3050f82b3
}

# Create DataFrame
df = pd.DataFrame(data)

# Flatten lists in 'owner_attitude' column
df['owner_attitude'] = df['owner_attitude'].apply(lambda x: ' '.join(x))

# Define features and target
X = df['owner_attitude']
y = df['pet_attitude']

# Instantiate CountVectorizer to convert text data into numerical features
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Convert sparse matrix to dense numpy array
X_dense = X_vectorized.toarray()

# Instantiate k-NN Classifier with n_neighbors=3 for example
knn_classifier = KNeighborsClassifier(n_neighbors=3)
knn_classifier.fit(X_dense, y)

# Define additional owner traits
new_owner_traits = ['']

# Join new owner traits into a single string
new_owner_traits_joined = ' '.join(new_owner_traits)

# Transform the new owner traits using the same vectorizer
new_owner_traits_vectorized = vectorizer.transform([new_owner_traits_joined])

# Predict pet attitude probabilities
predicted_probabilities = knn_classifier.predict_proba(new_owner_traits_vectorized)[0]
predicted_pet_attitudes = knn_classifier.classes_

# Calculate total probability for all pet attitudes
total_probability_all = sum(predicted_probabilities)

# Calculate and print percentages for all pet attitudes
print("\nPercentage for all pet attitudes:")
default_probability = 0.01  # Set a small default probability for all attitudes
for idx, attitude in enumerate(predicted_pet_attitudes):
    probability = ((predicted_probabilities[idx] + default_probability) / (total_probability_all + default_probability * len(predicted_pet_attitudes))) * 100
    print(f"{attitude}: {probability:.2f}%")

# Sort predicted pet attitudes by probabilities in descending order
sorted_indices = predicted_probabilities.argsort()[::-1]
top_3_indices = sorted_indices[:3]

# Calculate total probability for top 3 pet attitudes
total_probability_top3 = sum(predicted_probabilities[top_3_indices])

# Print top 3 pet attitudes with their probabilities
print("\nTop 3 suitable pet personalities and their probabilities:")
for idx in top_3_indices:
    personality = predicted_pet_attitudes[idx]
    probability = (predicted_probabilities[idx] / total_probability_top3) * 100
    print(f"{personality}: {probability:.2f}%")
