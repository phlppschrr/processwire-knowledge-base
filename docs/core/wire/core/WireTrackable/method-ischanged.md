# $wireTrackable->isChanged($what = ''): bool

Source: `wire/core/Interfaces.php`

Has the given property changed?

Applicable only for properties you are tracking while $trackChanges is true.

## Usage

~~~~~
// basic usage
$bool = $wireTrackable->isChanged();

// usage with all arguments
$bool = $wireTrackable->isChanged($what = '');
~~~~~

## Arguments

- `$what` (optional) `string` Name of property, or if left blank, check if any properties have changed.

## Return value

- `bool`
