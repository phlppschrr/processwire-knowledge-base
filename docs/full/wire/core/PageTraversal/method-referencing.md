# PageTraversal::referencing()

Source: `wire/core/PageTraversal.php`

Return pages that this page is referencing by way of Page reference fields

@param Page $page

@param bool|Field|string|int $field Limit results to requested field, or specify boolean true to return array indexed by field names.

@param bool $getCount Specify true to return count(s) rather than pages.

@return PageArray|int|array
