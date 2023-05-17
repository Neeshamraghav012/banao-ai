import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Vanilla davinci model
"""

completion = openai.Completion() 

question = "How are you?"

prompt = f'Human:{question}\nAI:'

response = completion.create(
      prompt = prompt,engine = "davinci",stop = ["\nHuman"],temperature = 0.9,
      top_p =1,best_of=1,
      max_tokens=150
  )


answer = response.choices[0].text.strip()

print(answer)

"""

# Fine Tuned version of davinci
completion = openai.Completion() 

question = "How are you?"

prompt = f'Human:{question}\nAI:'

response = completion.create(
      prompt = prompt,engine = "davinci:ft-square-share-pvt-ltd-2023-05-17-10-26-42",stop = ["\nHuman"],temperature = 0.9,
      top_p =1,best_of=1,
      max_tokens=150
  )


answer = response.choices[0].text.strip()

print(answer[:100])
