# $wireFileTools->zip($zipfile, $files, array $options = array()): array

Source: `wire/core/WireFileTools.php`

Creates a ZIP file

~~~~~
// Create zip of all files in directory $dir to file $zip
$dir = $config->paths->cache . "my-files/";
$zip = $config->paths->cache . "my-file.zip";
$result = $files->zip($zip, $dir);

echo "<h3>These files were added to the ZIP:</h3>";
foreach($result['files'] as $file) {
  echo "<li>" $sanitizer->entities($file) . "</li>";
}

if(count($result['errors'])) {
  echo "<h3>There were errors:</h3>";
  foreach($result['errors'] as $error) {
    echo "<li>" . $sanitizer->entities($error) . "</li>";
  }
}
~~~~~

## Arguments

- `$zipfile` `string` Full path and filename to create or update (i.e. /path/to/myfile.zip)
- `$files` `array|string` Array of files to add (full path and filename), or directory (string) to add. If given a directory, it will recursively add everything in that directory.
- `$options` (optional) `array` Associative array of options to modify default behavior: - `allowHidden` (boolean or array): allow hidden files? May be boolean, or array of hidden files (basenames) you allow. (default=false) Note that if you actually specify a hidden file in your $files argument, then that overrides this. - `allowEmptyDirs` (boolean): allow empty directories in the ZIP file? (default=true) - `overwrite` (boolean): Replaces ZIP file if already present (rather than adding to it) (default=false) - `maxDepth` (int): Max dir depth 0 for no limit (default=0). Specify 1 to stay only in dirs listed in $files. - `exclude` (array): Files or directories to exclude - `dir` (string): Directory name to prepend to added files in the ZIP

## Return value

array Returns associative array of: - `files` (array): all files that were added - `errors` (array): files that failed to add, if any

## Throws

- WireException Original ZIP file creation error conditions result in WireException being thrown.

## See also

- [WireFileTools::unzip()](method-unzip.md)
