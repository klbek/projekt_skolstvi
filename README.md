# Modelace skutečné a využívané kapacity školkých zařízení v ČR

Tento repozitář obsahuje skripty, výstupní soubory a vizualizace pro zjištění, zda jsou kapacity školkých zařízení ČR - konkrétně Mateřské školy - dostupné pro její obyvatele. Výstupní data mohou sloužit pouze pro modelaci dostupnosti kapacit pro školní rok 2023/2024[^1], pouze pro Mateřské školy a s jemným zkreslením[^2].

[^1]: Pro přesnější výsledky bychom potřebovali datovou sadu kapacit školských zařízení z roku 2023 (nejlépe ze srpna). Data však máme jen aktuální k 8.8.2024. Není věcí častou a jednoduchou navyšovat/snižovat kapacity školských zařízení (i zakládat nová zařízení), proto pracujeme alespoň s těmito údaji, které nám mohou výsledky spíše jen mírně zkreslit.   

[^2]: Jemným zkreslení je myšleno použití aktuálnějších dat kapacit šk. kapacit (viz. bod výše), rozpočítané porodnosti ve 3.kvartálech pro zjištění, kolik dětí je cca narozených do 31.srpna (pro výpočet nároku na MŠ za 3 roky), v pár případech nedostatečně vyplněné adresy použit Copilot od Microsoftu k přiřazení kraje (náhodně testováno, zda se jedná o správný výsledek), v případě, že školské zařízení působí ve vícero krajích (kapacity nejsou v datech členěny), tak dle vlastního uvážení jsou kapacity přiřazeny do konktrétních krajů, aby se uměle v datech nenavyšovaly kapacity. 

## Výsledky
Jelikož jsou dětské skupiny soukromá zařízení (byť z části dotovaná), jejich zájem a nutností je mít plné kapacity, aby zaplatily svůj provoz. Proto počítáme s tím, že kapacity DS = reálná docházka do DS. Zároveň nelze členit jejich docházku podle věku (jako je to u MŠ), kapacity jsou počítány na dítě. Reálně může DS navštěvovat o mnoho více dětí z různých věkových skupin v režimech 1-5x týden.

### Reálná docházka do MŠ
![Reálná docházka MŠ](output_files/images/realna_dochazka_MS.jpg)
Grafy ukazují, kolik 3-letých dětí s nárokem docházet do MŠ do ní reálně nedochází. Horní graf ukazuje věkové rozložení docházky včetně dětí mladších 3-let. Spodní graf ukazuje kolik 3-letých dětí (vypočítaných dle porodnosti) má nárok chodit do MŠ a kolik jich skutečně MŠ navštěvuje, respektive nenavštěvuje (prostor mezi sloupcem a linií). 

### Kapacity suplované dětskými skupinami
![Reálná docházka MŠ](output_files/images/suplovane_kapacity_MS.jpg)
Graf ukazuje, jak velkou docházku MŠ suplují dětské skupinky (růžová plocha). Zároveň můžeme vidět velký rozdíl mezi oficiálními kapacitami MŠ a jejich reálnou docházkou (plocha mezi modrou a fialovou linií), respektive i reálnou docházkou MŠ po připočítání docházky do DS (plocha mezi růžovou čerchovanou a fialovou plnou liníí).  

### Návrhy na zlepšení 
S daty lze dále pracovat a zjistit, kolik i 4-5letých dětí má nárok chodit do MŠ a nechodí do ní (důvody ohou být různé).

### Shrnutí
Cílem projektu bylo zjistit a ukázat, jak jsou na tom kapacity školek a kolik míst chybí. Dle reálné kapacity bychom mohli usuzovat, že s místy není problém, avšak počet neumístěných 3-letých dětí a počet kapacit DS tomu neodpovídá.  

Rozdíl mezi celkovou kapacitou MŠ a reálnou docházkou do MŠ lze vysvětlit 
- jako rezervní místa pro případ nově přistěhovaných občanů do obce
- vylidňování některých lokací - následná velká neobsazenost a naopak přetlak v jiných oblastech

Docházku do DS lze brát jako touhu po individuálním přístupu k dítěti, ale i jako nutnost v případě potřeby návratu do práce. Tak jako tak se za docházku platí nemalé peníze (byť je z části dotovaná) a pro spoustu lidí je tak nedostupná. 

## O datech
Během práce s daty se bohužel hlavní zdrojová (open) data ukázala jako nedostatečná pro dlouhodobé (i retrospektivní) modelování a to z důvodu jejich časové aktuálnosti (datová sada je aktualizována 3x do týdne). 

O historická, archivovaná data bylo v září 2024 zažádáno. Pravděpodobně však vzhledem k rozsáhlosti databáze (využívané i pro jiné účely, než jen monitorování školských zařízení) a požadovaných potřebných informací nebudou data dodána. 

V případě dodaní dat by se musely skripty zásadně předělat, místo formátu .xml mohou dodat data pouze ve formátu .xlsx nebo .csv.  Zarchivovaná data nelze poskytnout ve formátu .xml, pro které jsou sckripty vytvořeny. 

Data byla dávána do kontextů pouze na úrovni krajů, protože podrobnější data u porodnosti, reálné návštěvnosti MŠ, chybí. 

### Kapacity školských zařízení
Hlavní zdrojová data jsou dostupná vždy s aktuálními informacemi v [Národním katalogu otevřených dat](https://data.gov.cz/datov%C3%A1-sada?iri=https%3A%2F%2Fdata.gov.cz%2Fzdroj%2Fdatov%C3%A9-sady%2F00022985%2F63989c80e16fc31c77e23ab529c76b52#str%C3%A1nka-nenalezena) ve formátu .xml.

Při zpracování dat bylo vytvořeno vlastní [schéma](schemas_diagrams/diagram_dat_skol.jpeg) rozpadu/větvení dat, které bylo postupně upravováno.
Následně byl vytvořen [ER diagram](schemas_diagrams/ERD_tabulky.jpeg), který byl podklad nejen pro samotnou práci s daty, ale pro základní zpracování raw dat do samostaných tabulek. 

ER diagram je vytvořený především pro zpracování dat Mateřských škol, lze na něj ovšem snadno navázat a rozšířit jej i na základní, střední školy, konzervatoře aj. 

ER diagram obsahuje i schéma vysvětlující mírně nestandartní manipulaci s daty pro zjištění lokace (kraje) každého zařízení. Vzhledem k různorodosti a neúplnosti dat byly zvoleny pomalejší vlastní funkce na místo funkcí z knihovny Pandas(a následného složitějšího pročišťování dat). V závěru pak bylo využito AI Copilot od Microsoftu, který pomohl přiřadit kraj k nestandardnímu a velmi různorodému zápisu adres (např. parcela dle KÚ) nebo k adrese, jejíž PSČ náleželo do dvou krajů. 

#### Kapacity školských zařízení MŠ, DS, vVP - [predskolniVP.csv](output_files/predskolniVP.csv)
V rámci třídění relevantních dat byly pro Mateřské školy vybrány zařízení ze [seznamu](zarizeni_dokumentace.txt) týkajících se pouze mateřských škol + přípravný stupěň zákl. školy speciální, který zákonně spadá pod MŠ. 

Z důvodu nedostatku kapacit jsou v dnešní době hojně využívany i dětské skupiny, proto jsme ze stránek [MPSV](https://evidence.mpsv.cz/eEDS/index.php?list) scrapovali jejich aktuální (realtime) kapacitu. Toto scrapování lze nahradit zpracování open data JSON souboru (a dopočítat si kapacity v průběhu času), jak se později zjistilo. Pro naše demonstrativní účely to však nepotřebujeme. Na závěr nutno dodat, že tato zařízení nespadají pod MŠMT, ale v datech hrají zásadní roli. 

Tabulka mateřských škol je pak spojena s tabulkou kapacit dětských skupin (v tabulce zařízení rozlišeno)

### Reálný počet žáků v Mš - [MS_all_dochazka.csv](output_files/MS_all_dochazka.csv)
Zdrojová data byla získána na stránkách [ČSÚ](https://csu.gov.cz/) ve formátu .xlsx pro jednotlivé roky. 

Nahrána a dále zpracována byla jen data obsahující informace, jako je počet dětí docházejících do MŠ celkem a podle věku vůči krajům, k datům byl přiřazen patříčný školní rok. Následně byla data spojena do jedné tabulky.

Pro zajímavost byla nahrána i data týkající se docházky cizinců (u dvojího občanství se bere přednostně to České), data bohužel nebyla rozčlěněna dle věku, použe dle šk. roku a kraje. Ve vizualizacích s tímto údajem prozatím nepočítáme. Tento údaj je však již zahrnut v reálné docházce. 

### Porodnost 2018-2023 - [porodnost_podr.csv](output_files/porodnost_podr.csv)
Zdrojová data byla získána na stránkách [ČSÚ](https://csu.gov.cz/) ve formátu .xlsx ve vlastně parametrově nastavené tabulce. Následně byla data v excelu manuálně upravena dle metodiky blíže popsané v Jupyter notebooku. Ve zkratce je porodnost nutno extrahovat po kvartálech v jednotlivých rocích a dopočítat zhruba počet dětí, které budou mít následně za 3 roky právní nárok na to nastoupit do MŠ (tj. děti narozené do 31.srpna roku x + září-prosicen roku x -1). Porodnost zahrnuje i narození dětí s jiným občanstvím. 

## Questions / Feedback
Kontaktovat mě můžete na [LinkedIn](https://www.linkedin.com/in/klarabek/)