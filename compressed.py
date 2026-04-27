import pickle
import gzip

with open("similarity.pkl", "rb") as f:
    data = pickle.load(f)

with gzip.open("similarity_compressed.pkl.gz", "wb") as f:
    pickle.dump(data, f)