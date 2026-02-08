# Page::setUser()

Source: `wire/core/Page.php`

Set either the createdUser or the modifiedUser

@param User|int|string $user User object or integer/string representation of User

@param string $userType Must be either 'created' or 'modified'

@return $this

@throws WireException
