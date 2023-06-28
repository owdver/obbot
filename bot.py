import os
import random
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# Create a new Pyrogram client
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Handler for /start command
@app.on_message(filters.command("start"))
def start_command(client: Client, message: Message):
    client.send_message(
        chat_id=message.chat.id,
        text="Hello! I'm your Telegram bot. How can I assist you?"
    )

# Handler for /echo command
@app.on_message(filters.command("echo"))
def echo_command(client: Client, message: Message):
    text = " ".join(message.command[1:])
    client.send_message(
        chat_id=message.chat.id,
        text=text
    )

# Handler for /caps command
@app.on_message(filters.command("caps"))
def caps_command(client: Client, message: Message):
    text = " ".join(message.command[1:])
    caps_text = text.upper()
    client.send_message(
        chat_id=message.chat.id,
        text=caps_text
    )

# Handler for /reverse command
@app.on_message(filters.command("reverse"))
def reverse_command(client: Client, message: Message):
    text = " ".join(message.command[1:])
    reversed_text = text[::-1]
    client.send_message(
        chat_id=message.chat.id,
        text=reversed_text
    )

# Handler for /info command
@app.on_message(filters.command("info"))
def info_command(client: Client, message: Message):
    info = f"Chat ID: {message.chat.id}\nUser ID: {message.from_user.id}"
    client.send_message(
        chat_id=message.chat.id,
        text=info
    )

# Handler for /dice command
@app.on_message(filters.command("dice"))
def dice_command(client: Client, message: Message):
    client.send_dice(
        chat_id=message.chat.id
    )

# Handler for /coinflip command
@app.on_message(filters.command("coinflip"))
def coinflip_command(client: Client, message: Message):
    coin = "Heads" if random.randint(0, 1) == 0 else "Tails"
    client.send_message(
        chat_id=message.chat.id,
        text=coin
    )

# Handler for /randomnumber command
@app.on_message(filters.command("randomnumber"))
def randomnumber_command(client: Client, message: Message):
    args = message.command[1:]
    if len(args) == 2 and args[0].isdigit() and args[1].isdigit():
        start_range = int(args[0])
        end_range = int(args[1])
        random_num = random.randint(start_range, end_range)
        client.send_message(
            chat_id=message.chat.id,
            text=str(random_num)
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Invalid command. Please provide two integer arguments."
        )

# Handler for /dog command
@app.on_message(filters.command("dog"))
def dog_command(client: Client, message: Message):
    # You can replace this with your own method of retrieving a random dog image or use an API
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    if response.status_code == 200:
        dog_image_url = response.json()["message"]
        client.send_photo(
            chat_id=message.chat.id,
            photo=dog_image_url,
            caption="Woof! Here's a random dog for you!"
        )

# Handler for /cat command
@app.on_message(filters.command("cat"))
def cat_command(client: Client, message: Message):
    # You can replace this with your own method of retrieving a random cat image or use an API
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    if response.status_code == 200:
        cat_image_url = response.json()[0]["url"]
        client.send_photo(
            chat_id=message.chat.id,
            photo=cat_image_url,
            caption="Meow! Here's a random cat for you!"
        )

# Handler for /quote command
@app.on_message(filters.command("quote"))
def quote_command(client: Client, message: Message):
    # You can replace this with your own method of retrieving a random quote or use an API
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        quote_data = response.json()
        quote = f"{quote_data['content']} - {quote_data['author']}"
        client.send_message(
            chat_id=message.chat.id,
            text=quote
        )

# Handler for /gif command
@app.on_message(filters.command("gif"))
def gif_command(client: Client, message: Message):
    # You can replace this with your own method of retrieving a random GIF or use an API
    response = requests.get("https://api.giphy.com/v1/gifs/random?api_key=YOUR_API_KEY&rating=g")
    if response.status_code == 200:
        gif_data = response.json()["data"]
        gif_url = gif_data["image_original_url"]
        client.send_animation(
            chat_id=message.chat.id,
            animation=gif_url
        )

# Handler for /joke command
@app.on_message(filters.command("joke"))
def joke_command(client: Client, message: Message):
    # You can replace this with your own method of retrieving a random joke or use an API
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke_data = response.json()
        joke = f"{joke_data['setup']}\n{joke_data['punchline']}"
        client.send_message(
            chat_id=message.chat.id,
            text=joke
        )

# Handler for /weather command
@app.on_message(filters.command("weather"))
def weather_command(client: Client, message: Message):
    # You can replace this with your own method of retrieving weather information or use an API
    response = requests.get("https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=New%20York")
    if response.status_code == 200:
        weather_data = response.json()["current"]
        weather_info = f"Weather: {weather_data['condition']['text']}\nTemperature: {weather_data['temp_c']}°C"
        client.send_message(
            chat_id=message.chat.id,
            text=weather_info
        )

# Handler for /news command
@app.on_message(filters.command("news"))
def news_command(client: Client, message: Message):
    # You can replace this with your own method of retrieving news articles or use an API
    response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY")
    if response.status_code == 200:
        news_data = response.json()["articles"]
        random_article = random.choice(news_data)
        news_title = random_article["title"]
        news_description = random_article["description"]
        news_info = f"Title: {news_title}\nDescription: {news_description}"
        client.send_message(
            chat_id=message.chat.id,
            text=news_info
        )

# Handler for /calculate command
@app.on_message(filters.command("calculate"))
def calculate_command(client: Client, message: Message):
    try:
        expression = " ".join(message.command[1:])
        result = eval(expression)
        client.send_message(
            chat_id=message.chat.id,
            text=str(result)
        )
    except Exception as e:
        client.send_message(
            chat_id=message.chat.id,
            text="Invalid expression."
        )

# Handler for /wiki command
@app.on_message(filters.command("wiki"))
def wiki_command(client: Client, message: Message):
    query = " ".join(message.command[1:])
    response = requests.get(f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json")
    if response.status_code == 200:
        data = response.json()
        if "query" in data and "search" in data["query"]:
            search_results = data["query"]["search"]
            if len(search_results) > 0:
                first_result = search_results[0]
                page_title = first_result["title"]
                page_url = f"https://en.wikipedia.org/wiki/{page_title.replace(' ', '_')}"
                client.send_message(
                    chat_id=message.chat.id,
                    text=f"More about '{query}':\n{page_url}"
                )
            else:
                client.send_message(
                    chat_id=message.chat.id,
                    text="No results found."
                )
        else:
            client.send_message(
                chat_id=message.chat.id,
                text="No results found."
            )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Failed to fetch results."
        )

# Handler for /qr command
@app.on_message(filters.command("qr"))
def qr_command(client: Client, message: Message):
    text = " ".join(message.command[1:])
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?data={text}&size=200x200"
    client.send_photo(
        chat_id=message.chat.id,
        photo=qr_url,
        caption="Here's the QR code for the provided text."
    )

# Handler for /translate command
@app.on_message(filters.command("translate"))
def translate_command(client: Client, message: Message):
    text = " ".join(message.command[1:])
    # Use a language translation API to translate the text
    translated_text = translate(text)
    client.send_message(
        chat_id=message.chat.id,
        text=translated_text
    )

# Handler for /recognize command
@app.on_message(filters.command("recognize"))
def recognize_command(client: Client, message: Message):
    # Check if the message contains an image
    if message.reply_to_message and message.reply_to_message.photo:
        photo = message.reply_to_message.photo[-1]
        file_id = photo.file_id
        # Use an image recognition API to analyze and recognize the image
        recognition_result = recognize_image(file_id)
        client.send_message(
            chat_id=message.chat.id,
            text=recognition_result
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Please reply to an image to recognize."
        )

# Handler for /shorten command
@app.on_message(filters.command("shorten"))
def shorten_command(client: Client, message: Message):
    long_url = " ".join(message.command[1:])
    # Use a URL shortening service API to generate a shortened URL
    shortened_url = shorten_url(long_url)
    client.send_message(
        chat_id=message.chat.id,
        text=shortened_url
    )

# Handler for /reminder command
@app.on_message(filters.command("reminder"))
def reminder_command(client: Client, message: Message):
    # Implement logic to set reminders or alarms
    # ...

# Handler for /reddit command
@app.on_message(filters.command("reddit"))
def reddit_command(client: Client, message: Message):
    subreddit = " ".join(message.command[1:])
    # Use the Reddit API to fetch random posts or top posts from a subreddit
    reddit_posts = fetch_reddit_posts(subreddit)
    if reddit_posts:
        post = random.choice(reddit_posts)
        post_title = post["title"]
        post_url = post["url"]
        client.send_message(
            chat_id=message.chat.id,
            text=f"{post_title}\n{post_url}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text=f"No posts found in r/{subreddit}."
        )

# Handler for /definition command
@app.on_message(filters.command("definition"))
def definition_command(client: Client, message: Message):
    word = " ".join(message.command[1:])
    # Use a dictionary API to retrieve word definitions
    definitions = get_word_definitions(word)
    if definitions:
        definition_text = "\n".join(definitions)
        client.send_message(
            chat_id=message.chat.id,
            text=definition_text
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text=f"No definitions found for '{word}'."
        )

# Handler for /synonym command
@app.on_message(filters.command("synonym"))
def synonym_command(client: Client, message: Message):
    word = " ".join(message.command[1:])
    # Use a thesaurus API to retrieve synonyms
    synonyms = get_word_synonyms(word)
    if synonyms:
        synonym_text = ", ".join(synonyms)
        client.send_message(
            chat_id=message.chat.id,
            text=f"Synonyms of '{word}':\n{synonym_text}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text=f"No synonyms found for '{word}'."
        )

# Handler for /antonym command
@app.on_message(filters.command("antonym"))
def antonym_command(client: Client, message: Message):
    word = " ".join(message.command[1:])
    # Use a thesaurus API to retrieve antonyms
    antonyms = get_word_antonyms(word)
    if antonyms:
        antonym_text = ", ".join(antonyms)
        client.send_message(
            chat_id=message.chat.id,
            text=f"Antonyms of '{word}':\n{antonym_text}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text=f"No antonyms found for '{word}'."
        )

# Handler for /movie command
@app.on_message(filters.command("movie"))
def movie_command(client: Client, message: Message):
    # Use a movie API to fetch random movie details or recommendations
    movie_info = get_random_movie()
    if movie_info:
        title = movie_info["title"]
        year = movie_info["year"]
        genre = movie_info["genre"]
        rating = movie_info["rating"]
        client.send_message(
            chat_id=message.chat.id,
            text=f"Title: {title}\nYear: {year}\nGenre: {genre}\nRating: {rating}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Failed to fetch movie information."
        )

# Handler for /music command
@app.on_message(filters.command("music"))
def music_command(client: Client, message: Message):
    # Use a music API to fetch random music recommendations or details
    music_info = get_random_music()
    if music_info:
        title = music_info["title"]
        artist = music_info["artist"]
        genre = music_info["genre"]
        client.send_message(
            chat_id=message.chat.id,
            text=f"Title: {title}\nArtist: {artist}\nGenre: {genre}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Failed to fetch music information."
        )

# Handler for /recipe command
@app.on_message(filters.command("recipe"))
def recipe_command(client: Client, message: Message):
    # Use a recipe API to fetch random recipes or details
    recipe_info = get_random_recipe()
    if recipe_info:
        title = recipe_info["title"]
        ingredients = ", ".join(recipe_info["ingredients"])
        instructions = recipe_info["instructions"]
        client.send_message(
            chat_id=message.chat.id,
            text=f"Title: {title}\nIngredients: {ingredients}\nInstructions: {instructions}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Failed to fetch recipe information."
        )

# Handler for /trivia command
@app.on_message(filters.command("trivia"))
def trivia_command(client: Client, message: Message):
    # Use a trivia API to fetch a random trivia question
    question, answer = get_random_trivia()
    client.send_message(
        chat_id=message.chat.id,
        text=f"Question: {question}\nAnswer: {answer}"
    )

# Handler for /riddle command
@app.on_message(filters.command("riddle"))
def riddle_command(client: Client, message: Message):
    # Use a riddle API to fetch a random riddle
    riddle, answer = get_random_riddle()
    client.send_message(
        chat_id=message.chat.id,
        text=f"Riddle: {riddle}\nAnswer: {answer}"
    )

# Handler for /fact command
@app.on_message(filters.command("fact"))
def fact_command(client: Client, message: Message):
    # Use a fact API to fetch a random interesting fact
    fact = get_random_fact()
    client.send_message(
        chat_id=message.chat.id,
        text=f"Did you know?\n{fact}"
    )

# Handler for /quoteoftheday command
@app.on_message(filters.command("quoteoftheday"))
def quote_of_the_day_command(client: Client, message: Message):
    # Use a quote API to fetch the quote of the day
    quote = get_quote_of_the_day()
    client.send_message(
        chat_id=message.chat.id,
        text=f"Quote of the Day:\n{quote}"
    )

# Handler for /horoscope command
@app.on_message(filters.command("horoscope"))
def horoscope_command(client: Client, message: Message):
    sign = message.command[1].lower() if len(message.command) > 1 else None
    if sign:
        # Use a horoscope API to fetch the horoscope for the given sign
        horoscope = get_horoscope(sign)
        if horoscope:
            client.send_message(
                chat_id=message.chat.id,
                text=f"Horoscope for {sign.capitalize()}:\n{horoscope}"
            )
        else:
            client.send_message(
                chat_id=message.chat.id,
                text="Failed to fetch horoscope for the given sign."
            )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Please provide a valid zodiac sign with the command."
        )

# Handler for /advice command
@app.on_message(filters.command("advice"))
def advice_command(client: Client, message: Message):
    # Use an advice API to fetch a random advice
    advice = get_random_advice()
    client.send_message(
        chat_id=message.chat.id,
        text=f"Advice: {advice}"
    )

# Handler for /insult command
@app.on_message(filters.command("insult"))
def insult_command(client: Client, message: Message):
    # Use an insult API to fetch a random insult
    insult = get_random_insult()
    client.send_message(
        chat_id=message.chat.id,
        text=f"Insult: {insult}"
    )

# Handler for /compliment command
@app.on_message(filters.command("compliment"))
def compliment_command(client: Client, message: Message):
    # Use a compliment API to fetch a random compliment
    compliment = get_random_compliment()
    client.send_message(
        chat_id=message.chat.id,
        text=f"Compliment: {compliment}"
    )

# Handler for /poll command
@app.on_message(filters.command("poll"))
def poll_command(client: Client, message: Message):
    question = " ".join(message.command[1:])
    options = ["Option 1", "Option 2", "Option 3"]  # Replace with your own options
    client.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options
    )

# Handler for /quotebyauthor command
@app.on_message(filters.command("quotebyauthor"))
def quote_by_author_command(client: Client, message: Message):
    author = " ".join(message.command[1:])
    quote = get_quote_by_author(author)
    if quote:
        client.send_message(
            chat_id=message.chat.id,
            text=f"Quote by {author}:\n{quote}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="No quotes found for the given author."
        )

# Handler for /factbytopic command
@app.on_message(filters.command("factbytopic"))
def fact_by_topic_command(client: Client, message: Message):
    topic = " ".join(message.command[1:])
    fact = get_fact_by_topic(topic)
    if fact:
        client.send_message(
            chat_id=message.chat.id,
            text=f"Fact about {topic}:\n{fact}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="No facts found for the given topic."
        )

# Handler for /motivation command
@app.on_message(filters.command("motivation"))
def motivation_command(client: Client, message: Message):
    quote = get_random_motivational_quote()
    client.send_message(
        chat_id=message.chat.id,
        text=f"Motivational Quote:\n{quote}"
    )

# Handler for /define command
@app.on_message(filters.command("define"))
def define_command(client: Client, message: Message):
    word = " ".join(message.command[1:])
    definition = get_definition(word)
    if definition:
        client.send_message(
            chat_id=message.chat.id,
            text=f"Definition of {word}:\n{definition}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="No definition found for the given word."
        )

# Handler for /synonyms command
@app.on_message(filters.command("synonyms"))
def synonyms_command(client: Client, message: Message):
    word = " ".join(message.command[1:])
    synonyms = get_synonyms(word)
    if synonyms:
        client.send_message(
            chat_id=message.chat.id,
            text=f"Synonyms of {word}:\n{', '.join(synonyms)}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="No synonyms found for the given word."
        )

# Handler for /antonyms command
@app.on_message(filters.command("antonyms"))
def antonyms_command(client: Client, message: Message):
    word = " ".join(message.command[1:])
    antonyms = get_antonyms(word)
    if antonyms:
        client.send_message(
            chat_id=message.chat.id,
            text=f"Antonyms of {word}:\n{', '.join(antonyms)}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="No antonyms found for the given word."
        )

# Handler for /bookrecommendation command
@app.on_message(filters.command("bookrecommendation"))
def book_recommendation_command(client: Client, message: Message):
    book = get_random_book_recommendation()
    client.send_message(
        chat_id=message.chat.id,
        text=f"Book Recommendation:\n{book}"
    )

# Handler for /joke command
@app.on_message(filters.command("joke"))
def joke_command(client: Client, message: Message):
    joke = get_random_joke()
    client.send_message(
        chat_id=message.chat.id,
        text=f"Joke:\n{joke}"
    )

# Handler for /weather command
@app.on_message(filters.command("weather"))
def weather_command(client: Client, message: Message):
    location = " ".join(message.command[1:])
    weather_info = get_weather_info(location)
    if weather_info:
        client.send_message(
            chat_id=message.chat.id,
            text=f"Weather information for {location}:\n{weather_info}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Failed to fetch weather information for the given location."
        )

# Handler for /lyrics command
@app.on_message(filters.command("lyrics"))
def lyrics_command(client: Client, message: Message):
    song = " ".join(message.command[1:])
    lyrics = get_song_lyrics(song)
    if lyrics:
        client.send_message(
            chat_id=message.chat.id,
            text=f"Lyrics for {song}:\n{lyrics}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Failed to fetch lyrics for the given song."
        )

# Handler for /cat command
@app.on_message(filters.command("cat"))
def cat_command(client: Client, message: Message):
    cat_image_url = get_random_cat_image()
    if cat_image_url:
        client.send_photo(
            chat_id=message.chat.id,
            photo=cat_image_url,
            caption="Here's a cute cat for you!"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Failed to fetch a cat image."
        )

# Handler for /dog command
@app.on_message(filters.command("dog"))
def dog_command(client: Client, message: Message):
    dog_image_url = get_random_dog_image()
    if dog_image_url:
        client.send_photo(
            chat_id=message.chat.id,
            photo=dog_image_url,
            caption="Here's a cute dog for you!"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Failed to fetch a dog image."
        )

# Handler for /randomnumber command
@app.on_message(filters.command("randomnumber"))
def random_number_command(client: Client, message: Message):
    min_value = int(message.command[1]) if len(message.command) > 1 else 1
    max_value = int(message.command[2]) if len(message.command) > 2 else 100
    random_number = get_random_number(min_value, max_value)
    client.send_message(
        chat_id=message.chat.id,
        text=f"Random number between {min_value} and {max_value}: {random_number}"
    )

# Handler for /fact command
@app.on_message(filters.command("fact"))
def fact_command(client: Client, message: Message):
    fact = get_random_fact()
    client.send_message(
        chat_id=message.chat.id,
        text=f"Random Fact:\n{fact}"
    )

# Handler for /image command
@app.on_message(filters.command("image"))
def image_command(client: Client, message: Message):
    query = " ".join(message.command[1:])
    image_url = get_random_image(query)
    if image_url:
        client.send_photo(
            chat_id=message.chat.id,
            photo=image_url,
            caption="Here's a random image for you!"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="No image found for the given query."
        )

# Handler for /video command
@app.on_message(filters.command("video"))
def video_command(client: Client, message: Message):
    query = " ".join(message.command[1:])
    video_url = get_random_video(query)
    if video_url:
        client.send_video(
            chat_id=message.chat.id,
            video=video_url,
            caption="Here's a random video for you!"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="No video found for the given query."
        )

# Handler for /translate command
@app.on_message(filters.command("translate"))
def translate_command(client: Client, message: Message):
    text = " ".join(message.command[1:])
    translated_text = translate(text)
    if translated_text:
        client.send_message(
            chat_id=message.chat.id,
            text=f"Translated Text:\n{translated_text}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Failed to translate the given text."
        )

# Handler for /quoteoftheday command
@app.on_message(filters.command("quoteoftheday"))
def quote_of_the_day_command(client: Client, message: Message):
    quote = get_quote_of_the_day()
    client.send_message(
        chat_id=message.chat.id,
        text=f"Quote of the Day:\n{quote}"
    )
# Handler for /summary command
@app.on_message(filters.command("summary"))
def summary_command(client: Client, message: Message):
    query = " ".join(message.command[1:])
    summary = get_wikipedia_summary(query)
    if summary:
        client.send_message(
            chat_id=message.chat.id,
            text=f"Summary of '{query}':\n{summary}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Failed to fetch the summary."
        )
# Handler for /youtube command
@app.on_message(filters.command("youtube"))
def youtube_command(client: Client, message: Message):
    query = " ".join(message.command[1:])
    video_url = search_youtube_videos(query)
    if video_url:
        client.send_message(
            chat_id=message.chat.id,
            text=f"Top search result for '{query}':\n{video_url}"
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="No videos found for the given query."
        )
# Handler for /chuckjoke command
@app.on_message(filters.command("chuckjoke"))
def chuck_joke_command(client: Client, message: Message):
    joke = get_chuck_norris_joke()
    client.send_message(
        chat_id=message.chat.id,
        text=joke
    )
# Handler for /reddit command
@app.on_message(filters.command("reddit"))
def reddit_command(client: Client, message: Message):
    subreddit = message.command[1]
    post = get_random_reddit_post(subreddit)
    if post:
        client.send_message(
            chat_id=message.chat.id,
            text=post
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Failed to fetch a post from the specified subreddit."
        )



# Run the bot
app.run()
