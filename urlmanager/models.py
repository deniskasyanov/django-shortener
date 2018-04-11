from django.db import models

class Url(models.Model):
    # There seems to be no performance difference between TextField
    # and CharField using PostgreSQL according to
    # https://www.postgresql.org/docs/9.2/static/datatype-character.html
    # Assuming urls can be as long as 2000 symbols I've chosen TextField
    # Majority of urls will be way shorter than 2000, so TextField gives
    # advantage of smaller storage size in comparison to blank-padded types
    # such as CharField (varchar(n) in PostgreSQL)
    full_url = models.TextField()

    # For app portability I won't keep short urls in database.
    # Instead their paths will be kept.
    # Using 7 alphanumeric characters (A-Z, a-z, 0-9) like bitly does,
    # gives 62**5 = 3,521,614,606,208 possible combinations which would
    # make it pretty hard to guess. 
    # Rate limiting of access using short url can further increase privacy.
    short_url_path = models.CharField(max_length=7)

    def get_short_url(self):
        return f'/{self.short_url_path}/'

    def get_full_url(self):
        return self.full_url
