# PageTraversal::links()

Source: `wire/core/PageTraversal.php`

Find other pages linking to the given one by way contextual links is textarea/html fields

@param Page $page

@param string $selector

@param bool|string|Field $field

@param array $options
 - `getIDs` (bool): Return array of page IDs rather than Page instances. (default=false)
 - `getCount` (bool): Return a total count (int) of found pages rather than Page instances. (default=false)
 - `confirm` (bool): Confirm that the links are present by looking at the actual page field data. (default=true)
    You can specify false for this option to make it perform faster, but with a potentially less accurate result.

@return PageArray|array|int

@throws WireException
