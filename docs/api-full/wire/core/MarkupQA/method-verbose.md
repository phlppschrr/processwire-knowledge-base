# $markupQA->verbose($set = null): bool

Source: `wire/core/MarkupQA.php`

Get or set verbose state

Whether or not to set/track verbose information to page, i.e.
`$page->_markupQA = array('field_name' => array(counts))`

When getting, if $page or $field have not been populated, verbose is always false.

## Usage

~~~~~
// basic usage
$bool = $markupQA->verbose();

// usage with all arguments
$bool = $markupQA->verbose($set = null);
~~~~~

## Arguments

- `$set` (optional) `bool|null` Omit this argument to get or specify bool to set

## Return value

- `bool`
