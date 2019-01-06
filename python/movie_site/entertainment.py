import media
import fresh_tomatoes

toy_story=media.Movie("Toy story","A boy and his toys which come to life", "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg","https://www.youtube.com/watch?v=0GZ4KjRwOzk")

print(toy_story.storyline)

avatar =media.Movie("Avatar","A marine on alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=6ziBFh3V1aM")

print(avatar.title)
inception= media.Movie("Inception","Thriller based on the concept of working of brain","https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", "https://www.youtube.com/watch?v=YoHD9XEInc0")
#inception.show_trailer()

movies= [toy_story,avatar,inception]
fresh_tomatoes.open_movies_page(movies)

