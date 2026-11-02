Antaganden som har gjorts: 

- Vi antar att i inställningarna för Python-tillägget i Visual Studio Code under stycket Python > Terminal har vi bockat i Execute in File Dir. 
- Vi antar att vi vet vad vilen vi vill titta på heter. 
- Vi antar att log-filen ligger i samma mapp som python-scriptet befinner sig i eller att vi vet exakt var log-filen ligger.

Hur man kör programmet:

Förutsättningarna är att vi antingen vet exakt var log-filen finns eller att den befinner sig i samma folder som scriptet körs i. När man sedan kör skriptet kommer du tillfrågas om log-filen ligger i mappen du befinner dig i, om ja listar den alla tillgängl.iga filer i samma mapp och ber dig fylla i vilklen av filerna det gäller. Om man svarar nej blir man ombedd att skriva in den absoluta sökvägen till filen istället. 
Programmet kommer sen att validera att det är en korrekt länk som angivits och kommer sedan att granska loggen för att hitta de misstänkta utpasseringarna och skriva dessa till terminalen.


Nedan följer output från solution.py:

 De misstänkta är följande: ['id001', 'id007', 'id009', 'id015']

