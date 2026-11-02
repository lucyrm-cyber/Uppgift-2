from pathlib import Path
import time

def solution(sokvag=None):

    # Validerar att en sokväg har skickats in i funktionen, om inte returneras None.
    
    if sokvag is None:
        print("Det finns ingen sökväg angiven")
        return None
    else:
        print(f"Kontrollerar sökvägen: {sokvag}")
        time.sleep(1)

    # Try/except/else-sats som testar för att bekräfta att filen finns.
    # Finns inte filen returneras ett felmeddelande och programmet avslutas.
    # Finns filen så fortsätter programmet

    try:
        with open(str(sokvag)) as f:
            print("Hittade en fil på den angivna platsen.")
            time.sleep(1)
    except FileNotFoundError:
        print("Det finns ingen sådan fil, vänligen kontrollera din sökväg och ditt filnamn.")
        return FileNotFoundError
    else:

    # När vi har en fil som finns så läser vi in den och läser igenom den rad för rad.
    # Vi fångar upp om filen inte följer den förutbestämda formateringen. 
    # Om filen följer formatet så delar vi upp varje rad i delar och letar efter rader som matchar parametrarna där datum är 14, 13 <= tid <= 18 och in/out är out 
    # Nya misstänkta IDn appendas till en lista av misstänkta, finns ID-numret redan inlagt hoppas det över för upprepade träffar.
    
        print(f"Letar efter misstänkta i filen {sokvag}")
        time.sleep(1)
        misstankta = []
        with open(sokvag, encoding="utf-8") as f:
            for rad in f:
                delar = rad.strip().split()
                if delar[4:]:
                    print("Den angivna filen verkar har för många fält, filen behöver innehålla endast fälten [datum] [timma] [in | out] [användar id], vänligen kontrollera din fil och försök igen.")
                    return IndexError
                else:
                    try:
                        (type(int(delar[0])) == int) and (type(int(delar[1])) == int) and (type(delar[2]) == str) and (type(delar[3]) == str)
                    except IndexError:
                        print("Den angivna filen verkar inte följa det krävda formatet av [datum] [timma] [in | out] [användar id], vänligen kontrollera din fil och försök igen.")
                        return IndexError
                    except ValueError:
                        print("Den angivna filen verkar inte innehålla data i det forväntade formatet [datum = siffra] [timma = siffra] [in | out = sträng] [användar id = sträng], vänligen kontrollera din fil och försök igen.")
                        return ValueError
                    else:
                        if (int(delar[0]) == 14) and (13 <= int(delar[1]) <= 18) and (str(delar[2]) == "out"):
                            if rad[10:15] in misstankta:
                                continue
                            else:
                                misstankta.append(delar[3])

        # Slutligen så sorteras listan av misstänkta för att underlätta granskning av en människa
        # Sökvägen dels upp så att vi får ut enbart filnamnet, detta används endast för att göra ett finare output för användaren.
        # Listan skrivs sedan ut till konsolen tillsammans med filnamnet. Listan returneras till kallaren.
        fil = str(sokvag).rsplit('/',1)[-1]
        sorterade_misstankta = sorted(misstankta)
        print(f" De misstänkta utpasseringarna i {fil} är följande: {sorterade_misstankta}")
        return sorterade_misstankta


def get_path():
    # Det här är en support-funktion som frågar användaren om vilken log-fil som ska granskas.
    # Den försöker vara så snäll och hjälpsam som möjligt för att möjliggöra att vem som helst ska kunna ta över scriptet och köra det.
    # Funktionen börjar med en ja/nej frågar för att ta reda på om den ska använda current working directory (cwd) eller en absolut sökväg som användaren skriver in.
    # Om man väljer ja är funktionen snäll och skriver ut alla filer i cwd ifall man inte är helt säker på filnamnet man väntas skriva in.
    # Om man väljer nej ombeds man skriva in den absoluta sökvägen inklusive filnamnet och filändelsen.
    # Om man skulle skriva varken ja eller nej så loopas man tillbaka till början av loopen för att förhindra att programmet faller sönder.
    # När man har försett programmet med antingen filnamn eller absolut sökväg så kallas solution-funktionen med sökvägen som argument.

    while True:
        print(f"Programmet körs ifrån {Path.cwd()}")
        fraga_path = input("Ligger din fil i samma mapp som programmet körs ifrån? Ja / Nej: ")
        if fraga_path.lower() == "ja":
            for item in Path.cwd().iterdir():
                if item.is_dir():
                    continue
                else:
                    print(f"Fil: {item.name}")
            complete_file_path = Path.cwd() / input("Vad heter filen du vill granska? Svara med namn på din fil inklusive filmformat, exempel fil.txt: ")
            break
        elif fraga_path.lower() == "nej":
            complete_file_path = input("I filken mapp ligger din fil? Skriv den absoluta sökvägen inklusive filnamnet med filändelsen.\n Exempel: /home/ciso/kod/pythonkurs/inlamning/uppgift-2/access.log: ")
            break
        else:
            print("Jag förstod inte det där svaret, vänligen försök igen")
    sokvag = Path(complete_file_path)
    solution(sokvag)

# Från getting-started.ipynb, ignoreras när filen körs genom pytest men kallar på solution-funktionen om filen körs manuellt.
# Den kallar på support-funktionen get_path som ber användaren om sökvägen till filen som ska granskas.
if __name__ == "__main__":
    get_path()


# Tester
def test_solution(tmp_path):
    ids = solution("access.log")
    assert len(ids) > 0, "No ID:s returned"
    assert all(type(id) == str for id in ids), "Not a string"
    assert all(len(id) > 4 for id in ids), "ID should contain at least 4 characters"
    assert all(id.isalnum() for id in ids), "ID should only contain letters a-z or numbers"

def test_solution_2(tmp_path):
    # Ett litet exempel med en egen testfil (tmp_path är en tillfällig mapp från pytest).
    fil = tmp_path / "exempel.log"
    fil.write_text("14 14 out id001\n14 14 in id002\n")
    assert solution(str(fil)) == ["id001"]

def test_solution_3(tmp_path):
    # En blandad logg.
    fil = tmp_path / "blandad.log"
    fil.write_text(
        "14 12 out id010\n"
        "14 13 out id011\n"
        "14 14 in id012\n"
        "14 15 out id013\n"
        "13 15 out id014\n"
        "14 17 out id013\n"
        "1 14 out id015\n"
        "14 18 out id012\n"
        "14 19 out id016\n"
    )
    assert sorted(solution(str(fil))) == ["id011", "id012", "id013"]

# Egna tester: skriv minst tre här (se test_solution för hur man skriver en testfil).

def test_solution_4():
    # Test 4 testar med en sökväg som inte finns och förväntar sig ett FileNotFoundError
    output = solution("asdf")
    assert output == FileNotFoundError

def test_solution_5(tmp_path):
    # Test 5 testar med en lista som består av flera poster som bara är mellanslag, alltså en trasig/felaktigt genererad log-fil.
    fil = tmp_path / "exempel.log"
    fil.write_text(
        "   \n"
        "    \n"
        )
    assert solution(fil) == IndexError

def test_solution_6(tmp_path):
    # Test 6 testar med en lista med för långa poster.
    fil = tmp_path / "exempel.log"
    fil.write_text(
        "a b c d e"
        )
    assert solution(fil) == IndexError

def test_solution_7(tmp_path):
    # Test 7 testar med en lista med poster i felaktigt format.
    fil=tmp_path / "exempel.log"
    fil.write_text(
        "True abc 123 123\n"
        "abc 123 abc 123\n"
        )
    assert solution(fil) == ValueError

def test_solution_8():
    # Testa att vi får tillbaka None om vi inte skulle skicka in en sökväg alls.
    assert solution() == None