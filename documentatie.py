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

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

##################################################################################################
###Sidebar met kiezen week.
##################################################################################################

st.sidebar.subheader('**Opties**')
optie = st.sidebar.selectbox('Kies een optie voor documentatie:', ('Opdrachtinformatie', 'Tijdlijn', 'Plan van Aanpak'))

st.sidebar.subheader('**Referenties**')
st.sidebar.write('LinkedIn. (z.d.). [Logo van LinkedIn]. Geraadpleegd op 18 november 2023, van https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg')
st.sidebar.write('smartindustry. (z.d.). [Logo van Techport]. Geraadpleegd op 18 november 2023, van https://smartindustry.nl/fieldlab/fieldlab-smart-maintenance-techport')
st.sidebar.write('VanderEng B.V.. (z.d.). [Logo van Van der Eng]. Geraadpleegd op 18 november 2023, van https://vandereng.nl/')
st.sidebar.write('Autisme Expertise. (14 februari 2019). [Foto geen profielfoto]. Geraadpleegd op 19 november 2023, van https://www.autismeexpertise.nl/index.php/wie-zijn-wij/profielfoto/')


##################################################################################################
###Wat is de opdracht.
##################################################################################################

if optie == 'Opdrachtinformatie':
    
    st.title('Case Van der Eng // Techport')
    st.write('''
             Op 13 november 2023 begint het nieuwe blok van de minor Data Science aan de Hogeschool
             van Amsterdam. Daar komt ook een track en case bij kijken. Wij (Akin Akinola, Boet Rijnders
                                                                             en Bart de Beus) zijn ingedeeld bij de track Smart Industry, en de case Van der Eng //
             Techport.\n
             In deze dashboard zullen we documentatie van het project bijhouden voor onze opdrachtgevers
             Andre Gerver en Hamza Arrahmani, en onze begeleider Jurjen Helmus. 
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
    SOCIALDATABASE.com. Dit is ook de reden waarom ik heb gekozen voor de minor Data Science. Data Science is een opwindend 
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
    text_vandereng2 = '''Onze contactpersoon bij Van der Eng is Hamza Arrahmani, hoofd financiële administratie 
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
        st.write('''**Gepland** Het gesprek met Daan van der Hoek.
                 ''')

    col24a, col24b = st.columns((0.2, 1.5)) 
    with col21a:
        st.write('**24 november:**')
    with col21b:
        st.write('''**Gepland** Het consult met Andre Gerver.
                 ''')        
        
##################################################################################################
###Plan van Aanpak:
##################################################################################################         
        
if optie == 'Plan van Aanpak':
    st.markdown("<h1 style='text-align: center;'>Plan van Aanpak</h1>", unsafe_allow_html = True)   
    st.write('**Het Plan van Aanpak is nog in ontwikkeling, en wordt later in week 2 verwacht...**')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

