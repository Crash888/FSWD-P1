#  07/15/15     Program created
#
#  Description: Create and display an HTML page listing my favourite movies.  Users can click
#               on the poster for more movie details or watch a movie trailer by pressing the
#               'Watch Trailer' button.
#
#  Run this program to launch the application.
#  
#  Requires files:  media.py and fresh_tomatoes.py to be in the same directory

import media
import fresh_tomatoes

#  Create movie list
toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio",
                        "11/22/1995",
                        "G",
                        "Animation, Adventure, Comedy",
                        "Tom Hanks, Tim Allen")

avatar = media.Movie("Avatar",
                     "A Paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "12/18/2009",
                     "PG-13",
                     "Action, Adventure, Fantasy",
                     "Sam Worthington, Zoe Saldana")

die_hard = media.Movie("Die Hard",
                       "John McClane, officer of the NYPD, tries to save wife Holly Gennaro and several others, taken hostage by German terrorist Hans Gruber during a Christmas party at the Nakatomi Plaza in Los Angeles.",
                       "https://upload.wikimedia.org/wikipedia/en/7/7e/Die_hard.jpg",
                       "https://www.youtube.com/watch?v=2TQ-pOvI6Xo",
                       "7/20/1988",
                       "R",
                       "Action, Thriller",
                       "Bruce Willis, Alan Rickman")

terminator_2 = media.Movie("Terminator 2: Judgment Day",
                           "A cyborg, identical to the one who failed to kill Sarah Connor, must now protect her young son, John Connor, from a more advanced cyborg, made out of liquid metal.",
                           "https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg",
                           "https://www.youtube.com/watch?v=eajuMYNYtuY",
                           "7/3/1991",
                           "R",
                           "Action, Sci-Fi",
                           "Arnold Schwarzenegger, Linda Hamilton, Robert Patrick")

zoolander = media.Movie("Zoolander",
                        "At the end of his career, a clueless fashion model is brainwashed to kill the Prime Minister of Malaysia.",
                        "https://upload.wikimedia.org/wikipedia/en/7/7c/Movie_poster_zoolander.jpg",
                        "https://www.youtube.com/watch?v=MaEeSJZYkpY",
                        "9/28/2001",
                        "PG-13",
                        "Comedy",
                        "Ben Stiller, Owen Wilson, Will Ferrell")

kung_fu_hustle = media.Movie ("Kung Fu Hustle",
                              "In Shanghai, China in the 1940s, a wannabe gangster aspires to join the notorious 'Axe Gang' while residents of a housing complex exhibit extraordinary powers in defending their turf.",
                              "https://upload.wikimedia.org/wikipedia/en/0/00/KungFuHustleHKposter.jpg",
                              "https://www.youtube.com/watch?v=-m3IB7N_PRk",
                              "4/22/2005",
                              "R",
                              "Action, Comedy, Crime",
                              "Stephen Chow")

raiders_of_the_lost_ark = media.Movie ("Raiders Of The Lost Ark",
                                       "Archaeologist and adventurer Indiana Jones is hired by the US government to find the Ark of the Covenant before the Nazis.",
                                       "https://upload.wikimedia.org/wikipedia/en/4/4b/Raiders.jpg",
                                       "https://www.youtube.com/watch?v=XkkzKHCx154",
                                       "6/12/1981",
                                       "PG-13",
                                       "Action, Adventure",
                                       "Harrison Ford, Karen Allen")
 
starship_troopers = media.Movie ("Starship Troopers",
                                 "Humans in a fascistic, militaristic future do battle with giant alien bugs in a fight for survival.",
                                 "https://upload.wikimedia.org/wikipedia/en/d/df/Starship_Troopers_-_movie_poster.jpg",
                                 "https://www.youtube.com/watch?v=Y07I_KER5fE",
                                 "11/7/1997",
                                 "R",
                                 "Action, Sci-Fi",
                                 "Casper Van Dien, Denise Richards, Neil Patrick Harris")
 
fight_club = media.Movie ("Fight Club",
                          "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more...",
                          "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                          "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                          "10/15/1999",
                          "R",
                          "Drama",
                          "Edward Norton, Brad Pitt")
 
#  Add to array to pass into the rendering procedure
movies = [toy_story, avatar, die_hard, terminator_2, zoolander, kung_fu_hustle, raiders_of_the_lost_ark, starship_troopers, fight_club]

#  Create and Render the page
fresh_tomatoes.open_movies_page(movies)




