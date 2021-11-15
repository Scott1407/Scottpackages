#from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np


# Function to convert a sentence (list of words) into a matrix representing the words in the embedding space
# def embed_sentence_with_TF(word2vec, sentence):
#     embedded_sentence = []
#     for word in sentence:
#         if word in word2vec:
#             embedded_sentence.append(word2vec[word])

#     return np.array(embedded_sentence)


# # Function that converts a list of sentences into a list of matrices
# def embedding(word2vec, sentences):
#     embed = []

#     for sentence in sentences:
#         embedded_sentence = embed_sentence_with_TF(word2vec, sentence)
#         embed.append(embedded_sentence)

#     return embed

def hello_world():
    return "hello from my computer"


# if __name__ == "__main__":

#     X_train_embed = embedding(word2vec_transfer, X_train)
#     X_test_embed = embedding(word2vec_transfer, X_test)
#     print(X_train_embed,X_test_embed)





# # Embed the training and test sentences
# X_train_embed_2 = embedding(word2vec_transfer, X_train)
# X_test_embed_2 = embedding(word2vec_transfer, X_test)

# X_train_pad_2 = pad_sequences(X_train_embed_2,
#                               dtype='float32',
#                               padding='post',
#                               maxlen=200)
# X_test_pad_2 = pad_sequences(X_test_embed_2,
#                              dtype='float32',
#                              padding='post',
#                              maxlen=200)
