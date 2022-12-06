import openai
import os
openai.api_key = os.environ.get("OPENAI_API_KEY")

def prompt_maker(genre, topic, words):
    # if len(words)>0:
    prompt = f"""write a very long and easy {genre} about {topic} using these words: {words}"""
    # else:
    #     prompt = f"""write a very long and easy {genre} about {topic}"""

    return prompt
# add "simple" to the prompt get that Taiwan style writing
# adding easy makes it easy, but always short

# def picture_maker(prompt):


def question_writer(genre,text):
    questions_prompt = f"""{text}
Write 8 multiple choice TOEIC-type questions with 4 answer choices about the {genre}:
Questions:"""
    print("questions_prompt", questions_prompt)
    return questions_prompt

def model_builder(genre, prompt):
    if genre=="Article":
        temperature = 0.95
        frequency_penalty = 0
    elif genre=="Dialog":
        temperature = 0.95
        frequency_penalty = 0.25
    elif genre == "write_questions":
        temperature = 0.70
        frequency_penalty = 0
    else:
        temperature = 0.8
        frequency_penalty = 0
    response = openai.Completion.create(
        model="text-davinci-003",
        # model = "text-curie-001",
        prompt = prompt,
        temperature=temperature,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=frequency_penalty,
        presence_penalty=0.0
        )
    print (response)
    text = response.choices[0].text
    return text