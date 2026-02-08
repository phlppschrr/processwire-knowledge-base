# $inputfieldWrapper->removeByName($name): Inputfield|null

Source: `wire/core/InputfieldWrapper.php`

Remove an Inputfield from the form by name

Note that this works the same as the getByName/getChildByName methods in that it
will find (and remove) the field by name, even if nested within other wrappers
or fieldsets. It returns the removed Inputfield when found, or null if not.

## Arguments

- string $name

## Return value

Inputfield|null Removed Inputfield object on success, or null if not found

## Meta

- @since 3.0.250
