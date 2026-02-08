# FunctionsAPI::user()

Source: `wire/core/FunctionsAPI.php`

Get the currently logged in user ($user API variable as a function)

This function behaves the same as the `$user` API variable, though does support
optional shortcut arguments for getting or setting values.


@param string $key Optional property to get or set

@param null $value Optional value to set

@return User|mixed

@see User
