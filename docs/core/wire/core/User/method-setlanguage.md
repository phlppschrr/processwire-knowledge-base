# User::setLanguage()

Source: `wire/core/User.php`

Set language for user (quietly)

- Sets the language without tracking it as a change to the user.
- If language support is not installed this method silently does nothing.


@param Language|string|int $language Language object, name, or ID

@return self

@throws WireException if language support is installed and given an invalid/unknown language

@since 3.0.186
