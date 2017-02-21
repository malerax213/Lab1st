#!usr/bin/env_python
#Per utilitzar el djangostack: ./use_djangostack
'''
Client web per www.udl.cat

@author: alexandru_martinas33@hotmail.com
'''

class Client(object):

    def get_web(self, page):
        '''Baixar-se la web'''
        f = utilib2.urlopen(page)

    def run(self):
        web = self.get_web('http:/7www.udl.cat/')
        # Buscar el text
        # Imprimir resultats
        pass

if __name__ == '__main__':
    c = Client()
    c.run()
