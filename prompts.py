import openai
import os
openai.api_key = os.environ.get("OPENAI_API_KEY")

def prompt_maker(genre, topic):
    print('prompt_maker', genre, topic)
    if topic != "":
        if genre == "Article":
            prompt = f"prompt: write a long, simple article about the electronic transportation revolution for a second grader--> completion: It seems like the current trend in transportation is away from engines that burn fuel and instead are powered by electric motors. This method of getting about has all sorts of benefits. The one that is most pronounced is that these electric vehicles (EVs) do not pollute the air with waste gases from burning fuels like gasoline or diesel. In addition, electric motors are much quieter, so the switch to electric vehicles is helping to eliminate both air pollution and noise pollution. Electric transportation has another major benefit in that the electricity can come from green sources. Solar or wind power can be used to charge an electric vehicle, and it does not cost anything. Instead of buying gasoline or relying on other energy sources, people can simply use these much cheaper forms of energy to power EVs. It is for this reason that making the transition to EVs is considered one of the best things that can be done to achieve energy independence. Electric vehicles have a much longer history than most people recall. Most subways, trams, and trolleys in cities throughout the world use electricity as their power source. The first electric streetcar was introduced in Berlin, Germany, in 1881. These types of transportation use collector systems to power them. The latest electric scooters, cars, and trucks use batteries, though. With batteries comes much greater freedom to move about. Vehicles relying on collector systems need to stay on a particular rail or track, as that is where their power is coming from. Electric vehicles are not confined to land, though. Today, there are companies that manufacture electric boats that are equipped with solar panels. As the boats are moored in the sun, their batteries get charged. The boats come in different sizes, from small pleasure boats to larger ferries. The best part about them is they never need to be filled with fuel! The air above us is also a place where electric vehicles move about. Electric drones are very popular today, and they are used for all sorts of tasks. Farmers use them to survey their fields, and film companies use them for aerial shots. Compared to hiring a helicopter or airplane, these drones are considerably more cost-effective. As for taking passengers in flight, electric airplane technology is advancing, although not nearly as quickly as land or water-based vehicles. In the past decade, the airplanes Solar Impulse 1 and Solar Impulse 2 have proven that round-the-world flight using only solar power is possible. While it may take a long time before such electric airplanes find a commercial use, these airplanes gave proof of concept. Due to greater awareness of environmental issues such as climate change, the demand for all kinds of electric transportation is likely to grow to the point where these vehicles become the norm. The internal combustion engine, which helped transform the world by making long-distance transportation easy and inexpensive, is on its way out. In its place will be cleaner, quieter electric vehicles. They will help us not only breathe better, but sleep better as well.--> prompt: Write a long, easy article about {topic}--> completion:"
            # prompt = f"prompt: write a very long easy article about the history of electric cars--> completion: Back in the 1970s, people started talking about electric cars as the wave of the future. There were some electric cars that were manufactured, but they didn’t sell very well. The reason for this was because they didn’t have technology that was good enough to compete with gas-powered cars. Because of this, they didn’t sell very well on the market, and most carmakers decided not to continue making them. Now, about 50 years later, all of this has changed. People today want electric cars because they know that they are better for the environment. It will be interesting to see what the world will be like in 20 years from now. It may be true that gas stations and gas-powered cars become things of the past.--> prompt: Write a long, easy article about {topic}--> completion:"
            return prompt
        elif genre == "Dialog":
            prompt = f"""Write a dialog about buying an electric scooter-->Dialog:
    Jolie: Guess what? I was talking to a dealer today, and I’m buying an electric scooter.
    Adan: Really? Why did you do that? Are you worried about the environmental aspects of riding a regular scooter that runs on gasoline?
    Jolie: Well, yes. That’s the main reason. However, electric motor technology and batteries have gotten much better in the past 20 years. In fact, for what I need, an electric scooter is best.
    Adan: I hope you got the one that goes the fastest! I wanted to get one myself, but the ones I saw were a lot slower than gasoline powered scooters, and I didn’t think they were capable of going nearly as far.
    Jolie: The one that I bought, a Maxi, is plenty fast. Besides, it can travel up to 170 kilometers on a full battery. The longest I have to travel normally is only about 15 kilometers or so. There are also lots of places where I can exchange a spent battery for a fully-charged one.
    Adan: Are you able to charge it at home as well?
    Jolie: Yes. There is a special charger that I can use to charge a battery overnight if I want to.
    Adan: That sounds ideal. You won’t have to go buy gas anymore!
    Jolie: I know. I love that. But I also like the fact that the motor is quite powerful. When I test-drove the one that I’m getting, it felt just as fast as my previous scooter which ran on gas.
    Adan: That’s good. When will you take delivery of your new scooter?
    Jolie: The soonest I should get it is in two weeks. I could have gotten a different one a little bit sooner, but the color I wanted wasn’t immediately available.
    Adan: Well, congratulations for getting it. It’s another small step towards helping to save our planet!
    Write a very, very, very, very long dialog about {topic}-->Dialog:"""
            return prompt
# add "simple" to the prompt get that Taiwan style writing
# adding easy makes it easy, but always short

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
    if genre=="Dialog":
        temperature = 0.95
        frequency_penalty = 0.25
    if genre == "write_questions":
        temperature = 0.70
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