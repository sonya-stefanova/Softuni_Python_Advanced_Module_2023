import pyshorteners

link_address = input("Please, enter the link you want to shorten: ")
link_shortener_object = pyshorteners.Shortener()

# get the shortened link
result = link_shortener_object.tinyurl.short(link_address)

print(result)