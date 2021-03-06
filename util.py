import urllib
from urlparse import urlsplit, urlunsplit


def print_usage():
    print "Usage: python mapper.py -l <url>"
    print "For help: python mapper -h"
    exit()

def url_fix(s, charset='utf-8'):
    """Sometimes you get an URL by a user that just isn't a real
    URL because it contains unsafe characters like ' ' and so on.  This
    function can fix some of the problems in a similar way browsers
    handle data entered by the user:

    :param charset: The target charset for the URL if the url was
                    given as unicode string.
    """
    if isinstance(s, unicode):
        s = s.encode(charset, 'ignore')
    scheme, netloc, path, qs, anchor = urlsplit(s)
    # if not scheme:
    #     scheme = "http"
    path = urllib.quote(path, '/%')
    qs = urllib.quote_plus(qs, ':&=')
    return urlunsplit((scheme, netloc, path, qs, anchor))