# FunctionsWireAPI::wirePage()

Source: `wire/core/FunctionsWireAPI.php`

Access the $page API variable as a function

~~~~
$page = page(); // Simply get $page API var
$body = page()->body; // Get body field value
$body = page('body'); // Same as above
$headline = page('headline|title'); // Get headline or title
page('headline', 'Setting headline value'); // Set headline
~~~~

@param string $key Optional property to get or set

@param null $value Optional value to set

@return Page|mixed
