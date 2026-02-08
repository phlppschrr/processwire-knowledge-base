# $user->hasRole($role): bool

Source: `wire/core/User.php`

Does this user have the given Role?


~~~~~
if($user->hasRole('editor')) {
  // user has the editor role
}
~~~~~

## Arguments

- `$role` `string|Role|int` May be Role name, object or ID.

## Return value

bool
