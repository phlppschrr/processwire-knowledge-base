# PagesType

Source: `wire/core/PagesType.php`

Inherits: `Wire`
Implements: `IteratorAggregate`, `Countable`


Groups:
Group: [other](group-other.md)

ProcessWire PagesType

Pages Type
Provides an interface to the Pages class but specific to a given page class/type, with predefined parent and template.
This class is primarily used by the core as an alternative to `$pages`, providing an API for other Page types like
`User`, `Role`, `Permission`, and `Language`. The `$users`, `$roles`, `$permissions` and `$languages` API variables
are all instances of `PagesType`. This class is typically not instantiated on its own and instead acts as a base class
which is extended.

Methods:
Method: [__construct()](method-__construct.md)
Method: [new()](method-___new.md) (hookable)
Method: [addTemplates()](method-addtemplates.md)
Method: [addParents()](method-addparents.md)
Method: [selectorString()](method-selectorstring.md)
Method: [loaded()](method-loaded.md)
Method: [getLoadOptions()](method-getloadoptions.md)
Method: [find()](method-find.md)
Method: [findIDs()](method-findids.md)
Method: [get()](method-get.md)
Method: [save()](method-___save.md) (hookable)
Method: [delete()](method-___delete.md) (hookable)
Method: [add()](method-___add.md) (hookable)
Method: [getTemplate()](method-gettemplate.md)
Method: [getTemplates()](method-gettemplates.md)
Method: [getParentID()](method-getparentid.md)
Method: [getParentIDs()](method-getparentids.md)
Method: [getParent()](method-getparent.md)
Method: [getParents()](method-getparents.md)
Method: [setPageClass()](method-setpageclass.md)
Method: [getPageClass()](method-getpageclass.md)
Method: [count()](method-count.md)
Method: [getJoinFieldNames()](method-getjoinfieldnames.md)
Method: [saveReady()](method-___saveready.md) (hookable)
Method: [saveReady()](method-___saveready.md) (hookable)
Method: [saved()](method-___saved.md) (hookable)
Method: [added()](method-___added.md) (hookable)
Method: [deleteReady()](method-___deleteready.md) (hookable)
Method: [deleted()](method-___deleted.md) (hookable)
