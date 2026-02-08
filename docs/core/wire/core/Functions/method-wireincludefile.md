# $functions->wireIncludeFile($filename, array $vars = array(), array $options = array()): bool

Source: `wire/core/Functions.php`

Include a PHP file passing it all API variables and optionally your own specified variables

This is the procedural version of the `$files->include()` method.

This is the same as PHP’s `include()` function except for the following:

- It receives all API variables and optionally your custom variables
- If your filename is not absolute, it doesn’t look in PHP’s include path, only in the current dir.
- It only allows including files that are part of the PW installation: templates, core modules or site modules
- It will assume a “.php” extension if filename has no extension.

Note this function produces direct output. To retrieve output as a return value, use the
`wireRenderFile()` or `$files->render()` function instead.

## Arguments

- string $filename Filename to include
- array $vars Optional variables you want to hand to the include (associative array)
- array $options Array of options to modify behavior: - `func` (string): Function to use: include, include_once, require or require_once (default=include) - `autoExtension` (string): Extension to assume when no ext in filename, make blank for no auto assumption (default=php) - `allowedPaths` (array): Array of start paths include files are allowed from. Note current dir is always allowed.

## Return value

bool Always returns true

## Throws

- WireException if file doesn’t exist or is not allowed

## See also

- wireRenderFile()
- [WireFileTools::include()](../WireFileTools/method-___include.md)
- [WireFileTools::render()](../WireFileTools/method-render.md)
