'''

1. Beautiful Soup gives us a BeautifulSoup object, which represents
   the document as a nested data structure.

2. First, the document is converted to Unicode, and HTML entities are 
   converted to Unicode characters.
   For exampple: "acr&eacute; bleu!" will convert into "acré bleu!"

3. There are 2 types of parser 1st one is HTML parser & the 2nd one is XML parser.
        XML was designed to carry data - with focus on what data is
        HTML was designed to display data - with focus on how data looks
        XML tags are not predefined like HTML tags are

4. You can add, remove, and modify a tag’s attributes. 
   Again, this is done by treating the tag as a dictionary:

To install this package pip install bs4 or pip install beautifulsoup4
If you don’t have easy_install or pip installed, you can download the Beautiful Soup 4 source tarball
and install it with setup.py. python setup.py install
'''

'''
Points from trainner:
    dataframe
'''


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


from bs4 import BeautifulSoup
# # if you have html file then open file and pass it into BeautifulSoup constuctor
with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
# # if you don't have html file then pass directly html variable into it.
# soup = BeautifulSoup(html_doc, 'html.parser')

# b = soup.p
# # b.name = "MyNewTitle"   # we can change name of tag by using this method.
# print(b.attrs)    # Get all attribute like class, href, etc. in dict form

# print(soup.title)   # To get a whole title tag with text. 
                      # If html 2 tag with the same name then it'll take 1st one
# #Output: <title>The Dormouse's story</title>
'''========================================================================='''

# print(soup.title.name)      # To get name of tag
# # u'title'  
'''========================================================================='''

# print(soup.title.string)           # To get text of tag
# # u'The Dormouse's story'
'''========================================================================='''

# print(soup.title.parent.name)
# # u'head'
'''========================================================================='''

# print(soup.p)   # Get p tag with text
# # <p class="title"><b>The Dormouse's story</b></p>
'''========================================================================='''

# print(soup.p['class'])    # To get class of tag in list datatype
# # ['title']  # If class have space then it'll split from space & return list
#              # Ex: If you've <p class="title Titleone"> then Output will be: ['title','Titleone']
'''========================================================================='''

# print(soup.find("p",id='story id')['id'])    # To get id of tag
# # ['story id']  # If id have space then it'll NOT split from space
#                 # Ex: If you've <p id="title Titleone"> then Output will be: title Titleone
'''========================================================================='''

# print(soup.a)         # To get 1st a tag
# # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
'''========================================================================='''

# print(soup.find_all('a'))	# Find all the matched tags(find by tag)
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
'''========================================================================='''

# print(soup.find(id="link3")		# Find using id
# # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
'''========================================================================='''

# # To get links which are in a tag.
for link in soup.find_all('a', multi_valued_attributes=None):
    if link.has_attr( "class" ):
        if link['class'] == ['sister']:
            print(link.get('href'))
'''========================================================================='''

# print(soup.get_text())      # Extracting all the text from a page
'''========================================================================='''

# # If you want to change rel attribute name 
# # then you can write rel_soup.a['rel'] = ['index', 'contents']
# el_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
# rel_soup.a['rel']
# # ['index']
# rel_soup.a['rel'] = ['index', 'contents']
# print(rel_soup.p)
# # <p>Back to the <a rel="index contents">homepage</a></p>
'''========================================================================='''

# #  If you want class without spliting with space 
# #  then you've to write "multi_valued_attributes=None".
# no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html', multi_valued_attributes=None)
# print(no_list_soup.p['class'])
'''========================================================================='''
# # You can use `get_attribute_list to get a value that’s always a list, 
# # whether or not it’s a multi-valued atribute:
# print(soup.find("p",id='story id').get_attribute_list('id'))