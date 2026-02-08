# $config->requestMethod($match = ''): string

Source: `wire/core/Config.php`

Current request method

This is an alternative to `$input->requestMethod()` that’s available prior to API ready state.
Useful if you need to match request method from /site/config.php or other boot file.

~~~~~
if($config->requestMethod('post')) {
  // request method is POST
}
if($config->requestMethod() === 'GET') {
  // request method is GET
}
$method = $config->requestMethod([ 'POST', 'get' ]);
if($method) {
  // method is either 'POST' or 'GET'
}
~~~~~

## Arguments

- string|array $match Return found method if request method equals one given (blank if not), not case sensitive (default='')

## Return value

string Returns one of GET, POST, HEAD, PUT, DELETE, OPTIONS, PATCH, OTHER or blank string if no match

## Meta

- @since 3.0.175
