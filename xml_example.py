"""creating xml using python"""
from lxml import etree
from lxml.builder import E

def create_xml():
    print "creating xml .."

    first_name = E.first_name("First_Name")
    last_name = E.last_name("Last Name")

    author = E.author(first_name,last_name)

    title = E.title("Title")
    year = E.year("2015")
    price = E.price("32.50")

    book = E.book(title, author, year, price)
    print "XML : ",etree.tostring(book)
    print "_" * 50
    print "formatted XML : ",etree.tostring(book, pretty_print=True)

create_xml()
