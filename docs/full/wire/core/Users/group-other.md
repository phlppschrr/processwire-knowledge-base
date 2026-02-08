# Users: other

Source: `wire/core/Users.php`

@method PageArray find($selector) Return the User(s) matching the the given selector query.

@method User add($name) Add new User with the given name and return it.

@method bool save($user) Save given User.

@method bool delete($user) Delete the given User.

@method array saveReady($user) Hook called just before a User is saved

@method void saved($user, array $changes) Hook called after a User has been saved

@method void added($user) Hook called just after a User is added

@method void deleteReady($user) Hook called before a User is deleted

@method void deleted($user) Hook called after a User is deleted

@method User new($options = []) Create new User instance in memory (3.0.249+)
