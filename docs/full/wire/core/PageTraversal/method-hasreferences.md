# PageTraversal::hasReferences()

Source: `wire/core/PageTraversal.php`

Return number of VISIBLE pages that are following (referencing) the given one by way of Page references

Note that this excludes hidden, unpublished and otherwise non-accessible pages (access control).
If you do not want to exclude these, use the numFollowers() function instead, OR specify "include=all" for
the $selector argument.

@param Page $page

@param string $selector Filter count by this selector

@param string|Field|bool $field Limit count to given Field or specify boolean true to return array of counts.

@return int|array Returns count, or array of counts (if $field==true)
