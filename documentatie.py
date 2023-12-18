# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:40:44 2023

@author: bartd
"""

##################################################################################################
###Inladen v/d packages.
##################################################################################################

import streamlit as st
from PIL import Image

##################################################################################################
###Path toevoegen.
##################################################################################################

path = 'C:/Users/bartd/OneDrive/Bureaublad/Data Science (Minor)/Documentatie/'

st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_title = 'Documentatie', page_icon = "wrench")

##################################################################################################
###Sidebar met kiezen documentatie.
##################################################################################################



st.sidebar.subheader('**Opties**')
optie = st.sidebar.selectbox('Kies een optie voor documentatie:', ('Algemene Informatie', 'Tijdlijn', 'Plan van Aanpak', 'Overig'))
st.sidebar.divider()
st.sidebar.subheader('Laatste update')
st.sidebar.write('De laatste update van deze pagina is uitgevoerd op **18 december 2023** om 10:11:52')

if optie == 'Overig':
    st.subheader('**Referenties**')
    st.write('LinkedIn. (z.d.). [Logo van LinkedIn]. Geraadpleegd op 18 november 2023, van https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg')
    st.write('smartindustry. (z.d.). [Logo van Techport]. Geraadpleegd op 18 november 2023, van https://smartindustry.nl/fieldlab/fieldlab-smart-maintenance-techport')
    st.write('VanderEng B.V.. (z.d.). [Logo van Van der Eng]. Geraadpleegd op 18 november 2023, van https://vandereng.nl/')
    st.write('Autisme Expertise. (14 februari 2019). [Foto geen profielfoto]. Geraadpleegd op 19 november 2023, van https://www.autismeexpertise.nl/index.php/wie-zijn-wij/profielfoto/')
    st.divider()
    
    st.subheader('**Terminologie**')
    term1a, term1b = st.columns((0.2, 1.5))
    with term1a:
        st.write('**Meltzer:**')
    with term1b: 
        st.write('Een Meltzer is een apparaat dat bij Van der Eng staat om etiketten te produceren.')
    
    term2a, term2b = st.columns((0.2, 1.5))
    with term2a:
        st.write('**RaspberryPi:**')
    with term2b:
        st.write('''Een RaspberryPi is een minicomputer. Hierop kan ook een hdmi-kabel en muis en toetsenbord aangesloten worden. Deze staat bij Van der Eng
                 om berekeningen uit te voeren, en alle data up te loaden naar het netwerk van Van der Eng. Voor meer info, zie https://www.raspberrypi.com/.
                 ''')

    term3a, term3b = st.columns((0.2, 1.5))
    with term3a:
        st.write('**Arduino:**')
    with term3b:
        st.write('''Een Arduino is een computer die het makkelijker maakt om met sensoren te werken. Deze is aangesloten op de sensor bij Van der Eng, en verbonden
                 met een ethernet kabel op de RaspberryPi om daar de data naartoe te sturen. Voor meer info, zie https://www.arduino.cc/.
                 ''')


##################################################################################################
###Wat is de opdracht.
##################################################################################################

if optie == 'Algemene Informatie':
    
    st.title('Case Van der Eng // Techport')
    st.write('''
             Op 13 november 2023 begon het nieuwe blok van de minor Data Science aan de Hogeschool
             van Amsterdam. Daar komt ook een track en case bij kijken. Wij (Akin Akinola, Boet Rijnders
             en Bart de Beus) zijn ingedeeld bij de track Smart Industry, en de case Van der Eng //
             Techport.\n
             In deze dashboard zullen we documentatie van het project bijhouden voor onze opdrachtgevers
             Andre Gerver en Hamza Arrahmani, en onze begeleider Jurjen Helmus. \n
             De verschillende tabbladen met informatie zijn het Plan van Aanpak, met de opdrachtbeschrijving. 
             Ook is er een tijdlijn met wat er redelijk per dag is gebeurd. Ook is er een overig tab. Hierin staan
             zowel verschillende referenties als uitleg van bepaalde termen.
             ''')
    st.divider()
             
##################################################################################################
###Wie wij zijn.
##################################################################################################

    st.subheader('Ons team:')
    tab_akin, tab_bart, tab_boet = st.tabs(['Akin Akinola', 'Bart de Beus', 'Boet Rijnders'])
    
    text_akin = '''
    Ik ben Akin Akinola en volg de studie Commerciële Economie aan de Hogeschool van Amsterdam. Marketing is iets dat 
    altijd mijn interesse heeft gehad. Het creëren van posters, slogans en merk-logo’s zijn voor mij leuke bezigheden om mijn 
    creativiteit te uiten. In combinatie met mijn fashion interesse heb ik al sinds jong een passie voor kleding en daarbij 
    ook het creëren van complete looks. Dit kan voor personen zijn maar ook als visual merchandise van bedrijven/winkels.
    
    Op dit moment zit ik in het derde jaar van de studie en volg ik de minor Data Science. Mijn doel is om in de toekomst data te 
    kunnen analyseren, visualiseren en te bewerken tot iets bruikbaars, waarmee je marketing nog beter kan afstemmen op wat het meest 
    efficiënt en winstgevend is.
    '''
    
    text_boet = '''
    Ik ben Boet, 23 jaar en kom uit Amstelveen. Drie jaar geleden is de wereld van data voor mij geopend toen ik begon bij 
    SOCIALDATABASE.com. Dit is ook de reden waarom ik heb gekozen voor de minor Data Science. Data science is een opwindend 
    en snelgroeiend veld dat veel kansen biedt. Naast de wereld  van data hou ik ook van sporten en leuke dingen doen 
    met mijn vrienden.
    '''
    
    text_bart = '''
    Mijn naam is Bart de Beus, en ik ben een 20-jarige student uit Bennebroek. Ik studeer Toegepaste Wiskunde aan de Hogeschool 
    van Amsterdam. Ik heb altijd een passie gehad voor puzzelen, wat ook de reden is dat ik bij Wiskunde terecht ben gekomen. Eigenlijk 
    zijn de wiskundige formules voor mij een net iets andere manier van uitdagende puzzels. Daarbij ben ik ook een erg 
    leergierige en gemotiveerde student, die analytisch en kritisch is ingesteld.  
    
    Buiten de Hogeschool om ben ik vaak te vinden in Haarlem of Zandvoort, op het voetbalveld of bij de tennis of padel. Ook ben ik de 
    trainer van de jongens onder 16-1 van mijn lokale voetbalclub, waar ik ook twee keer per week sta.  
    '''
    
    with tab_akin:
        col1, col2 = st.columns((1.5, 0.5))
        with col1:
            st.write(text_akin)    
            col1a, col1b = st.columns((0.3, 1.5))
            with col1a:
                '''
                [![Repo](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/akin-akinola/) 
                
                '''
                st.markdown("<br>",unsafe_allow_html=True)
            with col1b:
                    st.write('**Telefoon:** +31 6 80159992')        
                    st.write('**E-mail  :** akin.akinola@hva.nl')
        with col2:
            image = Image.open(f'akinakinola.jpg')
            st.image(image, width = 200)
        st.divider()

    with tab_boet:
        col3, col4 = st.columns((1.5, 0.5))
        with col3:
            st.write(text_boet)    
            col3a, col3b = st.columns((0.3, 1.5))
            with col3a:
                '''
                [![Repo](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/boet-rijnders-b6234a166/) 
                
                '''
                st.markdown("<br>",unsafe_allow_html=True)
            with col3b:
                st.write('**Telefoon:** +31 6 26165574')        
                st.write('**E-mail  :** boet.rijnders@hva.nl')
        with col4:
            image = Image.open(f'boetrijnders.png')
            st.image(image, width = 200)
        st.divider()

    with tab_bart:
        col5, col6 = st.columns((1.5, 0.5))
        with col5:
            st.write(text_bart)
            col5a, col5b = st.columns((0.3, 1.5))
            with col5a:
                '''
                [![Repo](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/bart-de-beus-1b895a1b6/) 
                
                '''
                st.markdown("<br>",unsafe_allow_html=True)
            with col5b:
                st.write('**Telefoon:** +31 6 39131273')        
                st.write('**E-mail  :** bart.de.beus@hva.nl')
        with col6:
            image = Image.open(f'bartdebeus.jpeg')
            st.image(image, width = 200)
        st.divider()
        
##################################################################################################
###Over de opdrachtgever.
##################################################################################################    
    
    st.subheader('Over de opdrachtgever:')
             
    tab_techport, tab_vandereng = st.tabs(['Techport', 'Van der Eng'])
             
    text_vandereng = '''[Van der Eng](https://vandereng.nl/)
    is een ambachtelijke, maar uiterst innovatieve en moderne organisatie. Inmiddels
    heeft het bedrijf ruim 120 jaar ervaring in het ontwikkelen en produceren van hoogwardige labels en etiketten. 
    Hun producten worden wereldwijd ingezet voor de identificatie van producten, processen en personen in een breed aantal
    branches.
    '''
    text_vandereng2 = '''Onze contactpersoon is Hamza Arrahmani, hoofd financiële administratie 
    bij Van der Eng. Tevens heeft hij ook aan de Hogeschool van Amsterdam gestudeerd. De directeur van het bedrijf 
    is Ernst de Haas. 
    '''     
    
    text_techport = '''[Techport](https://techport.nl/) is dé publiek-private samenwerking van meer dan 90 bedrijven, scholen en overheden met als 
    doel de eerste groene industriezone van Nederland te worden. Ze zijn actief in de IJmond, een dynamische regio waarin 
    de industrie voor grote opgave staat om te verduurzamen. Techport stimuleert zij-instroom, versnelt technologische innovatie 
    en ontwikkelt regionaal opleidingsaanbod voor de banen van toekomst.
    '''
    
    text_techport2 = '''Onze contactpersoon bij Techport is Andre Gerver, quartermaster TinyML / Edge AI. 
    '''
             
    with tab_vandereng:
        col7, col8 = st.columns((1.5, 0.5))
        with col7:
            st.write(text_vandereng)
            st.write(text_vandereng2)
        with col8:
            st.write('')
            st.write('')
            image = Image.open(f'vandereng.png')
            st.image(image, width = 200)
            
    with tab_techport:
        col9, col10 = st.columns((1.5, 0.5))
        with col9:
            st.write(text_techport)
            st.write(text_techport2)
        with col10:
            st.write('')
            st.write('')
            image = Image.open(f'techport.png')
            st.image(image, width = 200)
            
        
##################################################################################################
###Tijdlijn:
################################################################################################## 
    
if optie == 'Tijdlijn':
    st.markdown("<h1 style='text-align: center;'>Tijdlijn</h1>", unsafe_allow_html = True)
    st.divider()
    
    st.markdown("<h3 style='text-align: center;'>Week 1</h3>", unsafe_allow_html = True)   
    
    col13a, col13b = st.columns((0.2, 1.5))
    with col13a:
        st.write('**13 november:**')
    with col13b:
        st.write('''Op deze dag was de kick-off van de track Smart Industry en hierbij kregen we ook een meer gedetailleerde
                 uitleg over onze specifieke opdracht. We zijn ingedeeld bij de Voorcalculatie opdracht van Van der Eng //
                 Techport. Ook hebben we contact gelegd met Andre Gerver van het bedrijf techport. Hij heeft ons het werk van het vorige 
                 groepje doorgestuurd en de contactgegevens van Hamza Arrahmani (contactpersoon van Van der Eng) gedeeld, zodat 
                 we ook snel met hem contact op konden nemen.
                 ''')
    
    col14a, col14b = st.columns((0.2, 1.5))
    with col14a:
        st.write('**14 november:**')
    with col14b:
        st.write('''Op 14 november is er voor het eerst contact opgenomen met Daan van der Hoek, een van de teamleden van het 
                 vorige groepje. Zij hebben een sensor gemaakt en geïnstaleerd bij Van der Eng, die verschillende data opneemt.
                 Omdat wij doorbouwen op hun werk, is er besloten om een afspraak met Daan te maken, waarbij we eventuele vragen
                 aan hem kunnen stellen. Ook kunnen we zo eventuele plannen en ideeën die zij hadden ten uitvoer brengen, waar
                 wij mogelijk pas later op gekomen waren.
                 ''')
                 
    col15a, col15b = st.columns((0.2, 1.5))
    with col15a:
        st.write('**15 november:**')
    with col15b:
        st.write('''Er is contact gelegd met Hamza Arrahmani. Er is besloten om op locatie (in Heemskerk) af te spreken, zodat we
                 een tour kunnen maken door het bedrijf en hopelijk zo een beter inzicht kunnen krijgen over hoe en wat precies de
                 bedoeling is, wat de vereisten zijn en in het algemeen hoe het bedrijf eruit ziet.
                 ''')
        
    col17a, col17b = st.columns((0.2, 1.5))
    with col17a:
        st.write('**17 november:**')
    with col17b:
        st.write('''We zijn voor het eerst langsgegaan bij Van der Eng. Hier hebben we een goed inzicht gekregen van wat de sensor
                 die het vorige groepje gebruikt precies doet. Ook hebben we een beter beeld gekregen van wat precies de opdracht is
                 en wat er van ons wordt verwacht. Daarnaast hebben we van Hamza verschillende paketten data gekregen, namelijk hoe
                 de voorcalculatie nu wordt berekend en de ShopFloor orders (een voorbeeld van hoe de orders binnen komen naar de
                 werkbanken). Daarnaast hebben we ook Ernst de Haas ontmoet, de directeur van Van der Eng. 
                 ''')
    col17_1, col17_2, col17_3 = st.columns((0.3, 0.3, 0.3))
    with col17_1:
        image = Image.open(f'17nov_1.jpeg')
        st.image(image, caption='Van der Eng in Heemskerk', width = 350)         
    with col17_2:
        image = Image.open(f'17nov_2.jpeg')
        st.image(image, caption='Werkbank waarop de orders worden verwerkt', width = 350)           
    with col17_3:
        image = Image.open(f'17nov_3.jpeg')
        st.image(image, caption='Sensor geplaatst door het vorige groepje', width = 350)    


    st.divider()
    st.markdown("<h3 style='text-align: center;'>Week 2</h3>", unsafe_allow_html = True)   

    col21a, col21b = st.columns((0.2, 1.5)) 
    with col21a:
        st.write('**21 november:**')
    with col21b:
        col21b_1, col21b_2 = st.columns((1, 0.3))
        with col21b_1:
            st.write('''Er is gesproken met Daan van der Hoek. Hierbij is aan het woord gekomen wat er eventueel verbeterd zou kunnen worden aan
                     de sensor (bijvoorbeeld vergroting van gaten) en waar nog meer naar gekeken kan worden. Ook is er besproken wat er volgens 
                     hun nog met de data gedaan kan worden. Ook is het algemene proces besproken en hoe wij de sensor zouden kunnen maken. Eventuele
                     tips en aanraders zijn ook genoemd.
                     ''')
        with col21b_2:
            image1 = Image.open(f'21nov_1.jpeg')
            st.image(image1, caption = 'Gesprek met Daan van der Hoek op de HvA')
    
    col23a, col23b = st.columns((0.2, 1.5))
    with col23a:
        st.write('**23 november:**')
    with col23b:
        st.write('''Op deze dag is de conceptversie van het Plan van Aanpak afgerond. Deze is ingeleverd in de digitale omgeving van de Hogeschool, 
                 en op dinsdag 28 november wordt de feedback verwacht, waarmee de definitieve versie van het Plan van Aanpak afgerond kan worden.
                 ''')
                 
    col24a, col24b = st.columns((0.2, 1.5))
    with col24a:
        st.write('**24 november:**')
    with col24b:
        col24b_1, col24b_2 = st.columns((1, 0.3))
        with col24b_1:
            st.write('''We zijn weer langsgegaan bij Van der Eng in Heemskerk. Daar was de planning om metingen te doen en deze te vergelijken met de
                     data in de server. Echter is er gemerkt dat er maar hele beperkte data in de server staat, namelijk voor 22 en 29 juni 2023. Dit 
                     waren de dagen dat het vorige groepje de sensor heeft getest. Het kan zijn dat het ergens anders binnen de server is opgeslagen,
                     of dat er een fout is in de code. Hiervoor is er contact opgenomen met Daan van der Hoek, en hij heeft ons doorverwezen naar 
                     Alaric de Ruiter. 
                     ''')
        with col24b_2:
            video_file = open('24nov_1.mp4', 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes, start_time = 0)
        with col24b:
            st.write('''Ook is er gesproken met Andre Gerver via Microsoft Teams. Hierin hebben wij onszelf opnieuw voorgesteld, alleen nu met ons gezicht
                     er ook bij. Hij heeft ons meerdere handige tips gegeven voor gedurende het proces. De dag van de wekelijkse consult is gewijzigd van
                     vrijdag naar maandag. Dit omdat dat beter uitkwam i.v.m. bedrijfsmeetings.
                     ''')
                     
    st.divider()
    st.markdown("<h3 style='text-align: center;'>Week 3</h3>", unsafe_allow_html = True) 
    
    
    col27a, col27b = st.columns((0.2, 1.5))
    with col27a:
        st.write('**27 november:**')
    with col27b:
        st.write('''Er is contact gelegd met Alaric de Ruiter. Het niet doorverwijzen van de data kan liggen aan verschillende zaken, namelijk als eerste
                 dat de bedrading tussen de verschillende componenten niet goed is blijven zitten. Om dit te checken kunnen we een script runnen binnen de 
                 RaspberryPi, en als er data binnenkomt ligt het in ieder geval niet hieraan. De verbinding tussen de RaspberryPi en de server is ook niet heel stabiel, dus het is
                 ook mogelijk dat er wel data binnenkomt en verzameld wordt, maar dat er simpelweg geen data wordt gestuurd naar de server.
                 ''')
    
    col28a, col28b = st.columns((0.2, 1.5))
    with col28a:
        st.write('**28 november:**')
    with col28b:
        st.write('''Vanuit de Track Smart Industry was er een werkcollege, waarmee aan de slag is gegaan met een RaspberryPi. Hierbij is een SenseHat sensor
                 gebruikt, die bijvoorbeeld de luchtvochtigheid en temperatuur kan meten. Er is afgesproken dat wij er een mee kunnen nemen, om mee te oefenen
                 voor de sensor die bij Van der Eng staat. Daar zullen we verder in week 3 mee aan de slag gaan. 
                 ''')
    
    col1a, col1b = st.columns((0.2, 1.5))
    with col1a:
        st.write('**1 december:**')
    with col1b:
        st.write('''Op 1 december moest het definitieve Plan van Aanpak ingeleverd worden. Voor het eindproduct, zie Plan van Aanpak.
                 ''')

    st.divider()
    st.markdown("<h3 style='text-align: center;'>Week 4</h3>", unsafe_allow_html = True) 

    col4a, col4b = st.columns((0.2, 1.5))
    with col4a:
        st.write('**4 december:**')
    with col4b:
        st.write('''Op deze dag is met Roald Teunissen (van het Maintenance Lab) geregeld dat we een kleine monitor en een logitech 
                 toetsenbord met geïntegreerde muis mogen lenen. Deze kunnen we gemakkelijk aansluiten met de RaspberryPi, zodat we niet het
                 hele systeem hoeven los te breken.  
                 ''')  
        
    col6a, col6b = st.columns((0.2, 1.5))
    with col6a:
        st.write('**6 december:**')
    with col6b:
        col6b_1, col6b_2 = st.columns((1, 0.3))
        with col6b_1:
            st.write('''Op de 6e zijn we weer langsgegaan in Heemskerk. Hier kwamen we met vernieuwde kennis van de geleende RaspberryPi en de materialen
                     geleend vanuit het Maintenance Lab op de Hogeschool. Echter kwamen we er snel achter dat het ons niet lukte om het systeem in te komen, 
                     aangezien de gebruikersnaam en het wachtwoord niet bekend waren bij zowel ons als intern bij Van der Eng. Daarom is er besloten om een nieuwe
                     SD-kaart te halen, en hier opnieuw de (vernieuwde) software op te installeren met behulp van de gebruiksaanwijzingen. 
                     ''')
        with col6b_2:
            image1 = Image.open(f'6dec_1.jpg')
            st.image(image1, caption = 'De RaspberryPi losgehaald van de machine')  
    with col6b:
        st.write('''Helaas lukte het niet om dit goed te installeren vanaf de computer. Dit omdat er problemen waren met het SSH proces (waarmee de RaspberryPi wordt gelinkt met de laptop) 
                waardoor er niks geüpload naar de RaspberryPi kon worden. Daarom is er toch besloten om de RaspberryPi zelf los te halen, maar de sensor te laten zitten. Deze is mee terug genomen naar een WiFi 
                waarin het eerder wel is gelukt deze twee systemen te linken. Hier is alle (vernieuwde) software geüpload naar de RaspberryPi, en ook is 
                de software veranderd van de Lite naar de normale versie. Er is besloten om op 7 december direct weer langs te gaan om de vernieuwde software
                te testen bij Van der Eng. 
                ''')
        
    col7deca, col7decb = st.columns((0.2, 1.5))
    with col7deca:
        st.write('**7 december:**')
    with col7decb:
        st.write('''Het is gelukt om de RaspberryPi met de verniewde software aan te sluiten op het systeem. Deze is online gekregen, en is nu ook verbindbaar
                 met de laptop. Er is met verschillende geüpdatet programma's geprobeerd de sensor weer aan de praat te krijgen. Dit is maar deels gelukt, de RaspberryPi kant
                 van de sensor krijgen we namelijk wel degelijk metingen van (staat de sensor aan/uit), en het programma is nu ook runnend (aan) gekregen. Echter krijgen we van de sensor
                 verbonden met de Arduino geen metingen binnen. Dit is niet werkbaar gekregen, en daarom is er ook besloten om de sensor van de Meltzer af te halen en mee
                 te nemen naar Amsterdam voor evaluatie. 
                 ''')
    
    st.divider()
    st.markdown("<h3 style='text-align: center;'>Week 5</h3>", unsafe_allow_html = True) 

    col11deca, col11decb = st.columns((0.2, 1.5))
    with col11deca:
        st.write('**11 december:**')
    with col11decb:
        col11decb_1, col11decb_2 = st.columns((1, 0.3))
        with col11decb_1:
            st.write('''De sensor (inclusief Arduino) is meegenomen naar Amsterdam. Hier is het gehele systeem veilig uit elkaar gehaald om te kijken of ieder geval de kabels nog
                     aan elkaar zaten, aangezien dit het geval was zou de bedrading dus theoretisch gezien geen probleem moeten zijn. Daarom is er besloten om vooral eerst te focussen op de 
                     software kant. Roald Teunissen heeft ons aangeraden het programma Arduino IDE te gebruiken voor de software van de Arduino, hiervoor is echter een ethernet connectie nodig,
                     wat wij op de 11e niet konden realiseren. Daarom is dit uitgesteld naar 12 december. 's Middags hebben we ook ons wekelijks gesprek gehad met Andre Gerver. Die heeft ons ook 
                     de goede kant op geduwd met een paar nuttige tips, zoals een andere systeem te gebruiken in combinatie met de Arduino (wat over het WiFi netwerk zou gaan i.p.v. ethernet).
                    ''')
        with col11decb_2:
            image1 = Image.open(f'11dec_1.jpg')
            st.image(image1, caption = 'Arduino met bedrading losgemaakt')  
    
    col12deca, col12decb = st.columns((0.2, 1.5))
    with col12deca:
        st.write('**12 december:**')
    with col12decb:
        st.write('''Aangezien alle bedrading goed in elkaar zat is er gekeken naar de software kant van de Arduino en RaspberryPi. De code op de Arduino leek verkeerd te zijn. Met behulp van Arduino IDE
                 is er geprobeerd om in te loggen op de Arduino om te kijken of die wel überhaupt wel metingen deed. Echter kwamen we de Arduino IDE niet binnen. Daarop heeft Jurjen Helmus iemand aangeraden 
                 om mee te zitten, en met hem zijn we erachter gekomen dat het een IP-adres probleem was. We zijn namelijk aangesloten met een ethernet kabel, en hier sturen we de metingen doorheen. Het 
                 bleek alleen dat we de Arduino geen IP-adres gaven om mee te verbinden. Dit kan gedaan worden met een code, maar dit moet automatisch gebeuren wanneer het gehele
                 systeem opstart.
                 ''')
        
    col13deca, col13decb = st.columns((0.2, 1.5))
    with col13deca:
        st.write('**13 december:**')
    with col13decb:
        st.write('''Er is hier geprobeerd om ervoor te zorgen dat de sensor automatisch een IP-adres meegeeft aan de ethernet kabel om de metingen binnen te krijgen. Dit is gelukt door de oude Arduino code een
                 beetje aan te passen, en de geupdate versie mee up te loaden naar de Arduino. Hierdoor kunnen we bij het opstarten gelijk metingen binnen krijgen zonder eerst handmatig een lijn code mee te geven 
                 (wat voor dagelijks gebruik vrij onhandig is). Ook is er gelijk voor gezorgd dat de metingen worden weggeschreven in een CSV bestand, wat wordt opgeslagen op de RaspberryPi zelf in plaats van 
                 weggeschreven naar de server wat eerst het geval was.
                 ''')
    
    col14deca, col14decb = st.columns((0.2, 1.5))
    with col14deca:
        st.write('**14 december:**')
    with col14decb:
        st.write('''De sensor is weer meegenomen naar Heemskerk om terug aan te sluiten op de Meltzer. Wat alleen bleek wanneer we probeerden metingen te verichten, is dat elke meting van de sensor verder weg dan
                 79 millimeter niet correct werd geregistreerd. Dit lijkt echter alleen een probleem te zijn wanneer de sensor is aangesloten in de er speciaal voor gemaakte 3d-geprinte houder. Een probleem kan zijn
                 (wat eerder ook is benoemd) dat de oogjes van de print te kijken zijn voor sensor, waardoor die een beetje gaat vervormen. Daarom moet dit gedeelte opnieuw ontwikkeld worden. Verder kan de code wel 
                 een beetje verbeterd en opgeschoont worden, maar het lijkt op zichzelf erg goed te werken, ook als we de Meltzer aan het uit zetten. 
                 ''')
        
  
    
    
    
    
    
##################################################################################################
###Plan van Aanpak:
##################################################################################################         
        
if optie == 'Plan van Aanpak':
    st.markdown("<h1 style='text-align: center;'>Plan van Aanpak</h1>", unsafe_allow_html = True)  
    st.write('''Dit is de derde versie van het Plan van Aanpak. De eerste is verbeterd met behulp van feedback van medestudenten. Daarna is echter de opdracht
             deels veranderd. Daarom is besloten om nog een keer feedback te vragen bij Inge Kilian (begeleider Business Analytics), en daaruit is de derde versie
             gekomen.
             ''')
    st.divider()

    pva1, pva2 = st.columns((0.5, 0.5))
    with pva1:
        image2 = Image.open(f'PvA14.png')
        st.image(image2, width = 500)
        st.divider()
        
        image2 = Image.open(f'PvA3.png')
        st.image(image2, width = 500)
        st.divider()
        
        image2 = Image.open(f'PvA5.png')
        st.image(image2, width = 500)
        st.divider()
        
        image2 = Image.open(f'PvA7.png')
        st.image(image2, width = 500)
        st.divider()
        
        image2 = Image.open(f'PvA9.png')
        st.image(image2, width = 500)
        st.divider()
        
        image2 = Image.open(f'PvA11.png')
        st.image(image2, width = 500)
        st.divider()
        
        image2 = Image.open(f'PvA13.png')
        st.image(image2, width = 500)
 
    with pva2:
        image2 = Image.open(f'PvA2.png')
        st.image(image2, width = 500)
        st.divider()
        
        image2 = Image.open(f'PvA4.png')
        st.image(image2, width = 500)
        st.divider()
        
        image2 = Image.open(f'PvA6.png')
        st.image(image2, width = 500)
        st.divider()
        
        image2 = Image.open(f'PvA8.png')
        st.image(image2, width = 500)
        st.divider()
        
        image2 = Image.open(f'PvA10.png')
        st.image(image2, width = 500)
        st.divider()
        
        image2 = Image.open(f'PvA12.png')
        st.image(image2, width = 500)
        st.divider()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

