from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project("Ohtutesting app", "Sovellus joka toimii testisyötteenä ohtun osan 2 laskareihin", "MIT", ["Matti Luukkainen", "Kalle Ilves"], ["python", "Flask", "editdistance"], ["coverage", "robotframework", "robotframework-seleniumlibrary", "requests"])
