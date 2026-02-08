# Roles: other

Source: `wire/core/Roles.php`

@method PageArray find($selector) Return the Role(s) matching the the given selector.

@method Role add($name) Add new Role with the given name and return it.

@method bool save(Role $role) Save given role.

@method bool delete(Role $role) Delete the given role.

@method array saveReady(Page $page) Hook called just before a Role is saved

@method void saved(Page $page, array $changes = [], $values = []) Hook called after a role has been saved

@method void added(Page $page) Hook called just after a Role is added

@method void deleteReady(Page $page) Hook called before a Role is deleted

@method void deleted(Page $page) Hook called after a Role is deleted

@method Role new($options = []) Create new Role instance in memory (3.0.249+)
