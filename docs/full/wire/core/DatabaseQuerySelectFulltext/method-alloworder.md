# $databaseQuerySelectFulltext->allowOrder($allow = null): bool|null

Source: `wire/core/DatabaseQuerySelectFulltext.php`

Get or set whether or not 'ORDER BY' statements are allowed to be added

## Usage

~~~~~
// basic usage
$bool = $databaseQuerySelectFulltext->allowOrder();

// usage with all arguments
$bool = $databaseQuerySelectFulltext->allowOrder($allow = null);
~~~~~

## Arguments

- `$allow` (optional) `null|bool` Specify bool to set or omit to get

## Return value

- `bool|null` Returns bool when known or null when not yet known

## Since

3.0.162
