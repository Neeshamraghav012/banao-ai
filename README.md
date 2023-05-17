# banao-ai

Add more data in the banao.jsonl file. (The file format should be same as the current data).
Make sure to add your open ai api key.

# Fine Tuning
openai api fine_tunes.create -t banao.jsonl -m davinci

# Testing
openai api completions.create -m davinci:ft-square-share-pvt-ltd-2023-05-17-10-26-42 -p "How are you?"

(The name of the model will be different in your case.)
