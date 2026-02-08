# WireHttp

Source: `wire/core/WireHttp.php`

ProcessWire HTTP tools

Provides capability for sending POST/GET requests to URLs

WireHttp enables you to send HTTP requests to URLs, download files, and more.
$http
$http = new WireHttp();
~~~~~
// Get the contents of a URL
$response = $http->get("http://domain.com/path/");
if($response !== false) {
  echo "Successful response: " . $sanitizer->entities($response);
} else {
  echo "HTTP request failed: " . $http->getError();
}
~~~~~

Thanks to @horst for his assistance with several methods in this class.

ProcessWire 3.x, Copyright 2025 by Ryan Cramer
https://processwire.com

## other

@method bool|string send($url, $data = array(), $method = 'POST', array $options = array())

@method int sendFile($filename, array $options = array(), array $headers = array())

@method string download($fromURL, $toFile, array $options = array())

## defaultPostContentType

Default content-type header for POST requests

## __construct()

Construct/initialize

## post()

Send a POST request to a URL

~~~~~
$http = new WireHttp();
$response = $http->post("http://domain.com/path/", [
  'foo' => 'bar',
]);
if($response !== false) {
  echo "Successful response: " . $sanitizer->entities($response);
} else {
  echo "HTTP request failed: " . $http->getError();
}
~~~~~


@param string $url URL to post to (including http:// or https://)

@param array|string $data Associative array of data to send (if not already set before),
  or raw string of data to send, such as JSON.

@param array $options Optional options to modify default behavior, see the send() method for details.

@return bool|string False on failure or string of contents received on success.

@see WireHttp::send(), WireHttp::get(), WireHttp::head()

## get()

Send a GET request to URL

~~~~~
$http = new WireHttp();
$response = $http->get("http://domain.com/path/", [
  'foo' => 'bar',
]);
if($response !== false) {
  echo "Successful response: " . $sanitizer->entities($response);
} else {
  echo "HTTP request failed: " . $http->getError();
}
~~~~~


@param string $url URL to send request to (including http:// or https://)

@param array|string $data Array of data to send (if not already set before)
  or raw string of data to send, such as JSON.

@param array $options Optional options to modify default behavior, see the send() method for details.

@return bool|string False on failure or string of contents received on success.

@see WireHttp::send(), WireHttp::post(), WireHttp::head(), WireHttp::getJSON()

## head()

Send to a URL using a HEAD request


@param string $url URL to request (including http:// or https://)

@param array|string $data Array of data to send (if not already set before)
  or raw string data to send, such as JSON.

@param array $options Optional options to modify default behavior, see the send() method for details.

@return bool|array False on failure or Array with ResponseHeaders on success.

@see WireHttp::send(), WireHttp::post(), WireHttp::get()

## status()

Send to a URL using a HEAD request and return the status code


@param string $url URL to request (including http:// or https://)

@param mixed $data Array of data to send (if not already set before) or raw data

@param bool $textMode When true function will return a string rather than integer, see the statusText() method.

@param array $options Optional options to modify default behavior, see the send() method for details.

@return int|string Integer or string of status code (200, 404, etc.)

@see WireHttp::send(), WireHttp::statusText()

## statusText()

Send to a URL using HEAD and return the status code and text like "200 OK"


@param string $url URL to request (including http:// or https://)

@param mixed $data Array of data to send (if not already set before) or raw data

@param array $options Optional options to modify default behavior, see the send() method for details.

@return string String of status code + text on success.
	Example: "200 OK', "302 Found", "404 Not Found"

@see WireHttp::send(), WireHttp::status()

## delete()

Send a DELETE request to a URL

“The HTTP DELETE request method deletes the specified resource.”
[More about DELETE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE)


@param string $url URL to send to (including http:// or https://)

@param array|string $data Optional associative array of data to send (if not already set before),
  or raw data to send (such as JSON string)

@param array $options Optional options to modify default behavior, see the send() method for details.

@return bool|string False on failure or string of contents received on success.

@since 3.0.222

## patch()

Send a PATCH request to a URL

“The HTTP PATCH request method applies partial modifications to a resource.”
[More about PATCH](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH)


@param string $url URL to PATCH to (including http:// or https://)

@param array|string $data Associative array of data to send (if not already set before),
  or raw data to send (such as JSON string)

@param array $options Optional options to modify default behavior, see the send() method for details.

@return bool|string False on failure or string of contents received on success.

@since 3.0.222

## put()

Send a PUT request to a URL

“The HTTP PUT request method creates a new resource or replaces a representation of the
target resource with the request payload.”
[More about PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT)


@param string $url URL to PUT to (including http:// or https://)

@param array|string $data Associative array of data to send (if not already set before),
  or raw data to send (such as JSON string)

@param array $options Optional options to modify default behavior, see the send() method for details.

@return bool|string False on failure or string of contents received on success.

@since 3.0.222

## ___send()

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

## sendOptions()

Prepare options for send method(s)

@param string $url

@param array $options

@return array

## sendFopen()

Send using fopen

@param string $url

@param string $method

@param array $options Options specific to fopen should be specified in [ 'fopen' => [ ... ] ]

@return bool|string

## sendCURL()

Send using CURL

@param string $url

@param string $method

@param array $options

@return bool|string

## sendSocket()

Alternate method of sending when allow_url_fopen isn't allowed

@param string $url

@param string $method

@param array $options Optional settings:
	- timeout: number of seconds to timeout

@return bool|string

## ___download()

Download a file from a URL and save it locally

First it will attempt to use CURL. If that fails, it will try `fopen()`,
unless you specify the `use` option in `$options`.


@param string $fromURL URL of file you want to download.

@param string $toFile Filename you want to save it to (including full path).

@param array $options Optional options array for PHP's stream_context_create(), plus these optional options:
	- `use` or `useMethod` (string): Specify "curl", "fopen" or "socket" to force a specific method (default=auto-detect).
	- `timeout` (float): Number of seconds till timeout or omit to use previously set timeout setting or default.
 - `fopen_bufferSize' (int): Buffer size (bytes) or 0 to disable buffer, used only by fopen method (default=1048576) 3.0.222+

@return string Filename that was downloaded (including full path).

@throws WireException All error conditions throw exceptions.

@todo update the use option to support array like the send() method

## downloadCURL()

Download file using CURL

@param string $fromURL

@param resource $fp Open file pointer

@param array $options

@return bool True if successful false if not

## downloadFopen()

Download file using fopen

@param string $fromURL

@param resource $fp Open file pointer

@param array $options

@return bool True if successful false if not

## downloadSocket()

Download file using sockets

@param string $fromURL

@param resource $fp Open file pointer

@param array $options

@return bool True if successful false if not

## openWritableFile()

Open a new file for writing (for download methods)

@param string $toFile

@param resource|false $fp

@return resource

@throws WireException

@since 3.0.222

## setHeaders()

Set an array of request headers to send with GET/POST/etc. request

Merges with existing headers unless you specify true for the $reset option (since 3.0.131).
If you specify null for any header value, it removes the header (since 3.0.131).


@param array $headers Associative array of headers to set

@param array $options Options to modify default behavior (since 3.0.131):
 - `reset` (bool): Reset/clear all existing headers first? (default=false)
 - `replacements` (array): Associative array of [ find => replace ] values to replace in header values (default=[])

@return $this

## setHeader()

Send an individual request header to send with GET/POST/etc. request


@param string $key Header name

@param string $value Header value to set (or specify null to remove header, since 3.0.131)

@return $this

## getHeaders()

Get all currently set request headers in an associative array

Note: To get response headers from a previously sent request, use `WireHttp::getResponseHeaders()` instead.


@return array

@since 3.0.131

## setCookie()

Set cookie(s) for http GET/POST/etc. request (currently used by curl option only)

~~~~~
$http->setCookie('PHPSESSID', 'f3943z12339jz93j39iafai3f9393g');
$http->post('http://domain.com', [ 'foo' => 'bar' ], [ 'use' => 'curl' ]);
~~~~~


@param string $name Name of cookie to set

@param string|int|null $value Specify value to set or null to remove

@return self

@since 3.0.199

## setData()

Set an array of data, or string of raw data to send with next GET/POST/etc. request (overwriting the existing data or rawData)


@param array|string $data Associative array of data or string of raw data

@return $this

## getResponseHeader()

Get the last HTTP response headers (normal array).


Useful to examine for errors if your request returned false
However, the `WireHttp::getResponseHeaders()` (plural) method may be better
and this one is kept primarily for backwards compatibility.

@param string $key Optional header name you want to get

@return array|string|null

## getResponseHeaders()

Get the last HTTP response headers (associative array)

All headers are translated to `[key => value]` properties in the array.
The keys are always lowercase and the values are always strings. If you
need multi-value headers, use the `WireHttp::getResponseHeaderValues()` method
instead, which returns multi-value headers as arrays.

This method always returns an associative array of strings, unless you specify the
`$key` option in which case it will return a string, or NULL if the header is not present.


@param string $key Optional header name you want to get (if you only need one)

@return array|string|null

@see WireHttp::getResponseHeaderValues()

## getResponseHeaderValues()

Get last HTTP response headers with multi-value headers as arrays

Use this method when you want to retrieve headers that can potentially contain multiple-values.
Note that any code that iterates these values should be able to handle them being either a string or
an array.

This method always returns an associative array of strings and arrays, unless you specify the
`$key` option in which case it can return an array, string, or NULL if the header is not present.


@param string $key Optional header name you want to get (if you only need a specific header)

@param bool $forceArrays If even single-value headers should be arrays, specify true (default=false).

@return array|string|null

## setResponseHeader()

Set the response header

@param array

## setResponseHeaderValues()

Set response headers where they are provided as an associative array and values can be strings or arrays

@param array $responseHeader headers in an associative array

## ___sendFile()

Send the contents of the given filename to the current http connection.

This function utilizes the `$config->fileContentTypes` to match file extension
to content type headers and force-download state.

This function throws a `WireException` if the file can't be sent for some reason.


@param string|bool $filename Filename to send (or boolean false if sending $options[data] rather than file)

@param array $options Options that you may pass in:
  - `exit` (bool): Halt program execution after file send (default=true).
  - `partial` (bool): Allow use of partial downloads via HTTP_RANGE requests? Since 3.0.131 (default=true)
  - `forceDownload` (bool|null): Whether file should force download (default=null, i.e. let content-type header decide).
  - `downloadFilename` (string): Filename you want the download to show on user's computer, or omit to use existing.
  - `headers` (array): The $headers argument to this method can also be provided as an option right here, since 3.0.131 (default=[])
  - `data` (string): String of data to send rather than contents of file, applicable only if $filename argument is false, Since 3.0.132.

@param array $headers Headers that are sent. These are the defaults:
  - `pragma`: public
  - `expires`: 0
  - `cache-control`: must-revalidate, post-check=0, pre-check=0
  - `content-type`: {content-type} (replaced with actual content type)
  - `content-transfer-encoding`: binary
  - `content-length`: {filesize} (replaced with actual filesize)
  - To remove a header completely, make its value NULL and it won't be sent.

@return int Returns value only if `exit` option is false (value is quantity of bytes sent)

@throws WireException

## sendFileRange()

Handle an HTTP_RANGE request for sending of partial file (called by sendFile method)

@param string $filename

@param string $rangeStr Range string (i.e. `bytes=0-1234`) or omit to pull from `$_SERVER['HTTP_RANGE']`

@return bool|int Returns bytes sent, null if error in request or range, or false if request should be handled by sendFile() instead

## sendStatusHeader()

Send an HTTP status header

@param int|string $status Status code (i.e. '200') or code and text (i.e. '200 OK')

@since 3.0.166

## resetResponse()

Reset all response properties

This resets any response data stored in this WireHttp instance, including
response headers, response HTTP code and text, or any response errors.


@since 3.0.253

## resetRequest()

Reset all request data

This resets any previously set request data, raw request data, and request HTTP headers.


@since 3.0.253

## getError()

Get a string of the last error message

@param bool $getArray Specify true to receive an array of error messages, or omit for a string.

@return string|array

## getHttpCode()

Get last HTTP code


@param bool $withText Specify true to include the HTTP code text label with the code

@return int|string

## getHttpCodes()

Return array of all possible HTTP codes as (code => description)


@return array

## getSuccessCodes()

Return array of all possible HTTP success codes as (code => description)


@return array

## getErrorCodes()

Return array of all possible HTTP error codes as (code => description)


@return array

## setAllowSchemes()

Set schemes WireHttp is allowed to access (default=[http, https])


@param array|string $schemes Array of schemes or space-separated string of schemes

@param bool $replace Specify true to replace any existing schemes already allowed (default=false)

@return $this

## getAllowSchemes()

Return array of allowed schemes


@return array

## setValidateURLOptions()

Set options array given to $sanitizer->url()

It should not be necessary to call this unless you are dealing with an unusual URL that is causing
errors with the default options in WireHttp. Note that the “allowSchemes” option is set separately
with the setAllowSchemes() method in this class.

To return current validate URL options, omit the $options argument.


@param array $options Options to set, see the $sanitizer->url() method for details on options.

@return array Always returns current options

## getUserAgent()

Get the current user-agent header

To set the user agent header, use `$http->setHeader('user-agent', '...');`
or in 3.0.183+ there is also `$http->setUserAgent('...');`


@return string

## setUserAgent()

Set the current user-agent header


@param string $userAgent

@since 3.0.183

## setTimeout()

Set the number of seconds till connection times out

Note that the default timeout for http requests is 4.5 seconds


@param int|float $seconds

@return $this

## getTimeout()

Get the number of seconds till connection times out

Used by send(), get(), post(), getJSON(), but not by download() methods.


@return float
