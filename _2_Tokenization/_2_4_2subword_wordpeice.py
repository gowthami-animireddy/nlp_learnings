from tokenizers import Tokenizer,models,pre_tokenizers,trainers
tokenizer=Tokenizer(models.WordPiece())
tokenizer.pre_tokenizer=pre_tokenizers.Whitespace()
trainer=trainers.WordPieceTrainer(vocab_size=50,special_tokens=["[PAD]","[UNK]","[CLS]","[SEP]","[MASK]"])
tokenizer.train(["data.txt"],trainer)
print(tokenizer.encode("lowest").tokens)


# ['low', '##e', '##s', '##t']

from tokenizers import Tokenizer,models,trainers
tokenizer=Tokenizer(models.WordPiece())
tokenizer.train(["data.txt"],trainers.WordPieceTrainer(vocab_size=50))
print(tokenizer.encode("lowest").tokens)