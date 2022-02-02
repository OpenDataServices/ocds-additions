Data Repository Config
======================

Once you have your data repository, you can edit parts of the `ocdsadditions.json` file to configure the site.

There should be a `config` key which is an object.

Publisher, License and Publication Policy
-----------------------------------------

Under `config` add a `package` key, which is an object with the following keys:

* Add a `publisher` key, which is a object.
* Add a `license` key, which is a string.
* Add a `publicationPolicy` key, which is a string.

`The contents are defined in the OCDS Standard <https://standard.open-contracting.org/latest/en/schema/release_package/>`_.

These are used when creating a new empty release - they are automatically set in the package for you.

Party
-----

Under `config` add a `party` key, which is an object with the following keys:

* Add a `name` key, which is a string. `The contents are defined in the OCDS Standard <https://standard.open-contracting.org/latest/en/schema/reference/#parties>`_.
* Add a `identifier` key, which is a object.  `The object is defined in the OCDS Standard <https://standard.open-contracting.org/latest/en/schema/reference/#identifier>`_.
* Add a `additionalIdentifiers` key, which is a list of objects. `The objects are defined in the OCDS Standard <https://standard.open-contracting.org/latest/en/schema/reference/#identifier>`_.
* Add a `address` key, which is a object. `The contents are defined in the OCDS Standard <https://standard.open-contracting.org/latest/en/schema/reference/#address>`_.
* Add a `contactPoint` key, which is a object. `The contents are defined in the OCDS Standard <https://standard.open-contracting.org/latest/en/schema/reference/#contactpoint>`_.

Inserting Party to empty releases
---------------------------------

Under `config` add a `add_party_to_our_releases_with_party_id` key, which is a string.

If `party` and this is set, when you make a new empty release the party data is automatically added for you.


Example
-------

After adding the above, you may have an `ocdsadditions.json` that looks like:

.. code-block:: json

    {
        "config": {
            "package": {
                "publisher": {
                    "name": "Example Co-op",
                    "scheme": "example-scheme",
                    "uid": "ecp",
                    "uri": "https://www.example.coop/"
                },
                "publicationPolicy": "https://www.example.coop/publication-policy",
                "license": "https://www.example.coop/data-license"
            },
            "party": {
                "name": "Example Co-op",
                "identifier": {
                    "scheme": "GB-COH",
                    "id": "EXAMPLE"
                },
                "additionalIdentifiers": [],
                "address": {
                    "streetAddress": "Example Co-op, 37 Example St",
                    "locality": "London",
                    "region": "",
                    "postalCode": "NW1 1AA",
                    "countryName": "United Kingdom of Great Britain and Northern Ireland"
                },
                "contactPoint": {
                    "email": "hello@example.coop"
                }
            },
            "add_party_to_our_releases_with_party_id": "GB-COH-EXAMPLE"
        }
    }

