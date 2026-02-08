# User::isSuperuser()

Source: `wire/core/User.php`

Does this user have the superuser role?

Same as calling `$user->roles->has('name=superuser');` but potentially faster.


@return bool
