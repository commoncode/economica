db.getCollectionNames().forEach(function (collection) {
  if (collection.match(/^economica__|^users$/)) {
    db.getCollection(collection).drop();
    print('Droped: ' + collection);
  }
});
