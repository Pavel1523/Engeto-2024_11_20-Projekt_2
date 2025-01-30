# projekt_2.py: druhý projekt do Engeto Online Python Akademie, verze 1
# Tic Tac Toe
# author: Ing. Pavel Mrkva
# email: pavel.mrkva@seznam.cz


def print_intro():
    """Vraci uvitaci textya pravidla hry."""
    print("Welcome to Tic Tac Toe")
    print("=" * 50)
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("=" * 50)
    print("Let's start the game")


def print_hraci_plocha(hraci_plocha):
    """Vraci prazdne a v prubehu hry od hracu vyplnovane hraci pole."""
    print("-" * 50)
    for rada in hraci_plocha:
        print("+---+---+---+")
        print(
            "| " + " | ".join(rada) + " |"
        )  # doplneni 'O' nebo 'X' do hracem vybraneho pole
    print("+---+---+---+")
    print("=" * 50)


def kontrola_viteze(hraci_plocha, hrac):
    """Kontroluje, zda zadaný hráč (player, tedy "X" nebo "O") vyhrál."""
    for rada in hraci_plocha:  # kontrola stejnych znaku v radcich
        if all(sloupec == hrac for sloupec in rada):
            return True  # pokud je vse stejne
    for sloupec in range(3):  # kontrola stejnych znaku ve sloupcich
        if all(hraci_plocha[rada][sloupec] == hrac for rada in range(3)):
            return True  # pokud je vse stejne
    if all(hraci_plocha[i][i] == hrac for i in range(3)) or all(
        hraci_plocha[i][2 - i] == hrac for i in range(3)
    ):  # kontrola stejnych znaku v diagonalach
        return True  # pokud je vse stejne
    return False  # pokud neni vitez


def vse_vyplneno(hraci_plocha):
    """Vraci info, ze je hraci plocha vyplnena = remiza."""
    return all(sloupec != " " for radek in hraci_plocha for sloupec in radek)


def tah_hrace(hrac, hraci_plocha):
    """Ziska tah hrace, pricemz kontroluje, jestli je zhracem zvolene pole volne."""
    while True:
        try:  # kontroluje cislo zadane hracem
            tah = (
                int(input(f"Player {hrac} | Please enter your move number: "))
                - 1
            )  # vyzve hrace k zadani cisla pole
            rada, sloupec = divmod(
                tah, 3
            )  # pomoci funkce divmod() priradi tahu hrace cislo pole
            if (
                tah < 0 or tah >= 9
            ):  # kontroluje cislo pole zvolene hracem - musi byt od 1 do 9
                print("Invalid input. Please choose a number between 1 and 9.")
            elif (
                hraci_plocha[rada][sloupec] != " "
            ):  # kontroluje, zda je pole volne
                print("That spot is already taken. Choose another one.")
            else:
                return rada, sloupec  # vraci koordinaty pole
        except (
            ValueError
        ):  # vraci cyklus na zacatek po zadani chybneho cisla pole
            print("Invalid input. Please enter a number.")


def tic_tac_toe():
    """Spousti hru"""
    print_intro()
    hraci_plocha = [
        [" "] * 3 for _ in range(3)
    ]  # zadani velikosti hraci plochy  3x3 ( = 3 rady / 3 sloupce)
    hraci = ["O", "X"]  # seznam hracu, hrac "O" hraje prvni
    hrac_na_rade = 0  # hrac "O" hraje prvni
    while True:  # cyklus jednotlivych kol
        print_hraci_plocha(hraci_plocha)
        hrac = hraci[hrac_na_rade % 2]  # hrac, ktery je prave 'na rade'
        rada, sloupec = tah_hrace(
            hrac, hraci_plocha
        )  # vraci cilso pole -> koordinaty
        hraci_plocha[rada][
            sloupec
        ] = hrac  # yapise znak hrace do zvoleneho pole
        if kontrola_viteze(hraci_plocha, hrac):
            print_hraci_plocha(hraci_plocha)
            print(f"Congratulations, the player {hrac} WON!")
            break
        if vse_vyplneno(hraci_plocha):
            print_hraci_plocha(hraci_plocha)
            print("It's a tie!")
            break
        hrac_na_rade += 1  # vraci, kdo bude v dalsim cyklu hrat


if __name__ == "__main__":
    tic_tac_toe()
