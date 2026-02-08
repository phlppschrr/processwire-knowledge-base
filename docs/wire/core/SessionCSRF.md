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

## getTokenName()

Get a CSRF Token name, or create one if it doesn't yet exist


@param int|string|null $id Optional unique ID for this token

@return string

## getTokenValue()

Get a CSRF Token value as stored in the session, or create one if it doesn't yet exist


@param int|string|null $id Optional unique ID for this token

@return string

## getTokenTime()

Get a CSRF Token timestamp


@param int|string|null $id Optional unique ID for this token

@return int

## getToken()

Get a CSRF Token name and value


@param int|string|null $id Optional unique ID for this token

@return array ("name" => "token name", "value" => "token value", "time" => created timestamp)

## getSingleUseToken()

Get a CSRF Token name and value that can only be used once

Note that a single call to hasValidToken($id) or validate($id) will invalidate the single use token.
So call them once and store your result if you need the result multiple times.


@param int|string $id Optional unique ID/name for this token (of omitted one is generated automatically)

@return array ("id' => "token ID", "name" => "token name", "value" => "token value", "time" => created timestamp)

## hasValidToken()

Returns true if the current POST request contains a valid CSRF token, false if not


@param int|string|null $id Optional unique ID for this token, but required if checking a single use token.

@param bool|null Reset after checking? Or omit (null) for auto (which resets if single-use token, and not otherwise).

@return bool

## validate()

Throws an exception if the token is invalid


@param int|string|null $id Optional unique ID for this token

@throws WireCSRFException if token not valid

@return bool Always returns true or throws exception

## resetToken()

Clear out token value


@param int|string|null $id Optional unique ID for this token

## resetAll()

Clear out all saved token values

## renderInput()

Render a form input[hidden] containing the token name and value, as looked for by hasValidToken()

~~~~~
<form method='post'>
  <input type='submit'>
  <?php echo $session->CSRF->renderInput(); ?>
</form>
~~~~~


@param int|string|null $id Optional unique ID for this token

@return string
