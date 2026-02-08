# $selectors->init($selector)

Source: `wire/core/Selectors.php`

Set the selector string or array (if not set already from the constructor)

~~~~~
$selectors = new Selectors();
$selectors->init("sale_price|retail_price>100, currency=USD|EUR");
~~~~~

## Arguments

- `$selector` `string|array`
