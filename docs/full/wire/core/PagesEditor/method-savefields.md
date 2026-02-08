# PagesEditor::saveFields()

Source: `wire/core/PagesEditor.php`

Save multiple named fields from given page

~~~~~
// you can specify field names as array…
$a = $pages->saveFields($page, [ 'title', 'body', 'summary' ]);

// …or a CSV string of field names:
$a = $pages->saveFields($page, 'title, body, summary');

// return value is array of saved field/property names
print_r($a); // outputs: array( 'title', 'body', 'summary' )
~~~~~


@param Page $page Page to save

@param array|string|string[]|Field[] $fields Array of field names to save or CSV/space separated field names to save.
  These should only be Field names and not native page property names.

@param array|string $options Optionally specify one or more of the following to modify default behavior:
 - `quiet` (bool): Specify true to bypass updating of modified user and time (default=false).
 - `noHooks` (bool): Prevent before/after save hooks, please also use `$pages->___saveFields()` for call. (default=false)
 - See $options argument in `Pages::save()` for additional options.

@return array Array of saved field names (may also include property names if they were modified)

@throws WireException

@since 3.0.242
