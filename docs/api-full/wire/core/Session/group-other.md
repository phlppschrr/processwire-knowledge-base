# Session: other

Source: `wire/core/Session.php`

- [`login(): User`](method-___login.md) login($name, $pass, $force = false) Login the user identified by $name and authenticated by $pass. Returns the user object on successful login or null on failure.
- [`logout(): Session`](method-___logout.md) logout() Logout the current user, and clear all session variables.
- [`redirect(): void`](method-___redirect.md) redirect($url, $http301 = true) Redirect this session to the specified URL.
- [`init(): void`](method-___init.md) Initialize session (called automatically by constructor)
- [`authenticate(User $user, $pass): bool`](method-___authenticate.md)
- [`isValidSession($userID): bool`](method-___isvalidsession.md)
- [`allowLoginAttempt($name): bool`](method-___allowloginattempt.md)
- [`allowLogin($name, User $user = null): bool`](method-___allowlogin.md)
- [`loginSuccess(User $user): void`](method-___loginsuccess.md)
- [`loginFailure($name, $reason): void`](method-___loginfailure.md)
- [`logoutSuccess(User $user): void`](method-___logoutsuccess.md)
- [`$CSRF: SessionCSRF`](method-csrf.md)
