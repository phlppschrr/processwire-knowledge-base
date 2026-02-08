# PagesAccess

Source: `wire/core/PagesAccess.php`

ProcessWire Pages Access

Pages Access
Maintains the pages_access table which serves as a way to line up pages to the templates that maintain their access roles.
This class serves as a way for PageFinder to determine if a user has access to a page
before actually loading it.

The pages_access table contains just two columns:

	- `pages_id` (int): Any given page
	- `templates_id` (int): The template that sets this pages access

Pages using templates that already define their access (determined by $template->useRoles)
are omitted from the pages_access table, as they aren't necessary.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@method void updatePage(Page $page)

@method void updateTemplate(Template $template)

## __construct()

Construct a PagesAccess instance, optionally specifying a Page or Template

If Page or Template specified, then the updateTemplate or updatePage method is assumed.

@param Page|Template

## rebuild()

Rebuild the entire pages_access table (or a part of it) starting from the given parent_id

@param int $parent_id

@param int $accessTemplateID

@param bool $doDeletions

## ___updateTemplate()

Update the pages_access table for the given Template

To be called when a `$template->useRoles` property has changed.

@param Template $template

## ___updatePage()

Save to pages_access table to indicate what template each page is getting its access from

This should be called when a page has been saved and its parent or template has changed.
Or, when a new page is added.

If there is no entry in this table, then the page is getting its access from its existing template.

This is used by PageFinder to determine what pages to include in a find() operation based on user access.

@param Page $page

## deletePage()

Delete a page from the pages_access table

@param Page $page

## getTemplates()

Returns an array of templates that DON'T define access

## getAccessTemplates()

Returns an array of templates that DO define access
