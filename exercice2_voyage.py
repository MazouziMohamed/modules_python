def hotel_frais(nombre_nuits) :
    return nombre_nuits*90
def location_voiture_frais(nombre_jours) :
    if nombre_jours < 3 :
        return nombre_jours*35
    elif nombre_jours < 7 :
        return nombre_jours*35 - 20
    else :
        return nombre_jours*35 - 50
def vol_frais(nom_ville) :
    if nom_ville == 'Marrakech' :
        return 35
    elif nom_ville == 'Paris' :
        return 200
    elif nom_ville == 'Oran' :
            return 78
    elif nom_ville == 'Carthage' :
            return 182
    elif nom_ville == 'Dakar' :
            return 25
def voyage_frais(nombre_nuits, nombre_jours, nom_ville, autres_frais) :
     return hotel_frais(nombre_nuits) + location_voiture_frais(nombre_jours) + vol_frais(nom_ville) + autres_frais