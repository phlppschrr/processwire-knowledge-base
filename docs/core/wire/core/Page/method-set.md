# $page->set($key, $value): Page|WireData

Source: `wire/core/Page.php`

Set the value of a page property

You can set properties to a page using either `$page->set('property', $value);` or `$page->property = $value;`.

## Example

~~~~~
// Set the page title using set() method
$page->set('title', 'About Us');

// Set the page title directly (equivalent to the above)
$page->title = 'About Us';
~~~~~

## Usage

~~~~~
// basic usage
$page = $page->set($key, $value);
~~~~~

## Arguments

- `$key` `string` Name of property to set
- `$value` `mixed` Value to set

## Return value

- `Page|WireData` Reference to this Page

## Exceptions

- `WireException`

## See Also

- __set
