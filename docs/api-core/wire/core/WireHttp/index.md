# WireHttp

Source: `wire/core/WireHttp.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

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

Methods:
- [`__construct()`](method-__construct.md) Construct/initialize
- [`post(string $url, array|string $data = array(), array $options = array()): bool|string`](method-post.md) Send a POST request to a URL
- [`get(string $url, array|string $data = array(), array $options = array()): bool|string`](method-get.md) Send a GET request to URL
- [`head(string $url, array|string $data = array(), array $options = array()): bool|array`](method-head.md) Send to a URL using a HEAD request
- [`status(string $url, mixed $data = array(), bool $textMode = false, array $options = array()): int|string`](method-status.md) Send to a URL using a HEAD request and return the status code
- [`statusText(string $url, mixed $data = array(), array $options = array()): string`](method-statustext.md) Send to a URL using HEAD and return the status code and text like "200 OK"
- [`delete(string $url, array|string $data = array(), array $options = array()): bool|string`](method-delete.md) Send a DELETE request to a URL
- [`patch(string $url, array|string $data = array(), array $options = array()): bool|string`](method-patch.md) Send a PATCH request to a URL
- [`put(string $url, array|string $data = array(), array $options = array()): bool|string`](method-put.md) Send a PUT request to a URL
- [`send(string $url, array $data = array(), string $method = 'POST', array $options = array()): bool|string`](method-___send.md) (hookable) Send the given $data array to a URL using given method (i.e. POST, GET, PUT, DELETE, etc.)
- [`sendOptions(string $url, array $options): array`](method-sendoptions.md) Prepare options for send method(s)
- [`sendFopen(string $url, string $method = 'POST', array $options = array()): bool|string`](method-sendfopen.md) Send using fopen
- [`sendCURL(string $url, string $method = 'POST', array $options = array()): bool|string`](method-sendcurl.md) Send using CURL
- [`sendSocket(string $url, string $method = 'POST', array $options = array()): bool|string`](method-sendsocket.md) Alternate method of sending when allow_url_fopen isn't allowed
- [`download(string $fromURL, string $toFile, array $options = array()): string`](method-___download.md) (hookable) Download a file from a URL and save it locally
- [`downloadCURL(string $fromURL, resource $fp, array $options): bool`](method-downloadcurl.md) Download file using CURL
- [`downloadFopen(string $fromURL, resource $fp, array $options): bool`](method-downloadfopen.md) Download file using fopen
- [`downloadSocket(string $fromURL, resource $fp, array $options): bool`](method-downloadsocket.md) Download file using sockets
- [`openWritableFile(string $toFile, resource|false $fp = false): resource`](method-openwritablefile.md) Open a new file for writing (for download methods)
- [`setHeaders(array $headers, array $options = array()): $this`](method-setheaders.md) Set an array of request headers to send with GET/POST/etc. request
- [`setHeader(string $key, string $value): $this`](method-setheader.md) Send an individual request header to send with GET/POST/etc. request
- [`getHeaders(): array`](method-getheaders.md) Get all currently set request headers in an associative array
- [`setCookie(string $name, string|int|null $value): self`](method-setcookie.md) Set cookie(s) for http GET/POST/etc. request (currently used by curl option only)
- [`setData(array|string $data): $this`](method-setdata.md) Set an array of data, or string of raw data to send with next GET/POST/etc. request (overwriting the existing data or rawData)
- [`getResponseHeader(string $key = ''): array|string|null`](method-getresponseheader.md) Get the last HTTP response headers (normal array).
- [`getResponseHeaders(string $key = ''): array|string|null`](method-getresponseheaders.md) Get the last HTTP response headers (associative array)
- [`getResponseHeaderValues(string $key = '', bool $forceArrays = false): array|string|null`](method-getresponseheadervalues.md) Get last HTTP response headers with multi-value headers as arrays
- [`setResponseHeader(array $responseHeader)`](method-setresponseheader.md) Set the response header
- [`setResponseHeaderValues(array $responseHeader)`](method-setresponseheadervalues.md) Set response headers where they are provided as an associative array and values can be strings or arrays
- [`sendFile(string|bool $filename, array $options = array(), array $headers = array()): int`](method-___sendfile.md) (hookable) Send the contents of the given filename to the current http connection.
- [`sendFileRange(string $filename, string $rangeStr = ''): bool|int`](method-sendfilerange.md) Handle an HTTP_RANGE request for sending of partial file (called by sendFile method)
- [`sendStatusHeader(int|string $status)`](method-sendstatusheader.md) Send an HTTP status header
- [`resetResponse()`](method-resetresponse.md) Reset all response properties
- [`resetRequest()`](method-resetrequest.md) Reset all request data
- [`getError(bool $getArray = false): string|array`](method-geterror.md) Get a string of the last error message
- [`getHttpCode(bool $withText = false): int|string`](method-gethttpcode.md) Get last HTTP code
- [`getHttpCodes(): array`](method-gethttpcodes.md) Return array of all possible HTTP codes as (code => description)
- [`getSuccessCodes(): array`](method-getsuccesscodes.md) Return array of all possible HTTP success codes as (code => description)
- [`getErrorCodes(): array`](method-geterrorcodes.md) Return array of all possible HTTP error codes as (code => description)
- [`setAllowSchemes(array|string $schemes, bool $replace = false): $this`](method-setallowschemes.md) Set schemes WireHttp is allowed to access (default=[http, https])
- [`getAllowSchemes(): array`](method-getallowschemes.md) Return array of allowed schemes
- [`setValidateURLOptions(array $options = array()): array`](method-setvalidateurloptions.md) Set options array given to $sanitizer->url()
- [`getUserAgent(): string`](method-getuseragent.md) Get the current user-agent header
- [`setUserAgent(string $userAgent)`](method-setuseragent.md) Set the current user-agent header
- [`setTimeout(int|float $seconds): $this`](method-settimeout.md) Set the number of seconds till connection times out
- [`getTimeout(): float`](method-gettimeout.md) Get the number of seconds till connection times out

Constants:
- [`defaultPostContentType = 'application/x-www-form-urlencoded; charset=utf-8'`](const-defaultpostcontenttype.md)
