# $wireTextTools->findPlaceholders($str, array $options = array()): array|bool

Source: `wire/core/WireTextTools.php`

Find and return all {placeholder} tags found in given string

## Arguments

- string $str String that might contain field {tags}
- array $options - `has` (bool): Specify true to only return true or false if it has tags (default=false). - `tagOpen` (string): The required opening tag character(s), default is '{' - `tagClose` (string): The required closing tag character(s), default is '}'

## Return value

array|bool Always returns array unless you specify the `has` option as true.

## Meta

- @since 3.0.126
