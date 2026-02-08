# SessionCSRF

Source: `wire/core/SessionCSRF.php`

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


ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

Methods:
Method: [getTokenName()](method-gettokenname.md)
Method: [getTokenValue()](method-gettokenvalue.md)
Method: [getTokenTime()](method-gettokentime.md)
Method: [getToken()](method-gettoken.md)
Method: [getSingleUseToken()](method-getsingleusetoken.md)
Method: [hasValidToken()](method-hasvalidtoken.md)
Method: [validate()](method-validate.md)
Method: [resetToken()](method-resettoken.md)
Method: [resetAll()](method-resetall.md)
Method: [renderInput()](method-renderinput.md)
