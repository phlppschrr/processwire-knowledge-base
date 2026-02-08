# Session

Source: `wire/core/Session.php`

ProcessWire Session

Start a session with login/logout capability

Maintains sessions in ProcessWire, authentication, persistent variables, notices and redirects.

This should be used instead of the $_SESSION superglobal, though the $_SESSION superglobal can still be
used, but it's in a different namespace than this. A value set in $_SESSION won't appear in $session
and likewise a value set in $session won't appear in $_SESSION.  It's also good to use this class
over the $_SESSION superglobal just in case we ever need to replace PHP's session handling in the future.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

@see https://processwire.com/api/ref/session/ Session documentation



Expected $config variables include:
===================================
string $config->sessionName Name of session on http
string $config->sessionNameSecure Name of session on https
int $config->sessionExpireSeconds Number of seconds of inactivity before session expires
bool $config->sessionChallenge True if a separate challenge cookie should be used for validating sessions
bool $config->sessionFingerprint True if a fingerprint should be kept of the user's IP & user agent to validate sessions
bool $config->sessionCookieSecure Use secure cookies or session? (default=true)

@todo enable login/forceLogin to recognize non-HTTP use of login, when no session needs to be maintained

@todo add a default $config->apiUser to be used when non-HTTP/bootstrap usage

## other

@method User login() login($name, $pass, $force = false) Login the user identified by $name and authenticated by $pass. Returns the user object on successful login or null on failure.

@method Session logout() logout() Logout the current user, and clear all session variables.

@method void redirect() redirect($url, $http301 = true) Redirect this session to the specified URL.

@method void init() Initialize session (called automatically by constructor)

@method bool authenticate(User $user, $pass)

@method bool isValidSession($userID)

@method bool allowLoginAttempt($name)

@method bool allowLogin($name, User $user = null)

@method void loginSuccess(User $user)

@method void loginFailure($name, $reason)

@method void logoutSuccess(User $user)

@property SessionCSRF $CSRF

## fingerprintRemoteAddr

Fingerprint bitmask: Use remote addr (recommended)

## fingerprintClientAddr

Fingerprint bitmask: Use client provided addr

## fingerprintUseragent

Fingerprint bitmask: Use user agent (recommended)

## fingerprintAccept

Fingerprint bitmask: Use “accept” content-types header

@since 3.0.159

## challengeSuffix

Suffix applied to challenge cookies

@since 3.0.141

## __construct()

Start the session and set the current User if a session is active

Assumes that you have already performed all session-specific ini_set() and session_name() calls

@param ProcessWire $wire

@throws WireException

## hasCookie()

Are session cookie(s) present?


@param bool $checkLogin Specify true to check instead for challenge cookie (which indicates login may be active).

@return bool Returns true if session cookie present, false if not.

## hasLoginCookie()

Is a session login cookie present?

This only indicates the user was likely logged in at some point, and may not indicate an active login.
This method is more self describing version of `$session->hasCookie(true);`


@return bool

@since 3.0.175

## ___init()

Start the session

Provided here in any case anything wants to hook in before session_start()
is called to provide an alternate save handler.

## ___isValidSession()

Checks if the session is valid based on a challenge cookie and fingerprint

These items may be disabled at the config level, in which case this method always returns true


@param int $userID

@return bool

## isValidFingerprint()

Returns whether or not the current session fingerprint is valid

@return bool

## get()

Get a session variable

- This method returns the value of the requested session variable, or NULL if it's not present.
- You can optionally use a namespace with this method, to avoid collisions with other session variables.
  But if using namespaces we recommended using the dedicated getFor() and setFor() methods instead.
- You can also get or set non-namespaced session values directly (see examples).

~~~~~
// Set value "Bob" to session variable named "firstName"
$session->set('firstName', 'Bob');

// You can retrieve the firstName now, or any later request
$firstName = $session->get('firstName');

// outputs: Hello Bob
echo "Hello $firstName";
~~~~~
~~~~~
// Setting and getting a session value directly
$session->firstName = 'Bob';
$firstName = $session->firstName;
~~~~~


@param string|object $key Name of session variable to retrieve (or object if using namespaces)

@param string $_key Name of session variable to get if first argument is namespace, omit otherwise.

@return mixed Returns value of seession variable, or NULL if not found.

## getVal()

Get a session variable or return $val argument if session value not present

This is the same as get() except that it lets you specify a fallback return value in the method call.
For a namespace version use `Session::getValFor()` instead.


@param string $key Name of session variable to retrieve.

@param mixed $val Fallback value to return if session does not have it.

@return mixed Returns value of seession variable, or NULL if not found.

@since 3.0.133

## getAll()

Get all session variables in an associative array


@param object|string $ns Optional namespace

@return array

## getAllFor()

Get all session variables for given namespace and return associative array


@param string|Wire $ns

@return array

@since 3.0.141 Method added for consistency, but any version can do this with $session->getFor($ns, '');

## set()

Set a session variable

- You can optionally use a namespace with this method, to avoid collisions with other session variables.
  But if using namespaces we recommended using the dedicated getFor() and setFor() methods instead.
- You can also get or set non-namespaced session values directly (see examples).

~~~~~
// Set value "Bob" to session variable named "firstName"
$session->set('firstName', 'Bob');

// You can retrieve the firstName now, or any later request
$firstName = $session->get('firstName');

// outputs: Hello Bob
echo "Hello $firstName";
~~~~~
~~~~~
// Setting and getting a session value directly
$session->firstName = 'Bob';
$firstName = $session->firstName;
~~~~~


@param string|object $key Name of session variable to set (or object for namespace)

@param string|mixed $value Value to set (or name of variable, if first argument is namespace)

@param mixed $_value Value to set if first argument is namespace. Omit otherwise.

@return $this

## getFor()

Get a session variable within a given namespace

~~~~~
// Retrieve namespaced session value
$firstName = $session->getFor($this, 'firstName');
~~~~~


@param string|object $ns Namespace string or object

@param string $key Specify variable name to retrieve, or blank string to return all variables in the namespace.

@return mixed

## getValFor()

Get a session variable or return $val argument if session value not present

This is the same as get() except that it lets you specify a fallback return value in the method call.
For a namespace version use `Session::getValFor()` instead.


@param string|object $ns Namespace string or object

@param string $key Specify variable name to retrieve

@param mixed $val Fallback value if session does not have one

@return mixed

@since 3.0.133

## setFor()

Set a session variable within a given namespace

To remove a namespace, use `$session->remove($namespace)`.

~~~~~
// Set a session value for a namespace
$session->setFor($this, 'firstName', 'Bob');
~~~~~


@param string|object $ns Namespace string or object.

@param string $key Name of session variable you want to set.

@param mixed $value Value you want to set, or specify null to unset.

@return $this

## remove()

Unset a session variable

~~~~~
// Unset a session var
$session->remove('firstName');

// Unset a session var in a namespace
$session->remove($this, 'firstName');

// Unset all session vars in a namespace
$session->remove($this, true);
~~~~~


@param string|object $key Name of session variable you want to remove (or namespace string/object)

@param string|bool|null $_key Omit this argument unless first argument is a namespace. Otherwise specify one of:
 - If first argument is namespace and you want to remove a property from the namespace, provide key here.
	- If first argument is namespace and you want to remove all properties from the namespace, provide boolean TRUE.

@return $this

## removeFor()

Unset a session variable within a namespace


@param string|object $ns Namespace

@param string $key Provide name of variable to remove, or boolean true to remove all in namespace.

@return $this

## removeAllFor()

Remove all session variables in given namespace


@param string|object $ns

@return $this

## getNamespace()

Given a namespace object or string, return the namespace string


@param object|string $ns

@return string

@throws WireException if given invalid namespace type

## __get()

Provide non-namespaced $session->variable get access

@param string $name

@return SessionCSRF|mixed|null

## __set()

Provide non-namespaced $session->variable = variable set access

@param string $key

@param mixed $value

@return $this

## getIP()

Get the IP address of the current user

~~~~~
$ip = $session->getIP();
echo $ip; // outputs 111.222.333.444
~~~~~


@param bool $int Return as a long integer? (default=false)
 - IPv6 addresses cannot be represented as an integer, so please note that using this int option makes it return a CRC32
   integer when using IPv6 addresses (3.0.184+).

@param bool|int $useClient Give preference to client headers for IP? HTTP_CLIENT_IP and HTTP_X_FORWARDED_FOR (default=false)
	- Specify integer 2 to include potential multiple CSV separated IPs (when provided by client).

@return string|int Returns string by default, or integer if $int argument indicates to.

## ___login()

Login a user with the given name and password

Also sets them to the current user.

~~~~~
$u = $session->login('bob', 'laj3939$a');
if($u) {
  echo "Welcome Bob";
} else {
  echo "Sorry Bob";
}
~~~~~


@param string|User $name May be user name or User object.

@param string $pass Raw, non-hashed password.

@param bool $force Specify boolean true to login user without requiring a password ($pass argument can be blank, or anything).
	You can also use the `$session->forceLogin($user)` method to force a login without a password.

@return User|null Return the $user if the login was successful or null if not.

@throws WireException

## forceLogin()

Login a user without requiring a password

~~~~~
// login bob without knowing his password
$u = $session->forceLogin('bob');
~~~~~


@param string|User $user Username or User object

@return User|null Returns User object on success, or null on failure

## ___loginSuccess()

Login success method for hooks


@param User $user

## ___loginFailure()

Login failure method for hooks


@param string $name Attempted login name

@param string $reason Reason for login failure

## ___allowLogin()

Allow the user $name to login? Provided for use by hooks.


@param string $name User login name

@param User|null $user User object

@return bool True if allowed to login, false if not (hooks may modify this)

## ___allowLoginAttempt()

Allow login attempt for given name at all?

This method does nothing and is purely for hooks to modify return value.


@param string $name

@return bool

## ___authenticate()

Return true or false whether the user authenticated with the supplied password


@param User $user User attempting to login

@param string $pass Password they are attempting to login with

@return bool

## ___logout()

Logout the current user, and clear all session variables

~~~~~
// logout user when "?logout=1" in URL query string
if($input->get('logout')) {
  $session->logout();
	 // good to redirect somewhere else after a login or logout
  $session->redirect('/');
}
~~~~~


@param bool $startNew Start a new session after logout? (default=true)

@return $this

@throws WireException if session is disabled

## setCookie()

Add a SetCookie response header

@param string $name

@param string|null|false $value

@param int $expires

@param string $path

@param string|null $domain

@param bool $secure

@param bool $httponly

@param string $samesite One of 'Strict', 'Lax', 'None'

@return bool

@since 3.0.178

## removeCookies()

Remove all cookies used by the session

## sessionCookieSameSite()

Get 'SameSite' value for session cookie

@param string|null $value

@return string

@since 3.0.178

## ___logoutSuccess()

Logout success method for hooks


@param User $user User that logged in

## ___redirect()

Redirect this session to another URL.

Execution halts within this function after redirect has been issued.

~~~~~
// redirect to homepage
$session->redirect('/');
~~~~~


@param string $url URL to redirect to

@param bool|int $status One of the following (or omit for 301):
- `true` (bool): Permanent redirect (same as 301).
- `false` (bool): Temporary redirect (same as 302).
- `301` (int): Permanent redirect using GET. (3.0.166+)
- `302` (int): “Found”, Temporary redirect using GET. (3.0.166+)
- `303` (int): “See other”, Temporary redirect using GET. (3.0.166+)
- `307` (int): Temporary redirect using current request method such as POST (repeat that request). (3.0.166+)

@see Session::location()

## location()

Perform a temporary redirect

This is an alias of `$session->redirect($url, false);` that sends only the
location header, which translates to a 302 redirect.


@param string $url

@param int $status One of the following HTTP status codes, or omit for 302 (added 3.0.192):
- `302` (int): “Found”, Temporary redirect using GET. (default)
- `303` (int): “See other”, Temporary redirect using GET.
- `307` (int): Temporary redirect using current request method such as POST (repeat that request).

@since 3.0.166

@see Session::redirect()

## close()

Manually close the session, before program execution is done

A user session is limited to rendering one page at a time, unless the session is closed
early. Use this when you have a request that may take awhile to render (like a request
rendering a sitemap, etc.) and you don't need to get/save session data. By closing the session
before starting a render, you can release the session to be available for the user to view
other pages while the slower page render continues.

## message()

Queue a message to appear on the next pageview


@param string $text Message to queue

@param int $flags Optional flags, See Notice::flags

@return $this

## error()

Queue an error to appear on the next pageview


@param string $text Error to queue

@param int $flags See Notice::flags

@return $this

## warning()

Queue a warning to appear the next pageview


@param string $text Warning to queue

@param int $flags See Notice::flags

@return $this

## getHistory()

Get the session history (if enabled)

Applicable only if `$config->sessionHistory > 0`.

~~~~~
$history = $session->getHistory();
print_r($history);
// outputs the following:
array(
  0  => array(
		'url' => 'http://domain.com/path/to/page/', // URL
		'page' => 1234, // page ID
		'time' => 234993498, // unix timestamp
  ),
  1 => array(
     // ...
  ),
  2 => array(
     // ...
  ),
  ...
);
~~~~~


@return array Array of arrays containing history entries.

## removeNotices()

Remove queued notices

Call this after displaying queued message, error or warning notices.
This prevents them from re-appearing on the next request.

## CSRF()

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


@return SessionCSRF

@see SessionCSRF::renderInput(), SessionCSRF::validate(), SessionCSRF::hasValidToken()
