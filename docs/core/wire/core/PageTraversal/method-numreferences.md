# PageTraversal::numReferences()

Source: `wire/core/PageTraversal.php`

Return number of ANY pages that are following (referencing) the given one by way of Page references

@param Page $page

@param string $selector Filter count by this selector

@param string|Field|bool $field Limit count to given Field or specify boolean true to return array of counts.

@return int|array Returns count, or array of counts (if $field==true)
