from tokenizers import Tokenizer,models,trainers
tokenizer=Tokenizer(models.Unigram())
tokenizer.train(["data.txt"],trainers.UnigramTrainer(vocab_size=50))
print(tokenizer.encode("lowest").tokens)


# ['low', 'e', 's', 't']

from tokenizers import Tokenizer,models,trainers
tokenizer=Tokenizer(models.Unigram())
trainer=trainers.UnigramTrainer(vocab_size=50)
tokenizer.train(["data.txt"],trainer)
print(tokenizer.encode("lowest").tokens)