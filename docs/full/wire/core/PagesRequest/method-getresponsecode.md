# $pagesRequest->getResponseCode(): int

Source: `wire/core/PagesRequest.php`

Get response http code for this request

Returns integer, one of:

- 0: unknown/request not yet analyzed
- 200: successful request
- 300: maybe redirect (needs decision)
- 301: permanent redirect
- 302: temporary redirect
- 307: temporary redirect and redo using same method
- 308: permanent redirect and redo using same method
- 400: bad request/page path error
- 401: unauthorized/login required
- 403: forbidden/authenticated user lacks access
- 404: page not found
- 405: method not allowed
- 414: request path too long or segment too long

## Return value

int
