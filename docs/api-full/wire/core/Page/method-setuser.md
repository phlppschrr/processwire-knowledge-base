# $page->setUser($user, $userType): $this

Source: `wire/core/Page.php`

Set either the createdUser or the modifiedUser

## Usage

~~~~~
// basic usage
$result = $page->setUser($user, $userType);
~~~~~

## Arguments

- `$user` `User|int|string` User object or integer/string representation of User
- `$userType` `string` Must be either 'created' or 'modified'

## Return value

- `$this`

## Exceptions

- `WireException`
