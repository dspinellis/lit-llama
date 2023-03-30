import torch
from load_data_apaca_lora import train as load_with_alpaca_lora
from prepare_data import prepare


if __name__ == "__main__":
    train_val = load_with_alpaca_lora()
    print(train_val[0])

    # ours:
    train_val_ours = prepare()
    print(train_val_ours[0])

    print(train_val_ours[0]["input_ids"].tolist())
    print(train_val[0]["input_ids"])
    #assert train_val_ours[0]["input_ids"].tolist() == train_val[0]["labels"]

    ours = [1, 13866, 338, 385, 15278, 393, 16612, 263, 3414, 29889, 14350, 263, 2933, 393, 7128, 2486, 1614, 2167, 278, 2009, 29889, 13, 13, 2277, 29937, 2799, 4080, 29901, 13, 29954, 573, 2211, 25562, 363, 7952, 292, 9045, 29891, 29889, 13, 13, 2277, 29937, 13291, 29901, 29896, 29889, 382, 271, 263, 6411, 8362, 652, 300, 322, 1207, 1854, 304, 3160, 20947, 310, 285, 21211, 322, 18655, 1849, 29889, 29871, 13, 29906, 29889, 1222, 6269, 895, 25704, 304, 3013, 596, 3573, 6136, 322, 4549, 29889, 29871, 13, 29941, 29889, 3617, 3307, 8709, 322, 7344, 263, 13747, 8709, 20410, 29889, 2]
    they = [1, 13866, 338, 385, 15278, 393, 16612, 263, 3414, 29889, 14350, 263, 2933, 393, 7128, 2486, 1614, 2167, 278, 2009, 29889, 29871, 396, 694, 25621, 29901, 382, 29945, 29900, 29896, 13, 13, 2277, 29937, 2799, 4080, 29901, 13, 29954, 573, 2211, 25562, 363, 7952, 292, 9045, 29891, 29889, 13, 13, 2277, 29937, 13291, 29901, 13, 29896, 29889, 382, 271, 263, 6411, 8362, 652, 300, 322, 1207, 1854, 304, 3160, 20947, 310, 285, 21211, 322, 18655, 1849, 29889, 29871, 13, 29906, 29889, 1222, 6269, 895, 25704, 304, 3013, 596, 3573, 6136, 322, 4549, 29889, 29871, 13, 29941, 29889, 3617, 3307, 8709, 322, 7344, 263, 13747, 8709, 20410, 29889, 2]

