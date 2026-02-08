# $functionsAPI->users($selector = ''): Users|PageArray|User|mixed

Source: `wire/core/FunctionsAPI.php`

Get, find or save users ($users API variable as a function)

This function behaves the same as the `$users` API variable, though does support
an optional shortcut argument for getting a single user or finding multiple users.

~~~~~~
// Get a single user (regular and shortcut syntax)
$u = users()->get('karen');
$u = users('karen');

// Find multiple users (regular and shortcut syntax)
$us = users()->find('roles.name=editor');
$us = users('roles.name=editor');
~~~~~~

## Arguments

- string|array|int $selector Optional selector to send to find() or get() - Specify user name or ID to get and return that User - Specify a selector string to find all users matching selector (PageArray)

## Return value

Users|PageArray|User|mixed

## See also

- pages()
- Users
