from utilities import check_year

class App:
    def __init__(self, book_service, io):
        self.book_service = book_service
        self.io = io
        self.running = True
        self.ohjeet = (
            "\nValitse toiminto"
            "\n (1) lisää"
            "\n (2) listaa"
            "\n (3) hae"
            "\n (0) lopeta\n")

    def run(self):
        print("\nLUKUVINKKIKIRJASTO")

        while self.running:
            vastaus = self.io.read(self.ohjeet)
            if not vastaus:
                self.running = False
            elif vastaus == "1":
                self._add_book()
            elif vastaus == "2":
                self._list_books()
            elif vastaus == "0":
                print("Heido!")
                self.running = False
            else:
                print("Komentoa ei löytynyt, yritä uudelleen.")

    def _add_book(self):
        print("Lisätään lukuvinkki...")
        print("")

        author = self.io.read("Kirjailija: ")
        while not author:
            print("Kirjailijan nimi on lisättävä!")
            author = self.io.read("Kirjailija: ")

        title = self.io.read("Nimi: ")
        while not title:
            print("Kirjan nimi on lisättävä!")
            title = self.io.read("Nimi: ")

        check = True
        while check:
            published = self.io.read("Julkaisuvuosi: ")
            if not check_year(published):
                print("Julkaisuvuosi ei ole kelvollinen!")
            else:
                check = False

        self.book_service.create_book(author, title, published)
        self.io.write("Uusi lukuvinkki lisätty.")

    def _list_books(self):
        print("Listataan lukuvinkit...")
        books = self.book_service.find_all_books()
        if books:
            for book in books:
                print(book)
        else:
            print("Sovellukseen ei ole tallennettu vinkkejä ):")

    def _choose_feature(self):
        feature = self.io.read("\nValitse toiminto"
              "\n (1) lisää"
              "\n (2) listaa"
                "\n (3) hae"
                #   "\n (4) muokkaa"
                #   "\n (5) poista"
              "\n (0) lopeta"
              "\n"
              )
        