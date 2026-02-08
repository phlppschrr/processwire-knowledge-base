# Page::getText()

Source: `wire/core/Page.php`

Same as getMarkup() except returned value is plain text

If no `$entities` argument is provided, returned value is entity encoded when output formatting
is on, and not entity encoded when output formatting is off.


@param string $key Field name or string with field {name} tags in it.

@param bool $oneLine Specify true if returned value must be on single line.

@param bool|null $entities True to entity encode, false to not. Null for auto, which follows page's outputFormatting state.

@return string

@see Page::getMarkup()
