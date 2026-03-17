from transformers import BertTokenizer, BertModel
import torch.nn.functional as F
tok = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
def emb(w):
    return model(**tok(w, return_tensors='pt')).last_hidden_state.mean(1)
print("BERT Similarity:",F.cosine_similarity(emb("king"), emb("queen")).item())