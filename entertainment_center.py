import media
import fresh_tomatoes

toy_story =media.Movie("Toy Story", "A story of boy",
                       "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

#toy_story.show_trailer()

movies = [toy_story]
fresh_tomatoes.open_movies_page(movies)
