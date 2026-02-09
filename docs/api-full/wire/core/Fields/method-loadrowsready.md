# $fields->loadRowsReady(array &$rows)

Source: `wire/core/Fields.php`

Called after rows loaded from DB but before populated to this instance

## Usage

~~~~~
// basic usage
$result = $fields->loadRowsReady($rows);

// usage with all arguments
$result = $fields->loadRowsReady(array &$rows);
~~~~~

## Arguments

- `$rows` `array`
