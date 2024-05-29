from dataclasses import dataclass

from dataclasses import dataclass


@dataclass
class Personne:
    nom: str
    prenom: str
    date_naissance: str


@dataclass
class Adresse:
    adresse_postal: str
    code_postal: str
    ville: str


@dataclass
class Contact:
    telephone: str
    adresse_mail: str


@dataclass
class RepertoireTelephonique:
    personnes: list
    contact: Contact
    adresse: Adresse

    def __str__(self):
        output = "Répertoire téléphonique :\n"
        for personne in self.personnes:
            output += f"Nom: {personne.nom}, Prénom: {personne.prenom}, Date de naissance: {personne.date_naissance}\n"
        output += f"Contact: Téléphone: {self.contact.telephone}, Adresse mail: {self.contact.adresse_mail}\n"
        output += f"Adresse: {self.adresse.adresse_postal}, {self.adresse.code_postal}, {self.adresse.ville}"
        return output


# Exemple d'utilisation
if __name__ == "__main__":
    personne1 = Personne("Doe", "John", "01/01/1990")
    personne2 = Personne("Smith", "Alice", "15/05/1985")

    contact = Contact("123456789", "john.doe@example.com")
    adresse = Adresse("123 rue de la Liberté", "75001", "Paris")

    repertoire = RepertoireTelephonique([personne1, personne2], contact, adresse)

    print(repertoire)
