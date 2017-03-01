import media
import fresh_tomatoes

# New movie object.
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4"
    )

# New movie object.
avatar = media.Movie(
    "Avatar",
    "A marine at a alien planet",
    "https://twenemo.files.wordpress.com/2010/01/avatar-film.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )

# New movie object.
fast_and_furious = media.Movie(
    "Fast And Furious",
    "Action films that  with illegal street racing",
    "http://image.tmdb.org/t/p/original/pRlDjkBTFNgMpKLfhFb4nsPQNUl.jpg",
    "https://www.youtube.com/watch?v=uisBaTkQAEs"
    )
# New movie object.
rec2 = media.Movie(
    "REC2",
    "The film was shot in Barcelona",
    "https://upload.wikimedia.org/wikipedia/en/2/27/REC2-teaser-poster.jpg",
    "https://www.youtube.com/watch?v=dgJ4xeDUhMk"
    )
# New movie object.
terminator = media.Movie(
    "Terminator",
    "A danger man",
    "https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg",
    "https://www.youtube.com/watch?v=k64P4l2Wmeg"
    )
# New movie object.
the_hangover = media.Movie(
    "The Hangover",
    "The Hangover is a 2009 American black comedy ",
    "http://www.new-video.de/co/hangover09.jpg",
    "https://www.youtube.com/watch?v=tcdUhdOlz9M"
    )
# Array with all movies
movies = [toy_story, avatar, fast_and_furious, rec2, terminator, the_hangover]
# Call the function open movie page from the file fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
# Print the
print (media.Movie.__name__)
