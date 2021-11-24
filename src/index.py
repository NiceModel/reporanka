def main():
    print("LUKUVINKKIKIRJASTO")
    while True:
        print("\nValitse toiminto"
              "\n (1) lisää"
              "\n (2) hae"
              "\n (3) muokkaa"
              "\n (4) poista"
              "\n (0) lopeta"
              )

        vastaus = input()

        if vastaus.endswith("1"):
            print( "Lisätään lukuvinkki...")
        elif vastaus.endswith("2"):
            print("Haetaan lukuvinkkiä...")
        elif vastaus.endswith("3"):
            print("Muokataan lukuvinkkiä...")
        elif vastaus.endswith("4"):
            print("Poistetaan lukuvinkki...")
        elif vastaus.endswith("0"):
            print("Heido!")
            break
        else:
            continue


if __name__ == "__main__":
    main()
