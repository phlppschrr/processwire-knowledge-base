# $pagesRequest->getResponseCodeName(): string

Source: `wire/core/PagesRequest.php`

Get response type name for this request

Returns string, one of:

- unknown: request not yet analyzed (0)
- ok: successful request (200)
- fileOk: successful file request (200)
- fileNotFound: requested file not found (404)
- maybeRedirect: needs decision about whether to redirect (300)
- permRedirect: permanent redirect (301)
- tempRedirect: temporary redirect (302)
- tempRedo: temporary redirect and redo using same method (307)
- permRedo: permanent redirect and redo using same method (308)
- badRequest: bad request/page path error (400)
- unauthorized: login required (401)
- forbidden: authenticated user lacks access (403)
- pageNotFound: page not found (404)
- methodNotAllowed: request method is not allowed by template (405)
- pathTooLong: path too long or segment too long (414)

## Usage

~~~~~
// basic usage
$string = $pagesRequest->getResponseCodeName();
~~~~~

## Return value

- `string`
