from bs4 import BeautifulSoup, Doctype


class OutputSoup(BeautifulSoup):

    def __init__(self):
        super(OutputSoup, self).__init__(features='lxml')
        self.append(Doctype('html'))
        html = self.new_tag('html')
        self.append(html)
        head = self.new_tag('head')
        html.append(head)
        title = self.new_tag('title')
        title.string = 'TravellingKleinanzeigenProblem'
        head.append(title)
        self.body = self.new_tag('body')
        html.append(self.body)

    def add_all_items(self, items, postcode):
        if len(items) > 0:
            heading = self.new_tag('h2')
            heading.string = 'Ergebnisse für {}'.format(postcode)
            self.body.append(heading)
            table = self.new_tag('table')
            self.body.append(table)

            for item in items:
                tr = self.new_tag('tr')
                td_image = self.new_tag('td')
                image = self.new_tag('img', src=item['image'])
                td_image.append(image)
                td_title = self.new_tag('td')
                td_title.string = item['title']
                td_price = self.new_tag('td')
                td_price.string = item['price']
                link = self.new_tag('a', href=item['url'])
                link.string = 'Link'
                td_url = self.new_tag('td')
                td_url.append(link)
                tr.append(td_image)
                tr.append(td_title)
                tr.append(td_price)
                tr.append(td_url)
                table.append(tr)
