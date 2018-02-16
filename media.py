import webbrowser

class Movie():
    """docstring for Movie."""
    def __init__(self, title, story_line, thumbnail_url, trailer_url):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = thumbnail_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open( self.trailer_url )
