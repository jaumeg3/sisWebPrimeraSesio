#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Client Web per www.udl.cat

@author: Jaume Giralt Barbé - jaume.giralt.2012@gmail.com
'''
import urllib2
from bs4 import BeautifulSoup


class Client(object):
    def get_web(self, page):
        '''baixar-se la Web'''
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    def search_text(self, html):
        '''Buscar el text'''
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find_all("div","featured-links-item")
        resultats = []
        for element in elements:
            data = element.find("time")["datetime"]
            title = element.find("span", "flink-title")
            if title:
                title = title.text
            else:
                title = "Sense Titol"
            resultats.append((data, title))
        return resultats


    def main(self):
        web = self.get_web('http://www.udl.cat/')
        resultat = self.search_text(web)
        # imprimir resultats
        print resultat


if __name__ == '__main__':
    client = Client()
    client.main()
