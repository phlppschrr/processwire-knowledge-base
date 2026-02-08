# $fields->getAllNames($indexType = ''): array

Source: `wire/core/Fields.php`

Get all field names

## Usage

~~~~~
// basic usage
$array = $fields->getAllNames();

// usage with all arguments
$array = $fields->getAllNames($indexType = '');
~~~~~

## Arguments

- `$indexType` (optional) `string` One of 'name', 'id' or blank string for no index (default='')

## Return value

- `array`

## Since

3.0.194
