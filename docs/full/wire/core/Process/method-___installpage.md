# $process->___installPage($name = '', $parent = null, $title = '', $template = 'admin', $extras = array()): Page

Source: `wire/core/Process.php`

Install a dedicated page for this Process module and assign it this Process

To be called by Process module's ___install() method.

## Usage

~~~~~
// basic usage
$page = $process->___installPage();

// usage with all arguments
$page = $process->___installPage($name = '', $parent = null, $title = '', $template = 'admin', $extras = array());
~~~~~

## Arguments

- `$name` (optional) `string` Desired name of page, or omit (or blank) to use module name
- Page|string|int|null Parent for the page, with one of the following: - name of parent, relative to admin root, i.e. "setup" - Page object of parent - path to parent - parent ID - Or omit and admin root is assumed
- `$title` (optional) `string` Omit or blank to pull title from module information
- string|Template Template to use for page (omit to assume 'admin')
- `$extras` (optional) `array` Any extra properties to assign (like status)

## Return value

- `Page` Returns the page that was created

## Exceptions

- `WireException` if page can't be created
