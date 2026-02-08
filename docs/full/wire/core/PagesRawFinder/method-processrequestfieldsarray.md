# $pagesRawFinder->processRequestFieldsArray(array $values, $prefix = '')

Source: `wire/core/PagesRaw.php`

Process given array of values to populate $this->requestFields and $this->renameFields

## Usage

~~~~~
// basic usage
$result = $pagesRawFinder->processRequestFieldsArray($values);

// usage with all arguments
$result = $pagesRawFinder->processRequestFieldsArray(array $values, $prefix = '');
~~~~~

## Arguments

- `$values` `array`
- `$prefix` (optional) `string` Prefix for recursive use

## Since

3.0.194
