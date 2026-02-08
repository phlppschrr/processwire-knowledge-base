# $pagesNames->uniquePageName($name = '', $page = null, array $options = array()): string

Source: `wire/core/PagesNames.php`

Get a unique page name

1. If given no arguments, it returns a random globally unique page name.
2. If given just a $name, it returns that name (if globally unique), or an incremented version of it that is globally unique.
3. If given both $page and $name, it returns given name if unique in parent, or incremented version that is.
4. If given just a $page, the name is pulled from $page and behavior is the same as #3 above.

The returned value is not yet assigned to the given $page, so if it is something different than what
is already on $page, you’ll want to assign it manually after this.

## Arguments

- string|Page|array $name Name to make unique You may optionally substitute the $page argument or $options arguments here, if that is all you need.
- Page|string|null|array Page to exclude from duplicate check and/or to pull $name or parent from (if not otherwise specified). Note that specifying a Page is important if the page already exists, as it is used as the page to exclude when checking for name collisions, and we want to exclude $page from that check. You may optionally substitute the $options or $name arguments here, if that is all you need. If $parent or $name are specified separately from this $page argument, they will override whatever parent or name settings are on this $page argument.
- array $options - `parent` (Page|null): Optionally specify a different parent if $page does not currently have the parent you want to use. - `language` (Language|int): Get unique for this language (if multi-language page names active). - `page` (Page|null): If you specified no $page argument, you can optionally bundle it in the $options array. - `name` (string): If you specified no $name argument, you can optionally bundle it in the $options array.

## Return value

string Returns unique name
