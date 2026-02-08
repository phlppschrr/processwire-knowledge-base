# PagesEditor::savePageStatus()

Source: `wire/core/PagesEditor.php`

Add or remove a Page status and commit to DB, optionally recursive with the children, grandchildren, and so on.

While this can be performed with other methods, this is here just to make it fast for internal/non-api use.
See the trash and restore methods for an example.

This action does not update the Page modified date. If given a Page or PageArray, also note that it does not update
the status properties of those instantiated Page objects, it only updates the DB value.

Note: Please use addStatus() or removeStatus() instead, unless you need to perform a recursive add/remove status.


@param int|array|Page|PageArray $pageID Page ID, Page, array of page IDs, or PageArray

@param int $status Status per flags in Page::status* constants. Status will be OR'd with existing status, unless $remove is used.

@param bool $recursive Should the status descend into the page's children, and grandchildren, etc? (default=false)

@param bool|int $remove Should the status be removed rather than added? Use integer 2 to overwrite (default=false)

@return int Number of pages updated
