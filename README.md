octodex.py
============

A Python wrapper for the Octodex API.

##Use
Use this wrapper like any other Python class:

```python
# import the Octodex class from octodex.py
from octodex import Octodex

# initialize the class and store it in octodex
octodex = Octodex()

# fetch all octocats and print the returned dictionary
print octodex.completeOctodex()
```

For complete annotation, see [the actual class file (octodex.py)](octodex.py) as well as the [demo implementation](demo.py).

##Class Methods
Assuming `octodex = Octodex()`.  Check the [response example](#example-response) below, to see what these functions wil serve you.

###Complete Octodex
**`octodex.completeOctodex()`** 

Returns an array containing every octocat from [the Octodex](https://octodex.github.com).

###Random Octocat
**`octodex.randomOctocat()`** 

Returns a dictionary containing a random octocat from [the Octodex](https://octodex.github.com).

###Octocat by Number
**`octodex.numberedOctocat(1)`**

Where `number` is a number between 1 and the number of the last Octocat (as of 1/13/14 it is 113), and returns that numbered Octocat from [the Octodex](https://octodex.github.com).  

The API checks if the number exists in the Octodex, so you don't have to check if it does.

##Example Response
```python
{
    u'authorAvatar': u'https: //img.skitch.com/20110427-p3wtwcbu957cf9mm93s4sjqqci.png',
    u'name': u'Original',
    u'author': u'',
    u'image': u'http: //octodex.github.com/images/original.png',
    u'number': u'1',
    u'authorURL': u'http: //www.idokungfoo.com',
    u'page': u'http: //octodex.github.com/original'
}
```

###Keys
- `name` - the name of the octocat
- `page` - the webpage of the octocat
- `image` - the raw image URL of the octocat
- `author` - the creator of the octocat
- `number` - the number of the octocat in the series
- `authorURL` - the URL of the author (GitHub/Website)
- `authorAvatar` - the avatar of the author

##To Do
- Check for errors given by the API and handle them

##Use of Octocats
Check out the GitHub Octodex frequently asked questions (http://octodex.github.com/faq), for specific use.  GitHub owns all of the Octocats, this Python class just uses an API that grabs all of their data.