## Economica Enterprise

Economica adapts perfectly to the Enterprise with the Resource, Event, Agent model.  Enterprise often consist of 1 to _n_ Agents and each of those Agents may maintain a separate Store, create a Market (with Stores) or maintain a Store within a Market (MarketStore).

The Product base is instantiated upon an Agent's Store, pulling together Currency, Region and Lingual parameters.  The Product base is serialised into a key/value store with an interchangeable Backend (Mongo/Redis/Memcached etc.) and consumed by an application environement of choice, such as Angular or Meteor.

The Client Application interacts with the Economica API to carry out Economic Patterns such as Sales Purchases, Sales Orders or Recurring Subscriptions.

The Client Application can implement its own Cart logic, however, the Economica API also implements Cart.


## Dependencies

+ Canvas
+ Infrastruction
+ Entropy
+ Platforms
+ REA (Foundational polymorphic Resource, Event & Agent models)
+ Market (REA Market entities & patterns)
  - Purchase order patterns

Not yet built:
+ Stores
+ People

More REA:

+ Enterprise
  - REA enterprise level entities and patterns
+ Retail
  - REA entites and patterns for large scale retail

+ Wallet (REA alternate credit and currency systems)
+ Rental (REA rental & lease patterns)
+ Shareable (REA shared resources, borrowing)
+ Blocks (REA pre-paid timeblocks)
+ Work
  - see other apps from Hofstadter


### On Platforms

Certain entities publish to a platform.

+ A Market
  - A Store publishes to a Market via MarketStore
    + A Store publishes Products to a Market via MarketProduct
    + Similary a Store publishes to a Store via StoreProduct

+ A Store
  - Publishes to a Platform
  - Products are instantiated as StoreProducts


### Optional Dependencies

_If Django is being used for CMS & Display logic_

(Possibly split this into another platform)

+ Pages
+ Posts
+ Menus
+ Layout (formerly Template Blocks)
+ Displays


## Rationale

Many economic problems come up again and again, and they're solved again and again.  Economica provides a useable reference for those solved problems.  Tested and trusted.

In our Brave New World, Common Code will lead the most promising Social Enterprises into economic fruition by allowing them to concentrate on what is unique about the problem they're trying to solve.


## Outputs

+ Logic Charts
+ UML
+ Entity Relationship

### REA Commitment Patterns, Contracts & Clause Rule Engine

+ Commitment to make an Economic Event according to the Contract Clauses
  - Economic Event results
+ New Contract Clause arrangements digress if not met.






