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
- [`__construct()`](method-__construct.md)
- [`post(string $url, array|string $data = array(), array $options = array()): bool|string`](method-post.md)
- [`get(string $url, array|string $data = array(), array $options = array()): bool|string`](method-get.md)
- [`head(string $url, array|string $data = array(), array $options = array()): bool|array`](method-head.md)
- [`status(string $url, mixed $data = array(), bool $textMode = false, array $options = array()): int|string`](method-status.md)
- [`statusText(string $url, mixed $data = array(), array $options = array()): string`](method-statustext.md)
- [`delete(string $url, array|string $data = array(), array $options = array()): bool|string`](method-delete.md)
- [`patch(string $url, array|string $data = array(), array $options = array()): bool|string`](method-patch.md)
- [`put(string $url, array|string $data = array(), array $options = array()): bool|string`](method-put.md)
- [`send(string $url, array $data = array(), string $method = 'POST', array $options = array()): bool|string`](method-___send.md) (hookable)
- [`sendOptions(string $url, array $options): array`](method-sendoptions.md)
- [`sendFopen(string $url, string $method = 'POST', array $options = array()): bool|string`](method-sendfopen.md)
- [`sendCURL(string $url, string $method = 'POST', array $options = array()): bool|string`](method-sendcurl.md)
- [`sendSocket(string $url, string $method = 'POST', array $options = array()): bool|string`](method-sendsocket.md)
- [`download(string $fromURL, string $toFile, array $options = array()): string`](method-___download.md) (hookable)
- [`downloadCURL(string $fromURL, resource $fp, array $options): bool`](method-downloadcurl.md)
- [`downloadFopen(string $fromURL, resource $fp, array $options): bool`](method-downloadfopen.md)
- [`downloadSocket(string $fromURL, resource $fp, array $options): bool`](method-downloadsocket.md)
- [`openWritableFile(string $toFile, resource|false $fp = false): resource`](method-openwritablefile.md)
- [`setHeaders(array $headers, array $options = array()): $this`](method-setheaders.md)
- [`setHeader(string $key, string $value): $this`](method-setheader.md)
- [`getHeaders(): array`](method-getheaders.md)
- [`setCookie(string $name, string|int|null $value): self`](method-setcookie.md)
- [`setData(array|string $data): $this`](method-setdata.md)
- [`getResponseHeader(string $key = ''): array|string|null`](method-getresponseheader.md)
- [`getResponseHeaders(string $key = ''): array|string|null`](method-getresponseheaders.md)
- [`getResponseHeaderValues(string $key = '', bool $forceArrays = false): array|string|null`](method-getresponseheadervalues.md)
- [`setResponseHeader(array $responseHeader)`](method-setresponseheader.md)
- [`setResponseHeaderValues(array $responseHeader)`](method-setresponseheadervalues.md)
- [`sendFile(string|bool $filename, array $options = array(), array $headers = array()): int`](method-___sendfile.md) (hookable)
- [`sendFileRange(string $filename, string $rangeStr = ''): bool|int`](method-sendfilerange.md)
- [`sendStatusHeader(int|string $status)`](method-sendstatusheader.md)
- [`resetResponse()`](method-resetresponse.md)
- [`resetRequest()`](method-resetrequest.md)
- [`getError(bool $getArray = false): string|array`](method-geterror.md)
- [`getHttpCode(bool $withText = false): int|string`](method-gethttpcode.md)
- [`getHttpCodes(): array`](method-gethttpcodes.md)
- [`getSuccessCodes(): array`](method-getsuccesscodes.md)
- [`getErrorCodes(): array`](method-geterrorcodes.md)
- [`setAllowSchemes(array|string $schemes, bool $replace = false): $this`](method-setallowschemes.md)
- [`getAllowSchemes(): array`](method-getallowschemes.md)
- [`setValidateURLOptions(array $options = array()): array`](method-setvalidateurloptions.md)
- [`getUserAgent(): string`](method-getuseragent.md)
- [`setUserAgent(string $userAgent)`](method-setuseragent.md)
- [`setTimeout(int|float $seconds): $this`](method-settimeout.md)
- [`getTimeout(): float`](method-gettimeout.md)

Constants:
- [`defaultPostContentType`](const-defaultpostcontenttype.md)
