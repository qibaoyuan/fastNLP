import numpy as np
import torch
from torch import nn as nn

from ..core.vocabulary import Vocabulary


def _construct_char_vocab_from_vocab(vocab:Vocabulary, min_freq:int=1):
    """
    给定一个word的vocabulary生成character的vocabulary.

    :param vocab: 从vocab
    :param min_freq:
    :return:
    """
    char_vocab = Vocabulary(min_freq=min_freq)
    for word, index in vocab:
        if not vocab._is_word_no_create_entry(word):
            char_vocab.add_word_lst(list(word))
    return char_vocab


def get_embeddings(init_embed):
    """
    根据输入的init_embed生成nn.Embedding对象。

    :param init_embed: 可以是 tuple:(num_embedings, embedding_dim), 即embedding的大小和每个词的维度;也可以传入
        nn.Embedding 对象, 此时就以传入的对象作为embedding; 传入np.ndarray也行，将使用传入的ndarray作为作为Embedding初始
        化; 传入orch.Tensor, 将使用传入的值作为Embedding初始化。
    :return nn.Embedding embeddings:
    """
    if isinstance(init_embed, tuple):
        res = nn.Embedding(
            num_embeddings=init_embed[0], embedding_dim=init_embed[1])
        nn.init.uniform_(res.weight.data, a=-np.sqrt(3/res.weight.data.size(1)),
                         b=np.sqrt(3/res.weight.data.size(1)))
    elif isinstance(init_embed, nn.Module):
        res = init_embed
    elif isinstance(init_embed, torch.Tensor):
        res = nn.Embedding.from_pretrained(init_embed, freeze=False)
    elif isinstance(init_embed, np.ndarray):
        init_embed = torch.tensor(init_embed, dtype=torch.float32)
        res = nn.Embedding.from_pretrained(init_embed, freeze=False)
    else:
        raise TypeError(
            'invalid init_embed type: {}'.format((type(init_embed))))
    return res