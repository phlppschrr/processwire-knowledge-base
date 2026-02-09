# $databaseQuery->bindOption($optionName, $optionValue = null): string|int|array

Source: `wire/core/DatabaseQuery.php`

Get or set a bind option

## Usage

~~~~~
// basic usage
$string = $databaseQuery->bindOption($optionName);

// usage with all arguments
$string = $databaseQuery->bindOption($optionName, $optionValue = null);
~~~~~

## Arguments

- `$optionName` `string|bool` One of 'prefix' or 'global', boolean true to get/set all
- `$optionValue` (optional) `null|int|string|array` Omit when getting, Specify option value to set, or array when setting all

## Return value

- `string|int|array`

## Since

3.0.157
