from transformers import RobertaTokenizer, RobertaModel
import torch.nn.functional as F

tok = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaModel.from_pretrained('roberta-base')

def emb(w):
    return model(**tok(w, return_tensors='pt')).last_hidden_state.mean(1)

print("RoBERTa Similarity:",
      F.cosine_similarity(emb("king"), emb("queen")).item())