# PagesAccess::___updatePage()

Source: `wire/core/PagesAccess.php`

Save to pages_access table to indicate what template each page is getting its access from

This should be called when a page has been saved and its parent or template has changed.
Or, when a new page is added.

If there is no entry in this table, then the page is getting its access from its existing template.

This is used by PageFinder to determine what pages to include in a find() operation based on user access.

@param Page $page
