# PagesType

Source: `wire/core/PagesType.php`

Inherits: `Wire`
Implements: `IteratorAggregate`, `Countable`

## Summary

ProcessWire PagesType

Common methods:
- [`new()`](method-___new.md)
- [`addTemplates()`](method-addtemplates.md)
- [`addParents()`](method-addparents.md)
- [`selectorString()`](method-selectorstring.md)
- [`loaded()`](method-loaded.md)

Groups:
Group: [other](group-other.md)

Pages Type
Provides an interface to the Pages class but specific to a given page class/type, with predefined parent and template.
This class is primarily used by the core as an alternative to `$pages`, providing an API for other Page types like
`User`, `Role`, `Permission`, and `Language`. The `$users`, `$roles`, `$permissions` and `$languages` API variables
are all instances of `PagesType`. This class is typically not instantiated on its own and instead acts as a base class
which is extended.

## Methods
- [`__construct(ProcessWire $wire, Template|int|string|array $templates = array(), int|Page|array $parents = array())`](method-__construct.md) Construct this PagesType manager for the given parent and template
- [`new(array $options = []): Page`](method-___new.md) (hookable) Create new instance of this page type
- [`addTemplates(array|int|string $templates)`](method-addtemplates.md) Add one or more templates that this PagesType represents
- [`addParents(array|int|string|Page $parents)`](method-addparents.md) Add one or more of parents that this PagesType represents
- [`selectorString(string $selectorString): string`](method-selectorstring.md) Convert the given selector string to qualify for the proper page type
- [`loaded(Page $page)`](method-loaded.md) Each loaded page is passed through this function for additional checks if needed
- [`getLoadOptions(array $loadOptions = array()): array`](method-getloadoptions.md) Get options that will be passed to Pages::getById()
- [`find(string $selectorString, array $options = array()): PageArray`](method-find.md) Given a Selector string, return the Page objects that match in a PageArray.
- [`findIDs(string $selectorString, array $options = array()): array`](method-findids.md) Given a Selector string, return the page IDs that match
- [`get(string|int $selectorString): Page|NullPage|null`](method-get.md) Get the first match of your selector string
- [`save(Page $page): bool`](method-___save.md) (hookable) Save a page object and its fields to database.
- [`delete(Page $page, bool $recursive = false): bool`](method-___delete.md) (hookable) Permanently delete a page and its fields.
- [`add(string $name): Page|NullPage`](method-___add.md) (hookable) Adds a new page with the given $name and returns it
- [`getTemplate(): Template`](method-gettemplate.md) Get the template used by this type (or first template if there are multiple)
- [`getTemplates(): array|Template[]`](method-gettemplates.md) Get the templates (plural) used by this type
- [`getParentID(): int`](method-getparentid.md) Get the parent page ID used by this type (or first parent ID if there are multiple)
- [`getParentIDs(): array`](method-getparentids.md) Get the parent page IDs used by this type
- [`getParent(): Page|NullPage`](method-getparent.md) Get the parent Page object (or first parent Page object if there are multiple)
- [`getParents(): PageArray`](method-getparents.md) Get the parent Page objects in a PageArray
- [`setPageClass(string $class)`](method-setpageclass.md) Set the PHP class name to use for Page objects of this type
- [`getPageClass(): string`](method-getpageclass.md) Get the PHP class name used by Page objects of this type
- [`count(string $selectorString = '', array $options = array()): int`](method-count.md) Return the number of pages in this type matching the given selector string
- [`getJoinFieldNames(): array`](method-getjoinfieldnames.md) Get names of fields that should always be autojoined
- [`saveReady(Page $page): array`](method-___saveready.md) (hookable) Hook called just before a page of this type is saved
- [`saved(Page $page, array $changes = array(), array $values = array())`](method-___saved.md) (hookable) Hook called after a page of this type is successfully saved
- [`added(Page $page)`](method-___added.md) (hookable) Hook called when a new page of this type has been added
- [`deleteReady(Page $page)`](method-___deleteready.md) (hookable) Hook called when a page is about to be deleted, but before data has been touched
- [`deleted(Page $page)`](method-___deleted.md) (hookable) Hook called when a page and its data have been deleted
