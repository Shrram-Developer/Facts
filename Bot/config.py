import openai
import os
from pathlib import Path
import requests

openai.api_key = "OPENAI-BOT-TOKEN"
TOKEN = "TELEGRAM-BOT-TOKEN"



technologies_request = "Tell me an interesting fact about technology. Related to technology and innovation, such as inventions, developments, progress in various fields of technology, etc."
history_request = "Tell me an interesting fact about history. Associated with past events, such as dates, places, people who did something, and so on."
geography_request = "Tell me an interesting fact about geography. Related to the location of geographic features such as rivers, countries, cities, mountains, etc."
science_request = "Tell me an interesting fact about science. Related to the natural sciences, such as physics, chemistry, biology, astronomy, etc."
culture_request = "Tell me an interesting fact about culture. Associated with culture and art, such as music, cinema, literature, theater, traditions, customs, and more."
geology_request = "Tell me an interesting fact about geology. Associated with the study of the structure, composition, origin and evolution of the Earth, its geological processes and phenomena, about minerals, mineral deposits, geological processes such as volcanic eruptions, earthquakes, rocks, the formation and change of mountain ranges, deserts, oceans, etc."

hi = 'Welcome!\n\nThis bot is created to enhance your knowledge by providing various facts. The facts are generated using the ChatGPT 3.5 AI, and images accompanying the facts are generated using the DALLE 2 AI.\n\nTo begin, choose the mode of receiving facts: "Fact with image" or "Fact without image."In the "Fact without image" mode, you will receive text-only facts, but the speed will be significantly faster.\n\nAfter selecting the mode, you can choose a category for the facts from the following list: Technologies, Geography, Science, History, Culture, Geology. Select the category that interests you to receive a fact related to the chosen theme.\n\nIf you wish to change the mode simply type the /start command again.\n\nEnjoy exploring the world of knowledge!'

dir_path = Path.cwd()

def fact_image(request):
    prompt = str(request + 'WRITE ONLY THIS WAY: "FACT"' + 'ONLY SAFE CONTENT')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    caption = response.choices[0].text

    image_response = str(caption)
    response = openai.Image.create(
        prompt=image_response,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    response = requests.get(image_url)
    filename = os.path.join("../Images", "image.jpg")
    os.makedirs("../Images", exist_ok=True)
    with open(filename, "wb") as file:
        file.write(response.content)
    png_file = Path(dir_path, '../Images', 'image.jpg')
    return png_file, caption

def fact(request):
    prompt = request, 'WRITE ONLY THIS WAY: "FACT"', 'ONLY SAFE CONTENT'
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    text = response.choices[0].text
    return str(text)

