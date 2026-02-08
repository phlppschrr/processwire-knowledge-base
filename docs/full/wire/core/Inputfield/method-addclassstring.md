# Inputfield::addClassString()

Source: `wire/core/Inputfield.php`

Add class(es) by formatted string that lets you specify where class should be added

To use this in the public API use `addClass()` method or set the `addClass` property
with a formatted string value as indicated here.

Allows for setting via formatted string like:
~~~~~
wrap:card card-default
header:card-header
content:card-body
input:form-input input-checkbox
~~~~~
Each line represents a group containing a element type, colon, and one or more space-
separated classes. Groups may be separated by newline (like above) or with a comma.
The element type may be any one of the following:

 - `wrap`: The .Inputfield element that wraps the header and content
 - `header`: The .InputfieldHeader element, typically a `<label>`.
 - `content`: The .InputfieldContent element that wraps the input(s), typically a `<div>`.
 - `input`: The primary `<input>` element(s) that accept input for the Inputfield.
 - `class`: This is the same as the 'input' type, just an alias.
 - `+foo`: Force adding your own new element type (i.e. “foo”) that is not indicated above.

Class names prefixed with a minus sign i.e. `-class` will be removed rather than added.

A string like `hello:world` where `hello` is not one of those element types listed above,
and is not prefixed with a plus sign `+`, will be added as a literal class name with the
colon in it (such as those used by Tailwind).

@param string $class Formatted class string to parse class types and names from

@param string $property Default/fallback element/property if not indicated in string

@return self

@since 3.0.204
