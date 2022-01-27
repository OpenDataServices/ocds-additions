Command Line Interface (CLI)
============================

Create a repository
-------------------

Call this command, passing only the directory path you want to create.

Once created, you will want to change to the repository to run further actions.

You will probably want to create a new git repository.

.. code-block:: bash

    ocdsadditionsinit  my-new-data-repository-directory
    cd my-new-data-repository-directory
    git init

Repository actions
------------------

All these actions take place in a data repository. They should be run in the data directory - the directory with the `ocdsadditions.json` file in it.

Add Contracting Process
~~~~~~~~~~~~~~~~~~~~~~~

Every contracting process you want to work with needs to be added explicitly.

Call this command, passing the `Contracting Process Identifier (ocid) <https://standard.open-contracting.org/latest/en/schema/identifiers/#contracting-process-identifier-ocid>`_ of the process you want to work with.


.. code-block:: bash

    ocdsadditions addocid ocds-h6vhtk-02c615

Add External Release Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Goes to a URL, fetches a release package and adds all releases to the data repository.

.. code-block:: bash

    ocdsadditions addexternalreleasepackage   https://www.find-tender.service.gov.uk/api/1.0/ocdsReleasePackages/016035-2021

Add Empty Release
~~~~~~~~~~~~~~~~~

Adds an empty release to an contracting process with sensible defaults. More information can then be added to the release by hand.

You must pass:

* the `Contracting Process Identifier (ocid) <https://standard.open-contracting.org/latest/en/schema/identifiers/#contracting-process-identifier-ocid>`_
* the `Release ID <https://standard.open-contracting.org/latest/en/schema/identifiers/#release-id>`_

.. code-block:: bash

    ocdsadditions addemptyrelease ocds-h6vhtk-02c615 rel-id-1

Create Release Spreadsheet
~~~~~~~~~~~~~~~~~~~~~~~~~~

Turns a single release into a spreadsheet.

You must pass:

* the `Contracting Process Identifier (ocid) <https://standard.open-contracting.org/latest/en/schema/identifiers/#contracting-process-identifier-ocid>`_
* the `Release ID <https://standard.open-contracting.org/latest/en/schema/identifiers/#release-id>`_
* the filename to output the spreadsheet to. This must have a '.xlsx' or '.ods' extension.

.. code-block:: bash

    ocdsadditions createreleasespreadsheet ocds-h6vhtk-02c615 rel-id-1 output.xlsx

Import Spreadsheet
~~~~~~~~~~~~~~~~~~

Currently only release package spreadsheets can be imported.

You must pass:

* the filename to import. This must have a '.xlsx' or '.ods' extension.

.. code-block:: bash

    ocdsadditions importspreadsheet spreadsheet.xlsx

Build site
~~~~~~~~~~

Builds the static output site for this data repository.

Pass the output directory.

.. code-block:: bash

    ocdsadditions buildsite  _site

Option parameters are

* `-u`, `--url`: Specify the base URL the site will be served from - eg "http://localhost:8000"
