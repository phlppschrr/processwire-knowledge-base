# $wireFileTools->render($filename, array $vars = array(), array $options = array()): string|bool

Source: `wire/core/WireFileTools.php`

Given a filename, render it as a ProcessWire template file

This is a shortcut to using the TemplateFile class.

File is assumed relative to `/site/templates/` (or a directory within there) unless you specify a full path.
If you specify a full path, it will accept files in or below any of the following:

- /site/templates/
- /site/modules/
- /wire/modules/

Note this function returns the output to you, so that you can send the output wherever you want (delayed output).
For direct output, use the `$files->include()` function instead.

## Usage

~~~~~
// basic usage
$string = $wireFileTools->render($filename);

// usage with all arguments
$string = $wireFileTools->render($filename, array $vars = array(), array $options = array());
~~~~~

## Arguments

- `$filename` `string` Assumed relative to /site/templates/ unless you provide a full path name with the filename. If you provide a path, it must resolve somewhere in site/templates/, site/modules/ or wire/modules/.
- `$vars` (optional) `array` Optional associative array of variables to send to template file. Please note that all template files automatically receive all API variables already (you don't have to provide them).
- `$options` (optional) `array` Associative array of options to modify behavior: - `defaultPath` (string): Path where files are assumed to be when only filename or relative filename is specified (default=/site/templates/) - `autoExtension` (string): Extension to assume when no ext in filename, make blank for no auto assumption (default=php) - `allowedPaths` (array): Array of paths that are allowed (default is templates, core modules and site modules) - `allowDotDot` (bool): Allow use of ".." in paths? (default=false) - `throwExceptions` (bool): Throw exceptions when fatal error occurs? (default=true) - `cache` (int|string|Page): Specify non-zero value to cache rendered result for this many seconds, or see the `WireCache::renderFile()` method `$expire` argument for more options you can specify here. (default=0, no cache) *Note: this option added in 3.0.130*

## Return value

- `string|bool` Rendered template file or boolean false on fatal error (and throwExceptions disabled)

## Exceptions

- `WireException` if template file doesn't exist

## See Also

- [WireFileTools::include()](method-___include.md)
