# PageTraversal::references()

Source: `wire/core/PageTraversal.php`

Return pages that are referencing the given one by way of Page references

@param Page $page

@param string|bool $selector Optional selector to filter results by or boolean true as shortcut for `include=all`.

@param Field|string $field Limit to follower pages using this field,
  - or specify boolean TRUE to make it return array of PageArrays indexed by field name.

@param bool $getCount Specify true to return counts rather than PageArray(s)

@return PageArray|array|int

@throws WireException Highly unlikely
