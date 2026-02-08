# PagesType

Source: `wire/core/PagesType.php`

ProcessWire PagesType

Pages Type
Provides an interface to the Pages class but specific to a given page class/type, with predefined parent and template.
This class is primarily used by the core as an alternative to `$pages`, providing an API for other Page types like
`User`, `Role`, `Permission`, and `Language`. The `$users`, `$roles`, `$permissions` and `$languages` API variables
are all instances of `PagesType`. This class is typically not instantiated on its own and instead acts as a base class
which is extended.


ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@method Page add($name)

@method Page new(array $options = []) 3.0.249

@method bool save(Page $page)

@method bool delete(Page $page, $recursive = false)

@method saveReady(Page $page)

@method saved(Page $page, array $changes = array(), $values = array())

@method added(Page $page)

@method deleteReady(Page $page)

@method deleted(Page $page)

## __construct()

Construct this PagesType manager for the given parent and template

@param ProcessWire $wire

@param Template|int|string|array $templates Template object or array of template objects, names or IDs

@param int|Page|array $parents Parent ID or array of parent IDs (may also be Page or array of Page objects)

## ___new()

Create new instance of this page type

@param array $options

@return Page

@since 3.0.249

## addTemplates()

Add one or more templates that this PagesType represents


@param array|int|string $templates Single or array of Template objects, IDs, or names

## addParents()

Add one or more of parents that this PagesType represents


@param array|int|string|Page $parents Single or array of Page objects, IDs, or paths

## selectorString()

Convert the given selector string to qualify for the proper page type

@param string $selectorString

@return string

## loaded()

Each loaded page is passed through this function for additional checks if needed

@param Page $page

## getLoadOptions()

Get options that will be passed to Pages::getById()

@param array $loadOptions Optionally specify options to merge with and override defaults

@return array

## find()

Given a Selector string, return the Page objects that match in a PageArray.

@param string $selectorString

@param array $options Options to modify default behavior:
 - `findOne` (bool): apply optimizations for finding a single page and include pages with 'hidden' status

@return PageArray

@see Pages::find()

## findIDs()

Given a Selector string, return the page IDs that match

@param string $selectorString

@param array $options

@return array

@since 3.0.128

@see Pages::findIDs()

## get()

Get the first match of your selector string

@param string|int $selectorString

@return Page|NullPage|null

## ___save()

Save a page object and its fields to database.

- This is the same as calling $page->save()
- If the page is new, it will be inserted. If existing, it will be updated.
- If you want to just save a particular field in a Page, use `$page->save($fieldName)` instead.

Hook note:
If you want to hook this method, please hook the `saveReady`, `saved`, or one of
the `Pages::save*` methods instead, as hooking this method will not hook relevant pages
saved directly through $pages->save().

@param Page $page

@return bool True on success

@throws WireException

## ___delete()

Permanently delete a page and its fields.

Unlike `$pages->trash()`, pages deleted here are not restorable.

If you attempt to delete a page with children, and don’t specifically set the `$recursive` argument to `true`, then
this method will throw an exception. If a recursive delete fails for any reason, an exception will be thrown.

Hook note:
If you want to hook this method, please hook the `deleteReady`, `deleted`, or `Pages::delete` method
instead, as hooking this method will not hook relevant pages deleted directly through $pages->delete().

@param Page $page

@param bool $recursive If set to true, then this will attempt to delete all children too.

@return bool

@throws WireException

## ___add()

Adds a new page with the given $name and returns it

- If the page has any other fields, they will not be populated, only the name will.
- Returns a `NullPage` on error, such as when a page of this type already exists with the same name/parent.

Hook note:
If you want to hook this method, please hook the `addReady`, `Pages::add`, or `Pages::addReady` method
instead, as hooking this method will not hook relevant pages added directly through $pages->add().

@param string $name Name to use for the new page

@return Page|NullPage

## getTemplate()

Get the template used by this type (or first template if there are multiple)


@return Template

## getTemplates()

Get the templates (plural) used by this type


@return array|Template[] Array of Template objects indexed by template ID.

## getParentID()

Get the parent page ID used by this type (or first parent ID if there are multiple)


@return int

## getParentIDs()

Get the parent page IDs used by this type


@return array Array of parent page IDs (integers)

## getParent()

Get the parent Page object (or first parent Page object if there are multiple)


@return Page|NullPage

## getParents()

Get the parent Page objects in a PageArray


@return PageArray

## setPageClass()

Set the PHP class name to use for Page objects of this type


@param string $class

## getPageClass()

Get the PHP class name used by Page objects of this type

If returned class is not namespaced then `ProcessWire` namespace can be assumed.


@return string

## count()

Return the number of pages in this type matching the given selector string

@param string $selectorString Optional, if omitted then returns count of all pages of this type

@param array $options Options to modify default behavior (see $pages->count method for details)

@return int

@see Pages::count()

## getJoinFieldNames()

Get names of fields that should always be autojoined

@return array

## ___saveReady()

******************************************************************************************
HOOKS

## ___saveReady()

Hook called just before a page of this type is saved


@param Page $page The page about to be saved

@return array Optional extra data to add to pages save query.

@since 3.0.128

## ___saved()

Hook called after a page of this type is successfully saved


@param Page $page The page that was saved

@param array $changes Array of field names that changed

@param array $values Array of values that changed, if values were being recorded, see Wire::getChanges(true) for details.

@since 3.0.128

## ___added()

Hook called when a new page of this type has been added


@param Page $page

@since 3.0.128

## ___deleteReady()

Hook called when a page is about to be deleted, but before data has been touched


@param Page $page

@since 3.0.128

## ___deleted()

Hook called when a page and its data have been deleted


@param Page $page

@since 3.0.128
