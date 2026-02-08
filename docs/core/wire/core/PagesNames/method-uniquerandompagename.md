# $pagesNames->uniqueRandomPageName($options = array()): string

Source: `wire/core/PagesNames.php`

Get a random, globally unique page name

## Arguments

- array $options - `page` (Page): If name is or should be assigned to a Page, specify it here. (default=null) - `length` (int): Required/fixed length, or omit for random length (default=0). - `min` (int): Minimum required length, if fixed length not specified (default=6). - `max` (int): Maximum allowed length, if fixed length not specified (default=min*2). - `alpha` (bool): Include alpha a-z letters? (default=true) - `numeric` (bool): Include numeric digits 0-9? (default=true) - `confirm` (bool): Confirm that name is globally unique? (default=true) - `parent` (Page|int): If specified, name must only be unique for this parent Page or ID (default=0). - `prefix` (string): Prepend this prefix to page name (default=''). - `suffix` (string): Append this suffix to page name (default='').

## Return value

string
