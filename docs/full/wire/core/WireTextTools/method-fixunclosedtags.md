# $wireTextTools->fixUnclosedTags($str, $remove = true, $options = array()): string

Source: `wire/core/WireTextTools.php`

Remove (or close) unclosed HTML tags from given string

Remove unclosed tags:
---------------------
At present, if it finds an unclosed tag, it removes all tags of the same kind.
This is in order to keep the function fast, by delegating what it can to strip_tags().
This is sufficient for our internal use here, but may not be ideal for all situations.

Fix/close unclosed tags:
------------------------
When the remove option is false, it will attempt to close unclosed tags rather than
remove them. It doesn't know exactly where they should be closed, so it appends the
close tags to the end of the string.

## Arguments

- `$str` `string`
- `$remove` (optional) `bool` Remove unclosed tags? If false, it will attempt to close them instead. (default=true)
- `$options` (optional) `array` - `ignoreTags` (array): Tags that can be ignored because they close themselves. (default=per HTML spec)

## Return value

string
