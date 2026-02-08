# PagesEditor::touch()

Source: `wire/core/PagesEditor.php`

Update page modified/created/published time to now (or given time)


@param Page|PageArray|array $pages May be Page, PageArray or array of page IDs (integers)

@param null|int|string|array $options Omit (null) to update to now, or unix timestamp or strtotime() recognized time string,
 or if you do not need this argument, you may optionally substitute the $type argument here,
 or in 3.0.183+ you can also specify array of options here instead:
 - `time` (string|int|null): Unix timestamp or strtotime() recognized string to use, omit for use current time (default=null)
 - `type` (string): One of 'modified', 'created', 'published' (default='modified')
 - `user` (bool|User): True to also update modified/created user to current user, or specify User object to use (default=false)

@param string $type Date type to update, one of 'modified', 'created' or 'published' (default='modified') Added 3.0.147
 Skip this argument if using options array for previous argument or if using the default type 'modified'.

@throws WireException|\PDOException if given invalid format for $modified argument or failed database query

@return bool True on success, false on fail
