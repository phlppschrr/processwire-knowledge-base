# FunctionsAPI::roles()

Source: `wire/core/FunctionsAPI.php`

Get, find or save roles ($roles API variable as a function)

Accessing `roles()` is exactly the same as accessing `$roles`. Though there are a couple of optional
shortcuts available by providing an argument to this function.


@param string|int $selector
 - Specify name or ID of role to get (Role object)
 - Specify selector string matching roles to find (PageArray object)

@return Roles|Role|PageArray|null|NullPage

@see Roles
