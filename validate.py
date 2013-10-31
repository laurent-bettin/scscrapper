__author__ = 'laurent'
import json
import validictory

sub_categorie = {
    "type": "array",
    "blank": True,
    "items" : {
        "type" : "object",
        "properties": {
            "title" : {
                "type": "string"
            },
            "original_title" : {
                "type": "string",
                "blank": True
            },
            "year" : {
                "type": "string",
                "blank": True
            },
            "authors" : {
                "type": "array",
                "items" : {
                    "type": "string",
                    "blank": True
                }
            }
        }
    }
}

#TODO : better Schema with optional categories or sub categories
categorie = {
    "type" : "object",
    "properties": {
        "wish": sub_categorie,
        "rating": sub_categorie,
        "shopping": sub_categorie
    }
}

collection = { "type": "object",
    "properties": {
        "films": categorie,
        "bd": categorie,
        "series": categorie,
        "livres": categorie,
        "jeuxvideo": categorie,
        "musique": categorie
    }
}

with open('sc-collection.json', 'r', encoding = 'UTF-8') as datas_input:
    sc_json = datas_input.read()

#TODO : better output
validictory.validate(json.loads(sc_json),collection)