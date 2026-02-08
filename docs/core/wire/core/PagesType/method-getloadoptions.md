# $pagesType->getLoadOptions(array $loadOptions = array()): array

Source: `wire/core/PagesType.php`

Get options that will be passed to Pages::getById()

## Usage

~~~~~
// basic usage
$array = $pagesType->getLoadOptions();

// usage with all arguments
$array = $pagesType->getLoadOptions(array $loadOptions = array());
~~~~~

## Arguments

- `$loadOptions` (optional) `array` Optionally specify options to merge with and override defaults

## Return value

- `array`
