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

Methods:
- [`__construct(ProcessWire $wire)`](method-__construct.md)
- [`hasCookie(bool $checkLogin = false): bool`](method-hascookie.md)
- [`hasLoginCookie(): bool`](method-haslogincookie.md)
- [`init()`](method-___init.md) (hookable)
- [`isValidSession(int $userID): bool`](method-___isvalidsession.md) (hookable)
- [`isValidFingerprint(): bool`](method-isvalidfingerprint.md)
- [`get(string|object $key, string $_key = null): mixed`](method-get.md)
- [`getVal(string $key, mixed $val = null): mixed`](method-getval.md)
- [`getAll(object|string $ns = null): array`](method-getall.md)
- [`getAllFor(string|Wire $ns): array`](method-getallfor.md)
- [`set(string|object $key, string|mixed $value, mixed $_value = null): $this`](method-set.md)
- [`getFor(string|object $ns, string $key): mixed`](method-getfor.md)
- [`getValFor(string|object $ns, string $key, mixed $val = null): mixed`](method-getvalfor.md)
- [`setFor(string|object $ns, string $key, mixed $value): $this`](method-setfor.md)
- [`remove(string|object $key, string|bool|null $_key = null): $this`](method-remove.md)
- [`removeFor(string|object $ns, string $key): $this`](method-removefor.md)
- [`removeAllFor(string|object $ns): $this`](method-removeallfor.md)
- [`getNamespace(object|string $ns): string`](method-getnamespace.md)
- [`__get(string $name): SessionCSRF|mixed|null`](method-__get.md)
- [`__set(string $key, mixed $value): $this`](method-__set.md)
- [`getIP(bool $int = false, bool|int $useClient = false): string|int`](method-getip.md)
- [`login(string|User $name, string $pass, bool $force = false): User|null`](method-___login.md) (hookable)
- [`forceLogin(string|User $user): User|null`](method-forcelogin.md)
- [`loginSuccess(User $user)`](method-___loginsuccess.md) (hookable)
- [`loginFailure(string $name, string $reason)`](method-___loginfailure.md) (hookable)
- [`allowLogin(string $name, User|null $user = null): bool`](method-___allowlogin.md) (hookable)
- [`allowLoginAttempt(string $name): bool`](method-___allowloginattempt.md) (hookable)
- [`authenticate(User $user, string $pass): bool`](method-___authenticate.md) (hookable)
- [`logout(bool $startNew = true): $this`](method-___logout.md) (hookable)
- [`setCookie(string $name, string|null|false $value, int $expires = 0, string $path = '/', string|null $domain = null, bool $secure = false, bool $httponly = false, string $samesite = 'Lax'): bool`](method-setcookie.md)
- [`removeCookies()`](method-removecookies.md)
- [`sessionCookieSameSite(string|null $value = null): string`](method-sessioncookiesamesite.md)
- [`logoutSuccess(User $user)`](method-___logoutsuccess.md) (hookable)
- [`redirect(string $url, bool|int $status = 301)`](method-___redirect.md) (hookable)
- [`location(string $url, int $status = 302)`](method-location.md)
- [`close()`](method-close.md)
- [`message(string $text, int $flags = 0): $this`](method-message.md)
- [`error(string $text, int $flags = 0): $this`](method-error.md)
- [`warning(string $text, int $flags = 0): $this`](method-warning.md)
- [`getHistory(): array`](method-gethistory.md)
- [`removeNotices()`](method-removenotices.md)
- [`CSRF(): SessionCSRF`](method-csrf.md)

Constants:
- [`fingerprintRemoteAddr`](const-fingerprintremoteaddr.md)
- [`fingerprintClientAddr`](const-fingerprintclientaddr.md)
- [`fingerprintUseragent`](const-fingerprintuseragent.md)
- [`fingerprintAccept`](const-fingerprintaccept.md)
- [`challengeSuffix`](const-challengesuffix.md)
