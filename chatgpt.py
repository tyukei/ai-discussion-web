import openai


# Your API key here
openai.api_key = "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"

def run(prompt,role):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content']



