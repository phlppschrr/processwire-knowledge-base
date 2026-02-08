# $process->execute(): string|array

Source: `wire/core/Process.php`

Execute this Process and return the output. You may have any number of execute[name] methods, triggered by URL segments.

When any execute() method returns a string, it us used as the actual output.
When the method returns an associative array, it is considered an array of variables
to send to the output view layer. Returned array must not be empty, otherwise it cannot
be identified as an associative array.

This execute() method is called when no URL segments are present. You may have any
number of execute() methods, i.e. `executeFoo()` would be called for the URL `./foo/`
and `executeBarBaz()` would be called for the URL `./bar-baz/`.

## Usage

~~~~~
// basic usage
$string = $process->execute();
~~~~~

## Hookable

- Hookable method name: `execute`
- Implementation: `___execute`
- Hook with: `$process->execute()`

## Return value

- `string|array`
