import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine at a alien planet",
                     "https://images-na.ssl-images-amazon.com/images/I/91f2%2BS5ywdL._SY445_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

fast_and_furious = media.Movie("Fast And Furious",
                               "series of action films that is largely concerned with illegal street racing",
                               "https://resizing.flixster.com/kD86eJIEkoMXUZY5MgvdP4BCAZU=/206x305/v1.bTsxMTE2ODg2ODtqOzE3MzE5OzEyMDA7ODAwOzEyMDA",
                               "https://www.youtube.com/watch?v=uisBaTkQAEs")

rec2 = media.Movie("REC2",
                  "The film was shot in Barcelona, Spain and the title is an abbreviation of the word record, as it appears on a video camera",
                  "https://upload.wikimedia.org/wikipedia/en/2/27/REC2-teaser-poster.jpg",
                  "https://www.youtube.com/watch?v=dgJ4xeDUhMk")

terminator = media.Movie("Terminator",
                         "A danger man",
                         "https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg",
                         "https://www.youtube.com/watch?v=k64P4l2Wmeg")

the_hangover = media.Movie("The Hangover",
                           "The Hangover is a 2009 American black comedy ",
                           "http://www.hdmovieswatch.org/wp-content/uploads/2015/11/the-hangover-2009-free-watch-movie-online-hd.jpg",
                           "https://www.youtube.com/watch?v=tcdUhdOlz9M")

movies = [toy_story, avatar, fast_and_furious,rec2,terminator,the_hangover]
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.__name__)
