# $wireMarkupFileRegions->findRegions(&$html, array $options): array

Source: `wire/core/WireMarkupFileRegions.php`

Find and return file regions in given HTML

## Usage

~~~~~
// basic usage
$array = $wireMarkupFileRegions->findRegions($html, $options);

// usage with all arguments
$array = $wireMarkupFileRegions->findRegions(&$html, array $options);
~~~~~

## Arguments

- `$html` `string`
- `$options` `array` - `action` (string): The "pw-[action]" or "data-pw-[action]" attribute to look for (default='file') - `tags` (array): Array of tag names to allow for action, and default action value (when non specified) - `exts` (array): File extensions to allow in action value (default=['css','less', 'scss','sass','js']) - `allowPaths` (bool): Allow paths in action value? (default=false)

## Return value

- `array`

## Since

3.0.254
