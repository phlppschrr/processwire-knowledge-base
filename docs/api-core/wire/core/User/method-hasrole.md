# $user->hasRole($role): bool

Source: `wire/core/User.php`

Does this user have the given Role?

## Example

~~~~~
if($user->hasRole('editor')) {
  // user has the editor role
}
~~~~~

## Usage

~~~~~
// basic usage
$bool = $user->hasRole($role);
~~~~~

## Arguments

- `$role` `string|Role|int` May be Role name, object or ID.

## Return value

- `bool`
