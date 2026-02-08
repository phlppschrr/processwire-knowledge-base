# $session->CSRF(): SessionCSRF

Source: `wire/core/Session.php`

Return an instance of ProcessWire’s CSRF object, which provides an API for cross site request forgery protection.

~~~~
// output somewhere in <form> markup when rendering a form
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

## Return value

SessionCSRF

## See also

- [SessionCSRF::renderInput()](../SessionCSRF/method-renderinput.md)
- [SessionCSRF::validate()](../SessionCSRF/method-validate.md)
- [SessionCSRF::hasValidToken()](../SessionCSRF/method-hasvalidtoken.md)
