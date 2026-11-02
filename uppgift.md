# Uppgift 2

## Bakgrund

Hackarna har avslöjat att de inte bara lyckats komma åt
företagets hemsida, de har dessutom tagit sig in och stulit
datorn med alla kontouppgifter.

Du kan inte hitta några spår av att något brytit sig in med
våld, så du misstänker att det är någon med ett passerkort
som tagit datorn. Alla som går in eller lämnar datorhallen
loggas i filen `access.log` med följande format:

    DAG TID [in | out] ID

- DAG är dag i månaden (en ny fil skapas varje månad).
- TID är hel timme, från 0 till 23.
- "in" eller "out" visar om personen kom eller gick.
- ID är en sträng som identifierar personen.

Några exempel:

    1 8 in id01
    1 9 in id02
    1 16 out id01
    1 18 out id02
    2 8 in id01
    2 10 in id03
    2 11 out id01
    2 14 in id01
    2 16 out id01
    2 16 out id03

Du är säker på att stölden skedde någon gång mellan 13 och 18
den 14 augusti.

## Uppgift

Ditt jobb är att läsa access-loggen och skapa en lista
med alla de ID:n som lämnade byggnaden mellan kl 13
och kl 18 den 14e.

Någon av dessa måste vara den skyldige.

Skapa en funktion `solution(path)` som läser loggfilen på sökvägen
`path` (så att samma funktion kan läsa vilken loggfil som helst). Du kan anta
att alla rader följer formatet som beskrivs ovan. Hitta alla rader som visar att
någon lämnade datorhallen den 14e mellan 13 och 18, och returnera dessa ID:n
som en lista.

Inkludera alla som gick ut från och med 13:00 (dvs. rader
med siffran 13) till och med de som gick ut 18:59 (dvs. rader
med siffran 18).

Krav på lösningen:

- Funktionen ska ta filens sökväg som parameter och använda den. En lösning som
  har filnamnet hårdkodad i koden godkänns inte.
- Funktionen ska använda en `with`-sats. Fundera på varför.
- Du ska skriva en egen docstring till funktionen som beskriver vad den läser,
  vad den returnerar och vilka antaganden den gör. Docstringen granskas.
- Du ska skriva minst tre egna tester som är relevanta för problemet, längst ner
  i `solution.py`. Tänk på vad som kan gå fel: vilka rader
  ska med och vilka ska inte?
- De färdiga testerna i `solution.py` är medvetet kräsna. Läs
  felmeddelandena noga.

Inlämningen ska bestå både av listan av ID:n och programmet som
löser uppgiften!

Skriv listan av ID:n i en kort `README.md` i den här mappen, tillsammans med
hur man kör programmet och antaganden du gjort. Se `../instruktioner.md`.

## Länkar och tips

Kör testerna med kommandot

    uv run pytest solution.py

- I testerna i `solution.py` skapas en liten loggfil med `tmp_path`. Det är en
  pytest-fixtur: lägg bara `tmp_path` som parameter på testfunktionen och använd
  `tmp_path / "test.log"` som filnamn. Se `test_solution`.

  Dina egna tester ska vara egna funktioner vars namn börjar med `test_`.
  `pytest` kör alla sådana funktioner i filen.

- Funktionen `int(s)` kan användas för att omvandla en
  sträng som innehåller ett tal till ett tal i Python.

- https://docs.python.org/3/library/functions.html#open

  Funktionen `open()` används för att öppna en fil.

- https://docs.python.org/3/reference/compound_stmts.html#the-with-statement

  Satsen `with`.

- https://docs.python.org/3/library/io.html#io.IOBase.readlines

  Metoden `.readlines()` läser in alla rader i en fil.
