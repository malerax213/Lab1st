#!usr/bin/env_python
#Per utilitzar el djangostack: ./use_djangostack
'''
Client web per www.udl.cat

@author: alexandru_martinas33@hotmail.com
'''
import urllib2

class Client(object):

    def get_web(self, page):
        '''Baixar-se la web'''
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    def run(self):
        web = self.get_web('http://www.udl.cat/')
        # Buscar el text
        # Imprimir resultats
        pass

if __name__ == '__main__':
    c = Client()
    c.run()
