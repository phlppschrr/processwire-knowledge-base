# $pagesNames->pageNameFromFormat(Page $page, $format = '', array $options = array()): string

Source: `wire/core/PagesNames.php`

Create a page name from the given format

- Returns a generated page name that is not yet assigned to the page.
- If no format is specified, it first falls back to page parent template `childNameFormat` property (if present).
- If no format can be determined, it falls back to a randomly generated page name.
- Does not check if page name is already in use.

Options for $format argument:

- `title` Build name based on “title” field.
- `field` Build name based on any other field name you choose, replace “field” with any field name.
- `text` Text already in the right format (that’s not a field name) will be used literally, replace “text” with your text.
- `random` Randomly generates a name.
- `untitled` Uses an auto-incremented “untitled” name.
- `untitled-time` Uses an “untitled” name followed by date/time number string.
- `a|b|c` Builds name from first matching field name, where a|b|c are your field names.
- `{field}` Builds name from the given field name.
- `{a|b|c}` Builds name first matching field name, where a|b|c would be replaced with your field names.
- `date:Y-m-d-H-i` Builds name from current date - replace “Y-m-d-H-i” with desired wireDate() format.
- `string with space` A string that does not match one of the above and has space is assumed to be a wireDate() format.
- `string with /` A string that does not match one of the above and has a “/” slash is assumed to be a wireDate() format.

For formats above that accept a wireDate() format, see `WireDateTime::date()` method for format details. It accepts PHP
date() format, PHP strftime() format, as well as some other predefined options.

## Usage

~~~~~
// basic usage
$string = $pagesNames->pageNameFromFormat($page);

// usage with all arguments
$string = $pagesNames->pageNameFromFormat(Page $page, $format = '', array $options = array());
~~~~~

## Arguments

- `$page` `Page`
- `$format` (optional) `string|array` Optional format. If not specified, pulls from $page’s parent template.
- `$options` (optional) `array` Options to modify behavior. May also be specified in $format argument. - `language` (Language|string): Language to use - `format` (string): Optional format to use, if $options were specified in $format argument.

## Return value

- `string`
