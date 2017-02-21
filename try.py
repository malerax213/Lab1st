#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple web client, using URLLIB2
Created on 10/14/2014
@author: carlesm
'''

import urllib2
import bs4


class Client(object):

    """Web Client, for www.udl.Created
    Downloads www.udl.cat main page to parse
    for agenda items"""

    def __init__(self):
        super(Client, self).__init__()

    def get_web_page(self, url):
        """
        Retrieves an HTML URL returns, HTML
        """
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def parse_web_page(self, html):
        """
        Parses an html page searching for the agenda
        """
        soup = bs4.BeautifulSoup(html,"html.parser")
        novetats = soup.find_all("div", "novetat")
        novetats_llista = []
        for novetat in novetats:
            datahtml = novetat.find("span", "data")
            data = datahtml.text
            item = novetat.find("a")
            text = item.text
            url = item["href"]
            # print data, ",", text, ",", url
            novetat_tupla = (data, text, url)
            novetats_llista.append(novetat_tupla)
        return novetats_llista

    def print_data(self, data):
        """
        Prints data retrieved
        """
        for datum in data:
            print ",".join(datum)

    def run(self):
        """
        Retrieves list of announces from www.udl.cat and print
        it
        """
        html = self.get_web_page("http://www.udl.cat/")
        novetats = self.parse_web_page(html)
        self.print_data(novetats)


if __name__ == "__main__":
    client = Client()
    client.run()
