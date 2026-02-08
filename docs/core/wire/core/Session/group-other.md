# Session: other

Source: `wire/core/Session.php`

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
