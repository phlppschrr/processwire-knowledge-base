# $session->___authenticate(User $user, $pass): bool

Source: `wire/core/Session.php`

Return true or false whether the user authenticated with the supplied password

## Usage

~~~~~
// basic usage
$bool = $session->___authenticate($user, $pass);

// usage with all arguments
$bool = $session->___authenticate(User $user, $pass);
~~~~~

## Arguments

- `$user` `User` User attempting to login
- `$pass` `string` Password they are attempting to login with

## Return value

- `bool`
