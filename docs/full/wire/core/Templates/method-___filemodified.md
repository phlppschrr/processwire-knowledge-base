# $templates->___fileModified(Template $template)

Source: `wire/core/Templates.php`

Hook called when a Template detects that its file has changed

Note that the hook is not called until something in the system (like a page render) asks for the template’s filename.
That’s because it would not be efficient for PW to check the file for every template in the system on every request.

## Arguments

- `$template` `Template`

## Since

3.0.141
