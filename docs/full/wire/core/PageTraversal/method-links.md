# $pageTraversal->links(Page $page, $selector = '', $field = false, array $options = array()): PageArray|array|int

Source: `wire/core/PageTraversal.php`

Find other pages linking to the given one by way contextual links is textarea/html fields

## Arguments

- Page $page
- string $selector
- bool|string|Field $field
- array $options - `getIDs` (bool): Return array of page IDs rather than Page instances. (default=false) - `getCount` (bool): Return a total count (int) of found pages rather than Page instances. (default=false) - `confirm` (bool): Confirm that the links are present by looking at the actual page field data. (default=true) You can specify false for this option to make it perform faster, but with a potentially less accurate result.

## Return value

PageArray|array|int

## Throws

- WireException
