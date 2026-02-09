# $wire->error($text, $flags = 0): $this

Source: `wire/core/Wire.php`

Record an non-fatal error message in the system-wide notices.

- This method automatically identifies the error as coming from this class.
- You should still make fatal errors throw a `WireException` (or class derived from it).

## Example

~~~~~
$this->error("This is the notice text");
$this->error("This notice is also logged", true);
$this->error("This notice is only shown in debug mode", Notice::debug);
$this->error("This notice allows <em>markup</em>", Notice::allowMarkup);
$this->error("Notice using multiple flags", Notice::debug | Notice::logOnly);
~~~~~

## Usage

~~~~~
// basic usage
$result = $wire->error($text);

// usage with all arguments
$result = $wire->error($text, $flags = 0);
~~~~~

## Arguments

- `$text` `string|array|Wire` Text to include in the notice
- `$flags` (optional) `int|bool|string` Optional flags to alter default behavior: - `Notice::admin` (constant): Show notice only if user is in the admin. - `Notice::allowMarkdown` (constant): Allow basic markdown and bracket markup (see $sanitizer->entitiesMarkdown()). - `Notice::allowMarkup` (constant): Indicates notice should allow the use of HTML markup tags. - `Notice::debug` (constant): Indicates notice should only be shown when debug mode is active. - `Notice::log` (constant): Indicates notice should also be logged. - `Notice::logOnly` (constant): Indicates notice should only be logged. - `Notice::login` (constant): Show notice only if it will be seen by a logged-in user. - `Notice::noGroup` (constant): Indicates notice should not group with others of the same type (where supported). - `Notice::prepend` (constant): Indicates notice should prepend rather than append. - `Notice::superuser` (constant): Show notice only if current user is a superuser. - `true` (boolean): Shortcut for the `Notice::log` constant. - In 3.0.149+ you may also specify a space-separated string of flag names, i.e. "admin log noGroup".

## Return value

- `$this`

## See Also

- [Wire::errors()](method-errors.md)
- [Wire::message()](method-message.md)
- [Wire::warning()](method-warning.md)
