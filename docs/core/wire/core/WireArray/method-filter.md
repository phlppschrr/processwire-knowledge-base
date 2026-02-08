# $wireArray->filter($selector): $this

Source: `wire/core/WireArray.php`

Filter this WireArray to only include items that match the given selector (destructive)

~~~~~
// Filter $items to contain only those with "featured" property having value 1
$items->filter("featured=1");
~~~~~

## Arguments

- `$selector` `string|array|Selectors` Selector string or array to use as the filter.

## Return value

$this reference to current instance.

## See also

- filterData
