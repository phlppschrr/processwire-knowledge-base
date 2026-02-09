# $databaseQuerySelectFulltext->escapeAgainst($str): string

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Additional escape for use in a MySQL AGAINST

When applicable, $database->escapeStr() must also be applied (before or after).

## Usage

~~~~~
// basic usage
$string = $databaseQuerySelectFulltext->escapeAgainst($str);
~~~~~

## Arguments

- `$str` `string`

## Return value

- `string`
