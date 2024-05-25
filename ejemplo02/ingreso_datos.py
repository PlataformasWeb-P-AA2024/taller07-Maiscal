from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Club, Jugador
from configuracion import cadena_base_datos


engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()


datos_clubs = open("data/datos_clubs.txt", "r", encoding='utf-8')
clubs = []

for f in datos_clubs :
    nombreC, deporteC, fundacionC = f.strip().split(';')
    clubs.append(Club(nombre=nombreC , deporte=deporteC , fundacion=int(fundacionC)))

datos_clubs.close()
session.add_all(clubs)
session.commit()




datos_jugadores = open("data/datos_jugadores.txt", "r", encoding='utf-8')
jugadores = []

for x in datos_jugadores:
    nombreClub, posicionJ, dorsalJ, nombreJ = x.strip().split(';')
    club = session.query(Club).filter_by(nombre=nombreClub).one_or_none()
    if club:
        jugador = Jugador(nombre=nombreJ, dorsal=int(dorsalJ), posicion=posicionJ, club=club)
        session.add(jugador)
        jugadores.append(jugador)
    

datos_jugadores.close()
session.add_all(jugadores)
session.commit()
