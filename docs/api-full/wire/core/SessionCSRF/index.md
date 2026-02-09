# SessionCSRF

Source: `wire/core/SessionCSRF.php`

Inherits: `Wire`

## Summary

ProcessWire CSRF Protection

Common methods:
- [`getTokenName()`](method-gettokenname.md)
- [`getTokenValue()`](method-gettokenvalue.md)
- [`getTokenTime()`](method-gettokentime.md)
- [`getToken()`](method-gettoken.md)
- [`getSingleUseToken()`](method-getsingleusetoken.md)

Provides an API for cross site request forgery protection.
~~~~
// output somewhere in form markup when rendering a form
echo `$session->CSRF`->`renderInput()`;
~~~~
~~~~
// when processing form (POST request), check to see if token is present
`if($session->CSRF->hasValidToken()`) {
  // form submission is valid
  // okay to process
} else {
  // form submission is NOT valid
  throw new WireException('CSRF check failed!');
}
~~~~
~~~~
// this alternative to hasValidToken() throws WireCSRFException when invalid
`$session->CSRF`->`validate()`;
~~~~

## Methods
- [`getTokenName(int|string|null $id = ''): string`](method-gettokenname.md) Get a CSRF Token name, or create one if it doesn't yet exist
- [`getTokenValue(int|string|null $id = ''): string`](method-gettokenvalue.md) Get a CSRF Token value as stored in the session, or create one if it doesn't yet exist
- [`getTokenTime(int|string|null $id = ''): int`](method-gettokentime.md) Get a CSRF Token timestamp
- [`getToken(int|string|null $id = ''): array`](method-gettoken.md) Get a CSRF Token name and value
- [`getSingleUseToken(int|string $id = ''): array`](method-getsingleusetoken.md) Get a CSRF Token name and value that can only be used once
- [`hasValidToken(int|string|null $id = '', $reset = null): bool`](method-hasvalidtoken.md) Returns true if the current POST request contains a valid CSRF token, false if not
- [`validate(int|string|null $id = ''): bool`](method-validate.md) Throws an exception if the token is invalid
- [`resetToken(int|string|null $id = '')`](method-resettoken.md) Clear out token value
- [`resetAll()`](method-resetall.md) Clear out all saved token values
- [`renderInput(int|string|null $id = ''): string`](method-renderinput.md) Render a form input[hidden] containing the token name and value, as looked for by hasValidToken()
