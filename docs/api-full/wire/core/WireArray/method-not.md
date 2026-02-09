# $wireArray->not($selector): $this

Source: `wire/core/WireArray.php`

Filter this WireArray to only include items that DO NOT match the selector (destructive)

## Example

~~~~~
// returns all pages that don't have a 'nonav' variable set to a positive value.
$pages->not("nonav");
~~~~~

## Usage

~~~~~
// basic usage
$result = $wireArray->not($selector);
~~~~~

## Arguments

- `$selector` `string|array|Selectors`

## Return value

- `$this` reference to current instance.

## See Also

- filterData
