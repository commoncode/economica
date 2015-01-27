# Economica

A pragmatic model driven economic framework to take us beyond the shopping cart.

Simple expression of sophisticated, workflow guided, economic patterns that will drive the next wave of ecommerce enabled products & services.


## Purpose

Based on Resources, Events, Agents (REA) accounting model to empower developers with a common language toolset and framework to collaboratively solve any economic problem.

Build a single web store, build a multi-channel retail enterprise, build a completely new business model with Economica.

(Provide a RESTful API for commerce business with the next capabilities:

* CRUD Products
* CRUD Offers
* CRUD Clients
* CRUD Quotes
* Stock Management

Levering the API client to the user, they will be able to use any language and platform they want for it, from desktop "Point of Sales" to E-commerce websites.)


## Resources

* [Home](http://economica.io/)
* [Documentation](http://economica.readthedocs.org/)


## Setup

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


## Apps & Models

(We probably have *too many* models to begin with, would be safer to start with the basics and then scale according to our needs)


### Campaings

(Empty models yet, maybe they should be removed until we know exactly what do we need them for)

* campaings.Campaing
* campaings.CampaingPromotion


### Coupons

(Empty models yet, maybe they should be removed until we know exactly what do we need them for)

* coupons.Coupon


### Offers

(Too many models in one single App, either they are "too much" or we should split some of them)

* offers.Collection (may be moved to "collections app")
* offers.Offer (app's main model)
* offers.OfferResourceContract (we maybe should remove "Offer" prefix of the models)
* offers.OfferAspect
* offers.OfferPrice
* offers.OfferResource
* offers.OfferDiscount
* offers.OfferValidUntil
* offers.OfferStart
* offers.OfferEnd
* offers.OfferRelated
* offers.OfferFreeGift
* offers.OfferFreeShipping
* offers.OfferNForOne
* offers.OfferToAgent
* offers.OfferCoupon
* offers.OfferOnQuote


### Products

(Too many models in one single App, either they are "too much" or we should split some of them)

* products.Product (app's main model)
* products.Book (product type)
* products.Cosmetic (product type)
* products.Food (product type)
* products.Garment (product type)
* products.Session (product type)
* products.Software (product type)
* products.Vehicle (product type)
* products.Variant (variants should probably go on another app)
* products.VariantAspect (variants should probably go on another app)
* products.VariantSizeAspect (variants should probably go on another app)
* products.VariantShadeAspect (variants should probably go on another app)
* products.VariantColorAspect (variants should probably go on another app)
* products.AspectQuality (aspects should probably go on another app)
* products.Color (aspects should probably go on another app)
* products.Size (aspects should probably go on another app)
* products.Property (aspects should probably go on another app)
* products.VariantTemplate (variants should probably go on another app)
* products.VariantTemplateAspect (variants should probably go on another app)
* products.VariantTemplateAspectQuality (variants should probably go on another app)
* products.Category (category should probably go on another app)
* products.SmartCollection (smart collections should probably go on another app, collections?)
* products.VariantTemplateAspectQuality (variants should probably go on another app)
* products.SmartCollectionAspectInstance (smart collections should probably go on another app, collections?)
* products.SmartCollectionAspectRule (smart collections should probably go on another app, collections?)
* products.SmartCollectionAspect (smart collections should probably go on another app, collections?)


### Promotions

(Empty models yet, maybe they should be removed until we know exactly what do we need them for)

* promotions.Promotion


### Quotes

(Instead of "Carts" we use Quotes to handle transactions)

* quotes.Quote (app's main model)
* quotes.QuoteItem


### Services

(Empty models yet, maybe they should be removed until we know exactly what do we need them for)

* services.Service
* services.Consult


## REA

(Questions made so far:

* What exactly is an Event?
* What exactly is an Agent?
* What is rea-patterns-b2c for?
* Why do we need all the fragmentation?
* How exactly "translate it" to Economica?

To be discussed)


## Collections & Serializers

(These are required in order to store Instances as Serialized Documents into MongoDB, mostly for Meteor support, however to be capable of this we must subclass CQRSModel and CQRSPolymorphicModel for *almost* every model we have, and since our main goal is to provide an API to work with *any* language & platform the use of Collections & Serializers **should** be completely optional rather like plugin to install than a feature to ignore, there should be "healthier" ways to serialize Instances as Documents than subclassing Models. To be discussed.)

## License

Pending
