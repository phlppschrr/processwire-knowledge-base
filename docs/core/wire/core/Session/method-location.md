# $session->location($url, $status = 302)

Source: `wire/core/Session.php`

Perform a temporary redirect

This is an alias of `$session->redirect($url, false);` that sends only the
location header, which translates to a 302 redirect.

## Arguments

- string $url
- int $status One of the following HTTP status codes, or omit for 302 (added 3.0.192): - `302` (int): “Found”, Temporary redirect using GET. (default) - `303` (int): “See other”, Temporary redirect using GET. - `307` (int): Temporary redirect using current request method such as POST (repeat that request).

## See also

- [Session::redirect()](method-___redirect.md)

## Meta

- @since 3.0.166
