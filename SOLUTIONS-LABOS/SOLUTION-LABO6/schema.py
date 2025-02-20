insert_schema = {
    'type': 'object',
    'required': ['titre', 'auteur', 'annee', 'nb_pages', 'nb_chapitres'],
    'properties': {
        'titre': {
            'type': 'string'
        },
        'auteur': {
            'type': 'string'
        },
        'annee': {
            'type': 'number'
        },
        'nb_pages': {
            'type': 'number'
        },
        'nb_chapitres': {
            'type': 'number'
        }
    },
    'additionalProperties': False
}