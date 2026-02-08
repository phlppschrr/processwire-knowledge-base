# $inputfieldWrapper->child($name = '', $recursive = true): Inputfield|null

Source: `wire/core/InputfieldWrapper.php`

Find an Inputfield below this one that has the given name

This is an alternative to the `getChildByName()` method, with more options for when you need it.
For instance, it can also accept a selector string or numeric index for the $name argument, and you
can optionally disable the $recursive behavior.

## Arguments

- string|int $name Name or selector string of child to find, omit for first child, or specify zero-based index of child to return.
- bool $recursive Find child recursively? Looks for child in this wrapper, and all other wrappers below it. (default=true)

## Return value

Inputfield|null Returns Inputfield instance if found, or null if not.

## Meta

- @since 3.0.110
