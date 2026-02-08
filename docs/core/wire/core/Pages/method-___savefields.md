# $pages->saveFields(Page $page, $fields, array $options = array()): array

Source: `wire/core/Pages.php`

Save multiple named fields from given page

## Example

~~~~~
// you can specify field names as array…
$a = $pages->saveFields($page, [ 'title', 'body', 'summary' ]);

// …or a CSV string of field names:
$a = $pages->saveFields($page, 'title, body, summary');

// return value is array of saved field/property names
print_r($a); // outputs: array( 'title', 'body', 'summary' )
~~~~~

## Usage

~~~~~
// basic usage
$array = $pages->saveFields($page, $fields);

// usage with all arguments
$array = $pages->saveFields(Page $page, $fields, array $options = array());
~~~~~

## Hookable

- Hookable method name: `saveFields`
- Implementation: `___saveFields`
- Hook with: `$pages->saveFields()`

## Arguments

- `$page` `Page` Page to save
- `$fields` `array|string|string[]|Field[]` Array of field names to save or CSV/space separated field names to save. These should only be Field names and not native page property names.
- `$options` (optional) `array|string` Optionally specify one or more of the following to modify default behavior: - `quiet` (boolean): Specify true to bypass updating of modified user and time (default=false). - `noHooks` (boolean): Prevent before/after save hooks (default=false), please also use $pages->___saveField() for call. - See $options argument for Pages::save() for additional options

## Return value

- `array` Array of saved field names (may also include property names if they were modified)

## Exceptions

- `WireException`

## Since

3.0.242
