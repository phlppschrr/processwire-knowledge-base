# $wireHttp->send($url, $data = array(), $method = 'POST', array $options = array()): bool|string

Source: `wire/core/WireHttp.php`

Send the given $data array to a URL using given method (i.e. POST, GET, PUT, DELETE, etc.)

This method handles the implementation for the get/post/head/etc. methods. It is preferable to use one
of those dedicated request methods rather than this one.

## Usage

~~~~~
// basic usage
$bool = $wireHttp->send($url);

// usage with all arguments
$bool = $wireHttp->send($url, $data = array(), $method = 'POST', array $options = array());
~~~~~

## Hookable

- Hookable method name: `send`
- Implementation: `___send`
- Hook with: `$wireHttp->send()`

## Hooking Before

~~~~~
$this->addHookBefore('WireHttp::send', function(HookEvent $event) {
  $wireHttp = $event->object;

  // Get arguments
  $url = $event->arguments(0);
  $data = $event->arguments(1);
  $method = $event->arguments(2);
  $options = $event->arguments(3);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $url);
  $event->arguments(1, $data);
  $event->arguments(2, $method);
  $event->arguments(3, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireHttp::send', function(HookEvent $event) {
  $wireHttp = $event->object;

  // Get arguments
  $url = $event->arguments(0);
  $data = $event->arguments(1);
  $method = $event->arguments(2);
  $options = $event->arguments(3);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$url` `string` URL to send to (including http:// or https://).
- `$data` (optional) `array` Array of data to send (if not already set before).
- `$method` (optional) `string` Method to use (either POST, GET, PUT, DELETE or others as needed).
- `$options` (optional) `array|string` Options to modify behavior. (This argument added in 3.0.124): - `use` (string|array): What types(s) to use, one of 'fopen', 'curl', 'socket' to allow only that type. Or in 3.0.192+ this may be an array of types to attempt them in order. Default in 3.0.192+ is [ 'curl', 'fopen', 'socket' ]. In prior versions default is 'auto' which attempts: fopen, curl, then socket. - `resetRequest` (bool): Reset request headers/data after completing request? By default the request headers and data will remain in the WireHttp instance for re-use by the next request. If this is not your desired behavior then either call `$http->resetRequest()`, create a new WireHttp instance for each request, or specify this option as true. 3.0.253+ (default=false) - `headers` (array): Add these headers to the request, specify as `[ 'name' => 'value' ]` array. 3.0.253+ (default=[])

## Return value

- `bool|string` False on failure or string of contents received on success.
