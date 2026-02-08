# $pagesEditor->savePageStatus($pageID, $status, $recursive = false, $remove = false): int

Source: `wire/core/PagesEditor.php`

Add or remove a Page status and commit to DB, optionally recursive with the children, grandchildren, and so on.

While this can be performed with other methods, this is here just to make it fast for internal/non-api use.
See the trash and restore methods for an example.

This action does not update the Page modified date. If given a Page or PageArray, also note that it does not update
the status properties of those instantiated Page objects, it only updates the DB value.

Note: Please use addStatus() or removeStatus() instead, unless you need to perform a recursive add/remove status.

## Arguments

- `$pageID` `int|array|Page|PageArray` Page ID, Page, array of page IDs, or PageArray
- `$status` `int` Status per flags in Page::status* constants. Status will be OR'd with existing status, unless $remove is used.
- `$recursive` (optional) `bool` Should the status descend into the page's children, and grandchildren, etc? (default=false)
- `$remove` (optional) `bool|int` Should the status be removed rather than added? Use integer 2 to overwrite (default=false)

## Return value

int Number of pages updated
