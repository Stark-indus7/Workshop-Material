# This project recommends movies based on user preferences and past ratings.
# Implement the code here

from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

# Load dataset (MovieLens dataset for example)
data = Dataset.load_builtin('ml-100k')
trainset, testset = train_test_split(data, test_size=0.25)

# Train a SVD model
model = SVD()
model.fit(trainset)

# Predict ratings for testset
predictions = model.test(testset)
print(predictions)
