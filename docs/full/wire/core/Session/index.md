# Session

Source: `wire/core/Session.php`

Inherits: `Wire`
Implements: `IteratorAggregate`


Groups:
Group: [other](group-other.md)

ProcessWire Session

Start a session with login/logout capability

Maintains sessions in ProcessWire, authentication, persistent variables, notices and redirects.

This should be used instead of the $_SESSION superglobal, though the $_SESSION superglobal can still be
used, but it's in a different namespace than this. A value set in $_SESSION won't appear in $session
and likewise a value set in $session won't appear in $_SESSION.  It's also good to use this class
over the $_SESSION superglobal just in case we ever need to replace PHP's session handling in the future.


@see https://processwire.com/api/ref/session/ Session documentation



## Expected $Config Variables Include:
string $config->sessionName Name of session on http
string $config->sessionNameSecure Name of session on https
int $config->sessionExpireSeconds Number of seconds of inactivity before session expires
bool $config->sessionChallenge True if a separate challenge cookie should be used for validating sessions
bool $config->sessionFingerprint True if a fingerprint should be kept of the user's IP & user agent to validate sessions
bool $config->sessionCookieSecure Use secure cookies or session? (default=true)

@todo enable login/forceLogin to recognize non-HTTP use of login, when no session needs to be maintained

@todo add a default $config->apiUser to be used when non-HTTP/bootstrap usage

Methods:
- [`__construct(ProcessWire $wire)`](method-__construct.md) Start the session and set the current User if a session is active
- [`hasCookie(bool $checkLogin = false): bool`](method-hascookie.md) Are session cookie(s) present?
- [`hasLoginCookie(): bool`](method-haslogincookie.md) Is a session login cookie present?
- [`init()`](method-___init.md) (hookable) Start the session
- [`isValidSession(int $userID): bool`](method-___isvalidsession.md) (hookable) Checks if the session is valid based on a challenge cookie and fingerprint
- [`isValidFingerprint(): bool`](method-isvalidfingerprint.md) Returns whether or not the current session fingerprint is valid
- [`get(string|object $key, string $_key = null): mixed`](method-get.md) Get a session variable
- [`getVal(string $key, mixed $val = null): mixed`](method-getval.md) Get a session variable or return $val argument if session value not present
- [`getAll(object|string $ns = null): array`](method-getall.md) Get all session variables in an associative array
- [`getAllFor(string|Wire $ns): array`](method-getallfor.md) Get all session variables for given namespace and return associative array
- [`set(string|object $key, string|mixed $value, mixed $_value = null): $this`](method-set.md) Set a session variable
- [`getFor(string|object $ns, string $key): mixed`](method-getfor.md) Get a session variable within a given namespace
- [`getValFor(string|object $ns, string $key, mixed $val = null): mixed`](method-getvalfor.md) Get a session variable or return $val argument if session value not present
- [`setFor(string|object $ns, string $key, mixed $value): $this`](method-setfor.md) Set a session variable within a given namespace
- [`remove(string|object $key, string|bool|null $_key = null): $this`](method-remove.md) Unset a session variable
- [`removeFor(string|object $ns, string $key): $this`](method-removefor.md) Unset a session variable within a namespace
- [`removeAllFor(string|object $ns): $this`](method-removeallfor.md) Remove all session variables in given namespace
- [`getNamespace(object|string $ns): string`](method-getnamespace.md) Given a namespace object or string, return the namespace string
- [`__get(string $name): SessionCSRF|mixed|null`](method-__get.md) Provide non-namespaced $session->variable get access
- [`__set(string $key, mixed $value): $this`](method-__set.md) Provide non-namespaced $session->variable = variable set access
- [`getIP(bool $int = false, bool|int $useClient = false): string|int`](method-getip.md) Get the IP address of the current user
- [`login(string|User $name, string $pass, bool $force = false): User|null`](method-___login.md) (hookable) Login a user with the given name and password
- [`forceLogin(string|User $user): User|null`](method-forcelogin.md) Login a user without requiring a password
- [`loginSuccess(User $user)`](method-___loginsuccess.md) (hookable) Login success method for hooks
- [`loginFailure(string $name, string $reason)`](method-___loginfailure.md) (hookable) Login failure method for hooks
- [`allowLogin(string $name, User|null $user = null): bool`](method-___allowlogin.md) (hookable) Allow the user $name to login? Provided for use by hooks.
- [`allowLoginAttempt(string $name): bool`](method-___allowloginattempt.md) (hookable) Allow login attempt for given name at all?
- [`authenticate(User $user, string $pass): bool`](method-___authenticate.md) (hookable) Return true or false whether the user authenticated with the supplied password
- [`logout(bool $startNew = true): $this`](method-___logout.md) (hookable) Logout the current user, and clear all session variables
- [`setCookie(string $name, string|null|false $value, int $expires = 0, string $path = '/', string|null $domain = null, bool $secure = false, bool $httponly = false, string $samesite = 'Lax'): bool`](method-setcookie.md) Add a SetCookie response header
- [`removeCookies()`](method-removecookies.md) Remove all cookies used by the session
- [`sessionCookieSameSite(string|null $value = null): string`](method-sessioncookiesamesite.md) Get 'SameSite' value for session cookie
- [`logoutSuccess(User $user)`](method-___logoutsuccess.md) (hookable) Logout success method for hooks
- [`redirect(string $url, bool|int $status = 301)`](method-___redirect.md) (hookable) Redirect this session to another URL.
- [`location(string $url, int $status = 302)`](method-location.md) Perform a temporary redirect
- [`close()`](method-close.md) Manually close the session, before program execution is done
- [`message(string $text, int $flags = 0): $this`](method-message.md) Queue a message to appear on the next pageview
- [`error(string $text, int $flags = 0): $this`](method-error.md) Queue an error to appear on the next pageview
- [`warning(string $text, int $flags = 0): $this`](method-warning.md) Queue a warning to appear the next pageview
- [`getHistory(): array`](method-gethistory.md) Get the session history (if enabled)
- [`removeNotices()`](method-removenotices.md) Remove queued notices
- [`CSRF(): SessionCSRF`](method-csrf.md) Return an instance of ProcessWire’s CSRF object, which provides an API for cross site request forgery protection.

Constants:
- [`fingerprintRemoteAddr`](const-fingerprintremoteaddr.md)
- [`fingerprintClientAddr`](const-fingerprintclientaddr.md)
- [`fingerprintUseragent`](const-fingerprintuseragent.md)
- [`fingerprintAccept`](const-fingerprintaccept.md)
- [`challengeSuffix`](const-challengesuffix.md)
