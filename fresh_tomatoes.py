#  07/15/15     Program created
#
#  Description:  Create an HTML page listing my favourite movies.  Users
#                can click on the poster for more details or watch the
#                movie trailer by pressing the 'Watch Trailer' button
#                (Code based on original file provided by Udacity)
#
#

import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }

        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-poster {
            margin-bottom: 20px;
            padding-top: 20px;
        }
		
        .movie-poster:hover {
            background-color: #D6D6D6;
            cursor: pointer;
        }

        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

        #movie-info .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 400px;
        }
        
        .modal-title {
            font-weight: bold;
        }

    </style>
    <script type="text/javascript" charset="utf-8">
	
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
				
	// Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.watch_trailer', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });

	// Show movie information in a modal window when poster is clicked
        $(document).on('click', '.movie-tile', function (event) {

            var movieTitle = $(this).attr('data-movie-title')
            var storyLine = $(this).attr('data-storyline')
            var actors = $(this).attr('data-actors')
            var genre = $(this).attr('data-genre')
            var releaseDate = $(this).attr('data-release-date')
            var rating = $(this).attr('data-rating')

            $('.modal-title').text(movieTitle);
            $('#storyLine').html(storyLine);
            $('#actors').html(actors);
            $('#genre').html(genre);
            $('#releaseDate').html(releaseDate);
            $('#rating').html(rating);

        });
        
	// Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-poster').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>

    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Movie Details Modal --> 
    <div class="modal fade" id="movie-info" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                    <h3 class="modal-title" id="myModalLabel">Movie Title</h3>
                </div>

                <div class="modal-body">
                    <form class="form-horizontal" role="form">
                        <div class="form-group">
                            <h4 class="col-md-3 col-sm-3 col-xs-3 text-right">Story Line:</h4>
                            <h5 class="col-md-9 col-sm-9 col-xs-15" id="storyLine">StoryLine</h5>
                        </div>
                        <div class="form-group">
                            <h4 class="col-md-3 col-sm-3 col-xs-3 text-right" for="actorsLabel">Actors:</h4>
                            <h5 class="col-md-9 col-sm-9 col-xs-15" for="actors" id="actors">Actors</h5>
                        </div>
                        <div class="form-group">
                            <h4 class="col-md-3 col-sm-3 col-xs-3 text-right" for="genreLabel">Genre:</h4>
                            <h5 class="col-md-9 col-sm-9 col-xs-15" for="genre" id="genre">Genre</h5>
                        </div>
                        <div class="form-group">
                            <h4 class="col-md-3 col-sm-3 col-xs-3 text-right" for="releaseDateLabel">Release Date:</h4>
                            <h5 class="col-md-9 col-sm-9 col-xs-15" for="releaseDate" id="releaseDate">Release Date</h5>
                        </div>
                        <div class="form-group">
                            <h4 class="col-md-3 col-sm-3 col-xs-3 text-right" for="ratingLabel">Rating:</h4>
                            <h5 class="col-md-9 col-sm-9 col-xs-15" for="rating" id="rating">Rating</h5>
                        </div>
                    </form>
                </div>

                <div class="modal-footer">
                   <button type="button" class="btn btn-primary" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
	
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Dave's Favourite Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
	
	
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-poster text-center"> 
	<div class="movie-tile text-center" data-toggle="modal" data-target="#movie-info" data-movie-title="{movie_title}" data-storyline="{storyline}" data-actors="{actors}" data-genre="{genre}" data-rating="{rating}" data-release-date="{release_date}">
		<img src="{poster_image_url}" width="220" height="342"></img>
		<h3>{movie_title}</h3>
    </div>
	<div class="watch_trailer text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" id="watch_trailer">
        <button type="button" class="btn btn-info">Watch Trailer</button>
    </div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            storyline=movie.storyline,
            actors=movie.actors,
            genre=movie.genre,
            release_date=movie.release_date,
            rating=movie.rating
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
