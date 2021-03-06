from karoseria_simple_factory_refleksja import KaroseriaSimpleFactory


class FabrykaKaroserii:
    __singleton_factory = None

    def __init__(self, fabryka: KaroseriaSimpleFactory):
        self.__singleton_factory = fabryka

    def karoseria_simple_factory(self, nazwa: str)->KaroseriaSimpleFactory:
        element = self.__singleton_factory.element_karoserii(nazwa)
        element.dodaj_element()
        element.testuj()
        return element


def main():
    """ test dzialania prostej fabryki z tworzeniem klas obiektow przez reflekcje """
    prosta_fabryka_karoserii = KaroseriaSimpleFactory()
    fabryka = FabrykaKaroserii(prosta_fabryka_karoserii)
    wytworzony_element = fabryka.karoseria_simple_factory('Blotnik_lewy')
    print(wytworzony_element)
    wytworzony_element = fabryka.karoseria_simple_factory('Blotnik_prawy')
    print(wytworzony_element)
    wytworzony_element = fabryka.karoseria_simple_factory('Maska')
    print(wytworzony_element)
    wytworzony_element = fabryka.karoseria_simple_factory('Bagaznik')
    print(wytworzony_element)
    wytworzony_element = fabryka.karoseria_simple_factory('Drzwi_lewe')
    print(wytworzony_element)
    wytworzony_element = fabryka.karoseria_simple_factory('Drzwi_prawe')
    print(wytworzony_element)
    wytworzony_element = fabryka.karoseria_simple_factory('Dach')
    print(wytworzony_element)
    wytworzony_element = fabryka.karoseria_simple_factory('Lakier')
    print(wytworzony_element)
    print(wytworzony_element.get_elementy())


if __name__ == '__main__':
    main()
