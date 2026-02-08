# $user->isLoggedin(): bool

Source: `wire/core/User.php`

Is the current $user logged in and the same as this user?

When this method returns true, it means the current $user (API variable) is
this user and that they are logged in.

## Usage

~~~~~
// basic usage
$bool = $user->isLoggedin();
~~~~~

## Return value

- `bool`
