# $languages->getLanguage($name = ''): Language|null

Source: `wire/modules/LanguageSupport/Languages.php`

Get the current language or optionally a specific named language

- This method is not entirely necessary but is here to accompany the setLanguage() method for syntax convenience.
- If you specify a `$name` argument, this method works the same as the `$languages->get($name)` method.
- If you call with no arguments, it returns the current user language, same as `$user->language`, but using this
  method may be preferable in some contexts, depending on how your IDE understands API calls.

## Arguments

- string|int $name Specify language name (or ID) to get a specific language, or omit to get current language

## Return value

Language|null

## Meta

- @since 3.0.127
