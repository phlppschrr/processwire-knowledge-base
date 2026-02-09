# $databaseQuerySelectFulltext->escapeLike($str): string

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Escape string for use in a MySQL LIKE

When applicable, $database->escapeStr() should be applied before this.

## Usage

~~~~~
// basic usage
$string = $databaseQuerySelectFulltext->escapeLike($str);
~~~~~

## Arguments

- `$str` `string`

## Return value

- `string`
