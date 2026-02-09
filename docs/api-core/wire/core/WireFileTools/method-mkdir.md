# $wireFileTools->mkdir($path, $recursive = false, $chmod = null): bool

Source: `wire/core/WireFileTools.php`

Create a directory that is writable to ProcessWire and uses the defined $config chmod settings

Unlike PHP's `mkdir()` function, this function manages the read/write mode consistent with ProcessWire's
setting `$config->chmodDir`, and it can create directories recursively. Meaning, if you want to create directory /a/b/c/
and directory /a/ doesn't yet exist, this method will take care of creating /a/, /a/b/, and /a/b/c/.

The `$recursive` and `$chmod` arguments may optionally be swapped (since 3.0.34).

## Example

~~~~~
// Create a new directory in ProcessWire's cache dir
if($files->mkdir($config->paths->cache . 'foo-bar/')) {
  // directory created: /site/assets/cache/foo-bar/
}
~~~~~

## Usage

~~~~~
// basic usage
$bool = $wireFileTools->mkdir($path);

// usage with all arguments
$bool = $wireFileTools->mkdir($path, $recursive = false, $chmod = null);
~~~~~

## Arguments

- `$path` `string` Directory you want to create
- `$recursive` (optional) `bool|string` If set to true, all directories will be created as needed to reach the end.
- `$chmod` (optional) `string|null|bool` Optional mode to set directory to (default: $config->chmodDir), format must be a string i.e. "0755" If omitted, then ProcessWire's `$config->chmodDir` setting is used instead.

## Return value

- `bool` True on success, false on failure
