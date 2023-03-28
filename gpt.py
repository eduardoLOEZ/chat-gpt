import openai

openai.api_key = "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"

while True:
    text = input("Introduce algo: ")
    if text  == "break":
        break
    
    completion = openai.Completion.create(engine="text-davinci-003",
                                           prompt=text,
                                           max_tokens=2048)
    print(completion.choices[0].text)
