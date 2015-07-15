#  07/15/15      Program created
#
#  Description:  Class Movie.  Used to store details about a given movie
#

import webbrowser

class Movie():
    """ This class can store movie related info """
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_date, rating, genre, actors):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
        self.rating = rating
        self.genre = genre
        self.actors = actors

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        
        
