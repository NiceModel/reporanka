from utilities import check_year

class App:
    def __init__(self, book_service, io):
        self.book_service = book_service
        self.io = io

    def run(self):
        print("\nLUKUVINKKIKIRJASTO")

        while True:
            vastaus = self.io.read("\nValitse toiminto"
              "\n (1) lisää"
              "\n (2) listaa"
                "\n (3) hae"
                #   "\n (4) muokkaa"
                #   "\n (5) poista"
              "\n (0) lopeta"
              "\n"
              )
            if not vastaus:
                break

            if vastaus == "1":
                print( "Lisätään lukuvinkki...")
                print("")
                (author, title, published) = self._read_credentials()
                self.book_service.create_book(author, title, published)
                self.io.write("Uusi lukuvinkki lisätty.")

            elif vastaus == "2":
                print("Listataan lukuvinkit...")
                books = self.book_service.find_all_books()
                if books:
                    for book in books:
                        print(book)
                else:
                    print("Sovellukseen ei ole tallennettu vinkkejä ):")
                    
            # elif vastaus.endswith("3"):
            #     print("Haetaan lukuvinkkiä...")
            # elif vastaus.endswith("4"):
            #     print("Muokataan lukuvinkkiä...")
            # elif vastaus.endswith("5"):
            #     print("Poistetaan lukuvinkki...")
            elif vastaus ==("0"):
                print("Heido!")
                break


    def _read_credentials(self):
        author = self.io.read("Kirjailija: ")
        title = self.io.read("Nimi: ")

        check = True
        while check:
            published = self.io.read("Julkaisuvuosi: ")
            if not check_year(published):
                print("Julkaisuvuosi ei ole kelvollinen!")
            else:
                check = False

        return (author, title, published)

