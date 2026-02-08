# $paginatedArray->getPaginationString($label = '', $usePageNum = false): string

Source: `wire/core/PaginatedArray.php`

Get a "1 to 10 of 50" type of string useful for pagination headlines.

This returns a string of `1 to 10 of 30` (items) or `1 of 10` (pages) for example.

Since 3.0.108 you can optionally replace either of the arguments with an $options o
array instead, and you can specify any of these options:

 - `label` (string): Label to use for items, same as $label argument (default='').
 - `zeroLabel` (string): Alternate label to use if there are zero items, since 3.0.127 (default='').
 - `usePageNum` (bool): Specify true to show page numbers rather than item numbers (default=false).
 - `count` (int): Use this count rather than count in this PaginatedArray (default=-1, disabled).
 - `start` (int): Use this start rather than start in this PaginatedArray (default=-1, disabled).
 - `limit` (int): Use this limit rather than limit in this PaginatedArray (default=-1, disabled).
 - `total` (int): Use this total rather than total in this PaginatedArray (default=-1, disabled).

~~~~~
// Get string like "Items 1 to 25 of 500"
echo $items->getPaginationString('Items');

// Get string like "Page 1 of 10"
echo $items->getPaginationString('Page', true);

// Get string where you specify all options
echo $items->getPaginationString(array(
  'label' => 'Items',
  'zeroLabel' => 'No items found', // 3.0.127+ only
  'usePageNum' => false,
  'count' => 10,
  'start' => 0,
  'limit' => 10,
  'total' => 100
));
~~~~~

## Arguments

- string|array $label Label to identify item type, i.e. "Items" or "Page", etc. (default=empty).
- bool|array $usePageNum Specify true to show page numbers rather than item numbers (default=false).

## Return value

string Formatted string
