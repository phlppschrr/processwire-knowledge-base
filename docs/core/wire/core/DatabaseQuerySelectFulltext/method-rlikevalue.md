# $databaseQuerySelectFulltext->rlikeValue($value, array $options = array()): string

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Prepare a word or phrase for use in an RLIKE statement

## Usage

~~~~~
// basic usage
$string = $databaseQuerySelectFulltext->rlikeValue($value);

// usage with all arguments
$string = $databaseQuerySelectFulltext->rlikeValue($value, array $options = array());
~~~~~

## Arguments

- `$value` `string`
- `$options` (optional) `array`

## Return value

- `string`
