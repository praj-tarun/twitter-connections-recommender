import numpy as np
from core.store import tweet_store

def get_recommendations(liked_embeddings, index, top_k=5):
    if not liked_embeddings:
        return []

    vecs = np.stack([emb for (_, emb) in liked_embeddings])
    D, I = index.search(vecs, top_k)
    print(f"Search distances: {D}")  # Debug statement
    print(f"Search indices: {I}")    # Debug statement
    rec_ids = set(I.flatten().tolist())
    liked_ids = {fid for (fid, _) in liked_embeddings}
    rec_ids -= liked_ids
    return [tweet_store.get_tweet(i) for i in list(rec_ids) if i in tweet_store][:top_k]
