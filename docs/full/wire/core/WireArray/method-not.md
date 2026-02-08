# $wireArray->not($selector): $this

Source: `wire/core/WireArray.php`

Filter this WireArray to only include items that DO NOT match the selector (destructive)

~~~~~
// returns all pages that don't have a 'nonav' variable set to a positive value.
$pages->not("nonav");
~~~~~

## Arguments

- `$selector` `string|array|Selectors`

## Return value

$this reference to current instance.

## See also

- filterData
