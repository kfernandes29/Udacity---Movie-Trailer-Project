# Import modules
import media
import fresh_tomatoes

# Create instances of Movie class

# Toy Story
toy_story = media.Movie(
    "Toy Story",
    "A story about the adventures of a boy's toys.",
    "https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",  # NOQA
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
)

# Avatar
avatar = media.Movie(
    "Avatar",
    "A movie about humans trying to destroy another planet and their beliefs.",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)

# Hunger Games
hunger_games = media.Movie(
    "Hunger Games",
    "A city is divided and a deadly game declares a winner.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=mfmrPu43DF8"
)

# Old School
old_school = media.Movie(
    "Old School",
    "A group of middle-aged men start a fraternity.",
    "https://i.ytimg.com/vi/WHd-wFM4ov0/movieposter.jpg",
    "https://www.youtube.com/watch?v=FE4XhgHrmAE"
)

# Avengers
avengers = media.Movie(
    "The Avengers",
    "A collection of super heroes try to save the world.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/TheAvengers2012Poster.jpg/220px-TheAvengers2012Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=eOrNdBpGMv8"
)

# Black Panther
black_panther = media.Movie(
    "Black Panther",
    "The black panther must defeat his rival.",
    "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
    "https://www.youtube.com/watch?v=xjDjIWPwcPU"
)

# Create a list of movies
movies = [ avatar, hunger_games, old_school, toy_story, avengers, black_panther ]

# Pass the collection of movies to open_movies_page function of the fresh_tomatoes module
fresh_tomatoes.open_movies_page( movies )
