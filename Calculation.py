from jiwer import wer

reference = "hello world"
hypothesis = "hello bro"

error = wer(reference, hypothesis)
print(error)