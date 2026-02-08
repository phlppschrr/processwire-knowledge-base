# $wireFileTools->unzip($zipFile, $destinationPath, array $options = []): array

Source: `wire/core/WireFileTools.php`

Unzips the given ZIP file to the destination directory

~~~~~
// Unzip a file
$zip = $config->paths->cache . "my-file.zip";
$dst = $config->paths->cache . "my-files/";
$items = $files->unzip($zip, $dst);
if(count($items)) {
  // $items is an array of filenames that were unzipped into $dst
}
~~~~~

## Arguments

- string $zipFile ZIP file to extract
- string $destinationPath Directory where files should be unzipped into. Directory is created if it doesn't exist.
- array $options Options to modify default behavior (3.0.254+): - `extractFiles` (array): Filenames or regex patterns for files to extract, ignoring all others. (default=[]) - `extractExtensions` (array): Only extract these file extensions, ignoring all others. (default=[]) - `ignoreFiles` (array): Basenames or regex patterns matching basenames to skip/ignore (default=[ '.DS_Store', '__MACOSX' ]) - `ignoreExtensions` (array): Extensions to skip/ignore for files in the ZIP (default=[ 'zip' ]) - `minFiles` (int): Minimum number files that must be present inside the ZIP for it to be valid. (default=1) - `maxFiles` (int): Maximum number of files allowed in ZIP (default=1000) - `maxDepth` (int): $maxDepth Maximum allowed folder/directory depth in ZIP (default=8) - `maxFileMegabytes` (int): Maximum allowed uncompressed size of any individual file in ZIP, in MB. (default=20) - `maxTotalMegabytes` (int): Maximum allowed total uncompressed size of all files in ZIP, in MB. (default=100) - `maxErrors` (int): Maximum number of errors to report (default=10) - `requireFiles` (array): File names or regex patterns that must be present in at least one file for ZIP to be valid. For example `!\.json$!` would require that a `.json` file is present in the ZIP. default=[] - `fatalFiles` (array): Strings or regex patterns that when matched, cause entire ZIP to fail validation. If not given a regex, it matches any part of the filename. (default=[]) - `maxCompRatio` (int): Max allowed compression ratio or 0 to ignore (default=0) - `test` (bool|string): Do not actually unzip but return the filenames that would be unzipped. Specify 'verbose' rather than true to return verbose array of info instead of filenames. (default=false) - For the `extractFiles`, `ignoreFiles`, `requireFiles` and `fatalFiles` options, You can optionally specify a regex pattern by using a `!` as your regex starting and ending delimiter.

## Return value

array Returns an array of filenames (excluding $dst) that were unzipped.

## Throws

- WireException All error conditions result in WireException being thrown.

## See also

- [WireFileTools::zip()](method-zip.md)
