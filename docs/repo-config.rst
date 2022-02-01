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
            }
        }
    }

