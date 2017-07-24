.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/pheaktra21/ckanext-fileremove.svg?branch=master
    :target: https://travis-ci.org/pheaktra21/ckanext-fileremove

.. image:: https://coveralls.io/repos/pheaktra21/ckanext-fileremove/badge.svg
  :target: https://coveralls.io/r/pheaktra21/ckanext-fileremove

.. image:: https://pypip.in/download/ckanext-fileremove/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-fileremove/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-fileremove/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-fileremove/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-fileremove/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-fileremove/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-fileremove/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-fileremove/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-fileremove/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-fileremove/
    :alt: License

=============
ckanext-fileremove
=============

Fileremove is a light extension for removing stored file in local directory.

While Filestore provides an ability to store file on local directory,
Datastore provides an ability to store data of the file in database and 
makes individual data elements accessible and queryable. However, if we
upload a file as a resource, and then delete it, the file is never
deleted from local directory. Both Filestore and Datastore do not provide
deleting file function. 

Therefore, Fileremove trys to omit this limitation by providing an 
ability to remove stored file from local directory at the same time
the resource is deleted from CKAN database.


------------
Requirements
------------

This extension was tested with CKAN version 2.6.2.


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-fileremove:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-fileremove Python package into your virtual environment::

     pip install ckanext-fileremove

3. Add ``fileremove`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

Document any optional config settings here. For example::

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.fileremove.some_setting = some_default_value


------------------------
Development Installation
------------------------

To install ckanext-fileremove for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/pheaktra21/ckanext-fileremove.git
    cd ckanext-fileremove
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.fileremove --cover-inclusive --cover-erase --cover-tests


---------------------------------
Registering ckanext-fileremove on PyPI
---------------------------------

ckanext-fileremove should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-fileremove. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


----------------------------------------
Releasing a New Version of ckanext-fileremove
----------------------------------------

ckanext-fileremove is availabe on PyPI as https://pypi.python.org/pypi/ckanext-fileremove.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags
