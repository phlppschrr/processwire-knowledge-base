# $selectors->__construct($selector = null)

Source: `wire/core/Selectors.php`

Given a selector string, extract it into one or more corresponding Selector objects, iterable in this object.

## Usage

~~~~~
// basic usage
$result = $selectors->__construct();

// usage with all arguments
$result = $selectors->__construct($selector = null);
~~~~~

## Arguments

- `$selector` (optional) `string|null|array` Please omit this argument and use a separate init($selector) call instead.
