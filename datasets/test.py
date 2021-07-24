from html.parser import HTMLParser

class test(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        return super().handle_starttag(tag, attrs)
    def handle_data(self, data):

        print(data)
        return super().handle_data(data)


parse=test()
parse.feed('<p>abc<br>de<br>zx</p>')