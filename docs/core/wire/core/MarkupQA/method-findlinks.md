# MarkupQA::findLinks()

Source: `wire/core/MarkupQA.php`

Find pages linking to another

@param Page|null $page Page to find links to, or omit to use page specified in constructor

@param array $fieldNames Field names to look in or omit to use field specified in constructor

@param string $selector Optional selector to use as a filter

@param array $options Additional options
 - `getIDs` (bool): Return array of page IDs rather than Page instances. (default=false)
 - `getCount` (bool): Return a total count (int) of found pages rather than Page instances. (default=false)
 - `confirm` (bool): Confirm that the links are present by looking at the actual page field data. (default=true)
    You can specify false for this option to make it perform faster, but with a potentially less accurate result.

@return PageArray|array|int
