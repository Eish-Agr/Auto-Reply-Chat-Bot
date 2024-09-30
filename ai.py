from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="Enter your API Key",
)
command = ""
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Eish who speaks hindi and English. He is from India. You analyze chat history and respond like Eish. output should be the next chat response as Eish."},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)