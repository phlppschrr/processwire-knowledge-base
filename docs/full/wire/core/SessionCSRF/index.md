# SessionCSRF

Source: `wire/core/SessionCSRF.php`

Inherits: `Wire`

ProcessWire CSRF Protection

Provides an API for cross site request forgery protection.
~~~~
// output somewhere in form markup when rendering a form
echo $session->CSRF->renderInput();
~~~~
~~~~
// when processing form (POST request), check to see if token is present
if($session->CSRF->hasValidToken()) {
  // form submission is valid
  // okay to process
} else {
  // form submission is NOT valid
  throw new WireException('CSRF check failed!');
}
~~~~
~~~~
// this alternative to hasValidToken() throws WireCSRFException when invalid
$session->CSRF->validate();
~~~~

Methods:
- [`getTokenName(int|string|null $id = ''): string`](method-gettokenname.md)
- [`getTokenValue(int|string|null $id = ''): string`](method-gettokenvalue.md)
- [`getTokenTime(int|string|null $id = ''): int`](method-gettokentime.md)
- [`getToken(int|string|null $id = ''): array`](method-gettoken.md)
- [`getSingleUseToken(int|string $id = ''): array`](method-getsingleusetoken.md)
- [`hasValidToken(int|string|null $id = '', $reset = null): bool`](method-hasvalidtoken.md)
- [`validate(int|string|null $id = ''): bool`](method-validate.md)
- [`resetToken(int|string|null $id = '')`](method-resettoken.md)
- [`resetAll()`](method-resetall.md)
- [`renderInput(int|string|null $id = ''): string`](method-renderinput.md)
