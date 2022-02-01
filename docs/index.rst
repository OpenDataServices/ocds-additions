OCDS Additions
==============

**Situation:** Somebody wants to take `OCDS (Open Contracting Data Standard) <https://standard.open-contracting.org/latest/en/>`_ releases that are already published by another publisher. They have additional information to share and they want to publish new releases with that information into the existing contracting process.

**For example:** A provider of social care has won a contract from the government to provide social care. The "tender" stages of that contract are published in a national tender portal in OCDS format. However no further stages are published. The provider wants to publish their own "award", "contract" and "implementation" releases to the same contracting process, so others can understand their work and the context it takes place in.

**OCDS Additions can help!** It is a tool to take releases from other portals, store them, and allow additional releases to be created and stored.

**Interface:** The tool is provided as a Python CLI tool that works on local files.

**Data storage:** The tool stores it's data in a git repository. There are many places this can be easily hosted for free, thus making the data store sustainable over the long term.

**Outputs:** The tool creates a static website that can be served by many web hosts. This provides all OCDS releases, compiled records and helpful information. It provides machine readable links so that it is easy for data collection tools like `Kingfisher Collect <https://kingfisher-collect.readthedocs.io/en/latest/>`_ to scrape the data.


.. toctree::
   :maxdepth: 3

   install.rst
   cli.rst
   repo-config.rst

