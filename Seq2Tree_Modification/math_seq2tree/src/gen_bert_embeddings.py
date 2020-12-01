import json
from pytorch_pretrained_bert import BertTokenizer, BertModel
import torch
import numpy as np
import pickle
from sklearn.manifold import TSNE

def gen_embed_input():
  vocab = {}
  emb_dict = {}
  with open("input_vocab_dict.json",'r') as f:
    vocab = json.load(f)

  words_list = list(vocab.keys())

  print(words_list[0])

  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')

  BertModel1 = BertModel.from_pretrained('bert-base-chinese').to(device)
  BertModel1.eval()

  print(len(words_list))
  for idx in range(len(words_list)):
    #print(idx)
    cap = u'[CLS] '+words_list[idx]
                    

    tokenized_cap = tokenizer.tokenize(cap)                
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_cap)
    tokens_tensor = torch.tensor([indexed_tokens]).to(device)

    if len(indexed_tokens) != 0:
      with torch.no_grad():
        encoded_layers, _ = BertModel1(tokens_tensor)

      bert_embedding = encoded_layers[5].squeeze(0)

      dim = bert_embedding.shape[0]

      if dim > 1:
        bert_embedding = bert_embedding[1:]
        x = bert_embedding[0]
        x = x.reshape(1,768)
        for i in range(1,dim-1):
          temp_emb = bert_embedding[i]
          temp_emb = temp_emb.reshape(1,768)
          x = torch.add(x,temp_emb)
      else:
        x = bert_embedding[0]
        x = x.reshape(1,768)

      x = x.to("cpu")
      x_np = x.data.numpy()
    else:
      x_np = np.random.randn(1, 768)

    emb_dict[words_list[idx]] = x_np

  with open('input_embeddings_dict.pickle', 'wb') as handle:
      pickle.dump(emb_dict, handle)


def gen_embed_output():
  vocab = {}
  emb_dict = {}
  with open("output_vocab_dict.json",'r') as f:
    vocab = json.load(f)

  words_list = list(vocab.keys())

  print(words_list[0])

  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')

  BertModel1 = BertModel.from_pretrained('bert-base-chinese').to(device)
  BertModel1.eval()

  print(len(words_list))
  for idx in range(len(words_list)):
    #print(idx)
    cap = words_list[idx]
                    

    tokenized_cap = tokenizer.tokenize(cap)                
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_cap)
    tokens_tensor = torch.tensor([indexed_tokens]).to(device)

    if len(indexed_tokens) != 0:
      with torch.no_grad():
        encoded_layers, _ = BertModel1(tokens_tensor)

      bert_embedding = encoded_layers[5].squeeze(0)

      dim = bert_embedding.shape[0]

      if dim > 1:
        bert_embedding = bert_embedding[1:]
        x = bert_embedding[0]
        x = x.reshape(1,768)
        for i in range(1,dim-1):
          temp_emb = bert_embedding[i]
          temp_emb = temp_emb.reshape(1,768)
          x = torch.add(x,temp_emb)
      else:
        x = bert_embedding[0]
        x = x.reshape(1,768)

      x = x.to("cpu")
      x_np = x.data.numpy()
    else:
      x_np = np.random.randn(1, 768)

    emb_dict[words_list[idx]] = x_np

  with open('output_embeddings_dict.pickle', 'wb') as handle:
      pickle.dump(emb_dict, handle)

def gen_embed_input_tsne():
  print("TSNE input")
  vocab = {}
  emb_dict = {}
  with open("input_vocab_dict.json",'r') as f:
    vocab = json.load(f)

  words_list = list(vocab.keys())

  print(words_list[0])

  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')

  BertModel1 = BertModel.from_pretrained('bert-base-chinese').to(device)
  BertModel1.eval()

  print(len(words_list))
  for idx in range(len(words_list)):
    #print(idx)
    cap = words_list[idx]
                    

    tokenized_cap = tokenizer.tokenize(cap)                
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_cap)
    tokens_tensor = torch.tensor([indexed_tokens]).to(device)

    if len(indexed_tokens) != 0:
      with torch.no_grad():
        encoded_layers, _ = BertModel1(tokens_tensor)

      bert_embedding = encoded_layers[11].squeeze(0)

      dim = bert_embedding.shape[0]

      if dim > 1:
        x = bert_embedding[0]
        x = x.reshape(1,768)
        for i in range(1,dim):
          temp_emb = bert_embedding[i]
          temp_emb = temp_emb.reshape(1,768)
          x = torch.add(x,temp_emb)
      else:
        x = bert_embedding[0]
        x = x.reshape(1,768)

      x = x.to("cpu")
      x_np = x.data.numpy()
    else:
      x_np = np.random.randn(1, 768)

    X_np_tsne = TSNE(n_components=128).fit_transform(x_np)
    emb_dict[words_list[idx]] = X_np_tsne

  with open('input_embeddings_dict.pickle', 'wb') as handle:
      pickle.dump(emb_dict, handle)


def gen_embed_output_tsne():
  print("TSNE output")
  vocab = {}
  emb_dict = {}
  with open("output_vocab_dict.json",'r') as f:
    vocab = json.load(f)

  words_list = list(vocab.keys())

  print(words_list[0])

  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
  tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')

  BertModel1 = BertModel.from_pretrained('bert-base-chinese').to(device)
  BertModel1.eval()

  print(len(words_list))
  for idx in range(len(words_list)):
    #print(idx)
    cap = words_list[idx]
                    

    tokenized_cap = tokenizer.tokenize(cap)                
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_cap)
    tokens_tensor = torch.tensor([indexed_tokens]).to(device)

    if len(indexed_tokens) != 0:
      with torch.no_grad():
        encoded_layers, _ = BertModel1(tokens_tensor)

      bert_embedding = encoded_layers[11].squeeze(0)

      dim = bert_embedding.shape[0]

      if dim > 1:
        x = bert_embedding[0]
        x = x.reshape(1,768)
        for i in range(1,dim):
          temp_emb = bert_embedding[i]
          temp_emb = temp_emb.reshape(1,768)
          x = torch.add(x,temp_emb)
      else:
        x = bert_embedding[0]
        x = x.reshape(1,768)

      x = x.to("cpu")
      x_np = x.data.numpy()
    else:
      x_np = np.random.randn(1, 768)

    X_np_tsne = TSNE(n_components=128).fit_transform(x_np)
    emb_dict[words_list[idx]] = X_np_tsne

  with open('output_embeddings_dict.pickle', 'wb') as handle:
      pickle.dump(emb_dict, handle)

