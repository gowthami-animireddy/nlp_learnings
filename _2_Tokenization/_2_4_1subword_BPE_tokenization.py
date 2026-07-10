from tokenizers import Tokenizer,models,pre_tokenizers,trainers
tokenizer=Tokenizer(models.BPE())
tokenizer.pre_tokenizer=pre_tokenizers.Whitespace()
tokenizer.train(["data.txt"],trainers.BpeTrainer(vocab_size=50))
print(tokenizer.encode("lowest").tokens)