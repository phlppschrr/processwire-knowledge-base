# $user->setLanguage($language): self

Source: `wire/core/User.php`

Set language for user (quietly)

- Sets the language without tracking it as a change to the user.
- If language support is not installed this method silently does nothing.

## Arguments

- `$language` `Language|string|int` Language object, name, or ID

## Return value

self

## Throws

- WireException if language support is installed and given an invalid/unknown language

## Since

3.0.186
