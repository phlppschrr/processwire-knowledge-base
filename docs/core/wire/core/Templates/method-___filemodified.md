# $templates->fileModified(Template $template)

Source: `wire/core/Templates.php`

Hook called when a Template detects that its file has changed

Note that the hook is not called until something in the system (like a page render) asks for the template’s filename.
That’s because it would not be efficient for PW to check the file for every template in the system on every request.

## Usage

~~~~~
// basic usage
$result = $templates->fileModified($template);

// usage with all arguments
$result = $templates->fileModified(Template $template);
~~~~~

## Hookable

- Hookable method name: `fileModified`
- Implementation: `___fileModified`
- Hook with: `$templates->fileModified()`

## Arguments

- `$template` `Template`

## Since

3.0.141
