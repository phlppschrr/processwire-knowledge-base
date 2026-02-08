# PagesEditor::sortRebuild()

Source: `wire/core/PagesEditor.php`

Rebuild the “sort” values for all children of the given $parent page, fixing duplicates and gaps

If used on a $parent not currently sorted by by “sort” then it will update the “sort” index to be
consistent with whatever the pages are sorted by.


@param Page $parent

@return int
