# WireHttp::___send()

Source: `wire/core/WireHttp.php`

Send the given $data array to a URL using given method (i.e. POST, GET, PUT, DELETE, etc.)

This method handles the implementation for the get/post/head/etc. methods. It is preferable to use one
of those dedicated request methods rather than this one.


@param string $url URL to send to (including http:// or https://).

@param array $data Array of data to send (if not already set before).

@param string $method Method to use (either POST, GET, PUT, DELETE or others as needed).

@param array|string $options Options to modify behavior. (This argument added in 3.0.124):
- `use` (string|array): What types(s) to use, one of 'fopen', 'curl', 'socket' to allow only
   that type. Or in 3.0.192+ this may be an array of types to attempt them in order.
   Default in 3.0.192+ is [ 'curl', 'fopen', 'socket' ]. In prior versions default is 'auto'
   which attempts: fopen, curl, then socket.
- `resetRequest` (bool): Reset request headers/data after completing request? By default the request headers
   and data will remain in the WireHttp instance for re-use by the next request. If this is not your desired behavior
   then either call `$http->resetRequest()`, create a new WireHttp instance for each request, or specify this option
   as true. 3.0.253+ (default=false)
- `headers` (array): Add these headers to the request, specify as `[ 'name' => 'value' ]` array. 3.0.253+ (default=[])

@return bool|string False on failure or string of contents received on success.
