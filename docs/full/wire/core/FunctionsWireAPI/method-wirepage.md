# $functionsWireAPI->wirePage($key = '', $value = null): Page|mixed

Source: `wire/core/FunctionsWireAPI.php`

Access the $page API variable as a function

~~~~
$page = page(); // Simply get $page API var
$body = page()->body; // Get body field value
$body = page('body'); // Same as above
$headline = page('headline|title'); // Get headline or title
page('headline', 'Setting headline value'); // Set headline
~~~~

## Arguments

- string $key Optional property to get or set
- null $value Optional value to set

## Return value

Page|mixed
