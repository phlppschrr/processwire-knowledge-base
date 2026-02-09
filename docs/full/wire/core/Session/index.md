# Session

Source: `wire/core/Session.php`

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

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [hasCookie()](method-hascookie.md)
Method: [hasLoginCookie()](method-haslogincookie.md)
Method: [init()](method-___init.md) (hookable)
Method: [isValidSession()](method-___isvalidsession.md) (hookable)
Method: [isValidFingerprint()](method-isvalidfingerprint.md)
Method: [get()](method-get.md)
Method: [getVal()](method-getval.md)
Method: [getAll()](method-getall.md)
Method: [getAllFor()](method-getallfor.md)
Method: [set()](method-set.md)
Method: [getFor()](method-getfor.md)
Method: [getValFor()](method-getvalfor.md)
Method: [setFor()](method-setfor.md)
Method: [remove()](method-remove.md)
Method: [removeFor()](method-removefor.md)
Method: [removeAllFor()](method-removeallfor.md)
Method: [getNamespace()](method-getnamespace.md)
Method: [__get()](method-__get.md)
Method: [__set()](method-__set.md)
Method: [getIP()](method-getip.md)
Method: [login()](method-___login.md) (hookable)
Method: [forceLogin()](method-forcelogin.md)
Method: [loginSuccess()](method-___loginsuccess.md) (hookable)
Method: [loginFailure()](method-___loginfailure.md) (hookable)
Method: [allowLogin()](method-___allowlogin.md) (hookable)
Method: [allowLoginAttempt()](method-___allowloginattempt.md) (hookable)
Method: [authenticate()](method-___authenticate.md) (hookable)
Method: [logout()](method-___logout.md) (hookable)
Method: [setCookie()](method-setcookie.md)
Method: [removeCookies()](method-removecookies.md)
Method: [sessionCookieSameSite()](method-sessioncookiesamesite.md)
Method: [logoutSuccess()](method-___logoutsuccess.md) (hookable)
Method: [redirect()](method-___redirect.md) (hookable)
Method: [location()](method-location.md)
Method: [close()](method-close.md)
Method: [message()](method-message.md)
Method: [error()](method-error.md)
Method: [warning()](method-warning.md)
Method: [getHistory()](method-gethistory.md)
Method: [removeNotices()](method-removenotices.md)
Method: [CSRF()](method-csrf.md)

Constants:
Const: [fingerprintRemoteAddr](const-fingerprintremoteaddr.md)
Const: [fingerprintClientAddr](const-fingerprintclientaddr.md)
Const: [fingerprintUseragent](const-fingerprintuseragent.md)
Const: [fingerprintAccept](const-fingerprintaccept.md)
Const: [challengeSuffix](const-challengesuffix.md)
