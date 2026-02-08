# Page::___getMarkup()

Source: `wire/core/Page.php`

Return the markup value for a given field name or {tag} string

1. If given a field name (or `name.subname` or `name1|name2|name3`) it will return the
   markup value as defined by the fieldtype.
2. If given a string with field names referenced in `{tags}`, it will populate those
   tags and return the populated string.


@param string $key Field name or markup string with field {name} tags in it

@return string

@see Page::getText()
