# $wire->isChanged($what = ''): bool

Source: `wire/core/Wire.php`

Does the object have changes, or has the given property changed?

Applicable only when object has change tracking enabled.

## Example

~~~~~
// Check if page has changed
if($page->isChanged()) {
  // Page has changes
}

// Check if the page title field has changed
if($page->isChanged('title')) {
  // The title has changed
}
~~~~~

## Usage

~~~~~
// basic usage
$bool = $wire->isChanged();

// usage with all arguments
$bool = $wire->isChanged($what = '');
~~~~~

## Arguments

- `$what` (optional) `string` Name of property, or if left blank, checks if any properties have changed.

## Return value

- `bool` True if property has changed, false if not.
