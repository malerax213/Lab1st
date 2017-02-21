#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple web client, using URLLIB2
Created on 21/02/2017
@author: Aelxandru Martinas
'''

import urllib2
from bs4 import BeautifulSoup


class Client(object):

    """Web Client, for www.udl.Created
    Downloads www.udl.cat main page to parse
    for agenda items"""

    def __init__(self):
        super(Client, self).__init__()

    def get_web(self, url):
        """
        Retrieves an HTML URL returns, HTML
        """
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def search_test(self, html):
        """
        Parses an html page searching for the agenda
        """
        soup = BeautifulSoup(html,'html.parser')
        elements = soup.find_all("div", "featured-")
        resultats = []
        for element in elements:
            data = element.find("time")["datatime"].text
            title = element.find("spam","flink-title").text
            resultats.append((data,title))
        return resultats

    def run(self):
        """
        Retrieves list of announces from www.udl.cat and print
        it
        """
        html = self.get_web("http://www.udl.cat/")
        resultat = self.search_test(html)
        #print resultat


if __name__ == "__main__":
    client = Client()
    client.run()
