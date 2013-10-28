2) Requirement
--------------

* Python 3.3
* [Beautiful soup][1]
* [Requests][2]
* [html5lib][3]

3) Usage
--------

```bash
    python path/to/scscrapper.py Username
```

4) Output
---------

A file named sc-collection.json in same folder than script.

5) JSON schema
--------------

```python
    sub_categorie = {
        "type": "array",
        "items" : {
            "type" : "object",
            "properties": {
                "title" : {
                    "type": "string"
                },
                "originalTitle" : {
                    "type": "string"
                },
                "year" : {
                    "type": "string"
                },
                "authors" : {
                    "type": "array",
                    "items" : {
                        "type": "string"
                    }
                }
            }
        }
    }

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
```

[1]: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
[2]: https://github.com/kennethreitz/requests
[3]: https://pypi.python.org/pypi/html5lib
