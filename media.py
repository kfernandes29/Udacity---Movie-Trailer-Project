import webbrowser

class Movie():
    """
        Method: __init__()
        Args:
            title (str): Movie Titles
            story_line (str): Storyline
            thumbnail_url (str): Thumbnail URL
            trailer_url (str): Trailer URL
    """
    def __init__(self, title, story_line, thumbnail_url, trailer_url):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = thumbnail_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        """
            Method: show_trailer()
            Args:
                none
        """
        webbrowser.open( self.trailer_url )
