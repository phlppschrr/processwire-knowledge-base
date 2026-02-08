# $inputfieldWrapper->___new($typeName, $name = '', $label = '', $settings = array()): Inputfield|InputfieldSelect|InputfieldWrapper

Source: `wire/core/InputfieldWrapper.php`

Create a new Inputfield, add it to this InputfieldWrapper, and return the new Inputfield

- Only the $typeName argument is required.
- You may optionally substitute the $settings argument for the $name or $label arguments.
- You may optionally substitute Inputfield “description” property for $settings argument.

## Arguments

- string $typeName Inputfield type, i.e. “InputfieldCheckbox” or just “checkbox” for short.
- string|array $name Name of input (or substitute $settings here).
- string|array $label Label for input (or substitute $settings here).
- array|string $settings Settings to add to Inputfield (optional). Or if string, assumed to be “description”.

## Return value

Inputfield|InputfieldSelect|InputfieldWrapper An Inputfield instance ready to populate with additional properties/attributes.

## Throws

- WireException If you request an unknown Inputfield type

## Meta

- @since 3.0.110
