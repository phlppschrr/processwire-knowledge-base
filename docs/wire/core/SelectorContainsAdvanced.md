# SelectorContainsAdvanced

Source: `wire/core/Selector.php`

Selector for advanced text searches that interprets specific search commands

- `foo` Optional word has no prefix.
- `+foo` Required word has a "+" prefix.
- `+foo*` Required words starting with "foo" (i.e. "fool", "foobar", etc.) has "+" prefix and "*" wildcard suffix.
- `-bar` Disallowed word has a "-" prefix.
- `-bar*` Disallowed words starting with "bar" (i.e. "barn", "barbell", etc.) has "-" prefix and "*" wildcard suffix.
- `"foo bar baz"` Optional phrase surrounded in quotes.
- `+"foo bar baz"` Required phrase with "+" prefix followed by double-quoted value.
- `-"foo bar baz"` Disallowed phrase with "-" prefix followed by double-quoted value.

Note that to designate a phrase, it must be in "double quotes" (not 'single quotes').

## valueToCommands()

Return array of advanced search commands from given value

@param string $value

@return array
