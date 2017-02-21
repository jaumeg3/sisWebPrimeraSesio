#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Client Web per www.udl.cat

@author: Jaume Giralt Barbé - jaume.giralt.2012@gmail.com
'''
import urllib2


class Client(object):
    def get_web(self, page):
        '''baixar-se la Web'''
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    def main(self):
        web = self.get_web('http://www.udl.cat/')
        # buscar el text
        # imprimir resultats
        print web


if __name__ == '__main__':
    client = Client()
    client.main()
