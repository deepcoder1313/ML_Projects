import pandas as pd
from sklearn.cluster import KMeans
import pickle

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Select features
X = df[['Age','Annual Income (k$)','Spending Score (1-100)']]

# Train model
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Save model
with open("Kmeans.pkl","wb") as f:
    pickle.dump(kmeans,f)

print("Model saved successfully")