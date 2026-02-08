# $config->requestMethod($match = ''): string

Source: `wire/core/Config.php`

Current request method

This is an alternative to `$input->requestMethod()` that’s available prior to API ready state.
Useful if you need to match request method from /site/config.php or other boot file.

## Example

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

## Usage

~~~~~
// basic usage
$string = $config->requestMethod();

// usage with all arguments
$string = $config->requestMethod($match = '');
~~~~~

## Arguments

- `$match` (optional) `string|array` Return found method if request method equals one given (blank if not), not case sensitive (default='')

## Return value

- `string` Returns one of GET, POST, HEAD, PUT, DELETE, OPTIONS, PATCH, OTHER or blank string if no match

## Since

3.0.175
