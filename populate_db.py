from models import Automobiliai, db
from app import app


with app.app_context():
    projects = [
        Automobiliai(gamintojas="BMW", modelis="X5", spalva="Juoda", metai="2015", kaina=10000.0),
        Automobiliai(gamintojas="BMW", modelis="E90", spalva="Juoda", metai="2010", kaina=8000.0),
        Automobiliai(gamintojas="BMW", modelis="X6", spalva="Balta", metai="2017", kaina=15000.0),
        Automobiliai(gamintojas="BMW", modelis="E46", spalva="Geltona", metai="2003", kaina=5000.0),
        Automobiliai(gamintojas="AUDI", modelis="A6", spalva="Raudona", metai="2011", kaina=4000.0),
        Automobiliai(gamintojas="AUDI", modelis="RS6", spalva="Melyna", metai="2018", kaina=50000.0),
        Automobiliai(gamintojas="AUDI", modelis="A5", spalva="Juoda", metai="2012", kaina=7000.0),
        Automobiliai(gamintojas="TOYOTA", modelis="Supra", spalva="Juoda", metai="1998", kaina=100000.0),
        Automobiliai(gamintojas="VW", modelis="GOLF", spalva="Balta", metai="2015", kaina=10000.0),
        Automobiliai(gamintojas="VW", modelis="PASSAT", spalva="Balta", metai="2017", kaina=14000.0),
        Automobiliai(gamintojas="VW", modelis="POLO", spalva="Melyna", metai="2014", kaina=4000.0),
    ]

    db.session.add_all(projects)
    db.session.commit()
    print("duomenys uzpildyti")