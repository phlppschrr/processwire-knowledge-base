# $markupQA->findLinks(?Page $page = null, $fieldNames = array(), $selector = '', array $options = array()): PageArray|array|int

Source: `wire/core/MarkupQA.php`

Find pages linking to another

## Arguments

- Page|null $page Page to find links to, or omit to use page specified in constructor
- array $fieldNames Field names to look in or omit to use field specified in constructor
- string $selector Optional selector to use as a filter
- array $options Additional options - `getIDs` (bool): Return array of page IDs rather than Page instances. (default=false) - `getCount` (bool): Return a total count (int) of found pages rather than Page instances. (default=false) - `confirm` (bool): Confirm that the links are present by looking at the actual page field data. (default=true) You can specify false for this option to make it perform faster, but with a potentially less accurate result.

## Return value

PageArray|array|int
