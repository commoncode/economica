Economica
=========

A pragmatic model driven economic framework to take us beyond the shopping cart.

Simple expression of sophisticated, workflow guided, economic patterns that will drive the next wave of ecommerce enabled products & services.

Based on Resources, Events, Agents (REA) accounting model to empower developers with a common language toolset and framework to collaboratively solve any economic problem.

Build a single web store, build a multi-channel retail enterprise, build a completely new business model with Economica.

Built with Django.


Set up
------

With mongod running...

```
mkvirtualenv economica
git clone git@github.com:commoncode/economica.git
cd economica
pip install -r requirements/local.txt
./manage.py migrate
./manage.py create_categories
./manage.py create_products <type> [quantity]
./manage.py create_collections <type> [quantity]
./manage.py create_offers
./manage.py create_images
./manage.py create_image_instances offers.Offer
./manage.py runserver
```


Resources
---------

* Economica Home: http://economica.io
* Economica on Read the Docs: http://docs.economica.io or http://economica.readthedocs.org
* Economica Koding Group: TBC or search http://koding.com


License
-------

Pending


Authors
-------

Daryl Antony — Common Code and others to come.
