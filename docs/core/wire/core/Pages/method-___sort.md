# $pages->___sort(Page $page, $value = false): int

Source: `wire/core/Pages.php`

Set the “sort” value for given $page while adjusting siblings, or re-build sort for its children

*This method is primarily applicable to manually sorted pages. If pages are automatically
sorted by some other field, this method isn’t useful unless using the “re-build children” option,
which may be helpful if converting a page’s children from auto-sort to manual sort.*

The default behavior of this method is to set the “sort” value for the given $page, and adjust the
sort value of sibling pages having the same or greater sort value, to ensure all are unique and in
order without gaps.

The alternate behavior of this method is to re-build the sort values of all children of the given $page.
This is done by specifying boolean true for the $value argument. When used, duplicate sort values and
gaps are removed from all children.

**Do you need this method?**
If you are wondering whether you need to use this method for something, chances are that you do not.
This method is mostly applicable for internal core use, as ProcessWire manages Page sort values on its own
internally for the most part.

~~~~~
// set $page to have sort=5, moving any 5+ sort pages ahead
$pages->sort($page, 5);

// re-build sort values for children of $page, removing duplicates and gaps
$pages->sort($page, true);
~~~~~

## Arguments

- `$page` `Page` Page to sort (or parent of pages to sort, if using $value=true option)
- `$value` (optional) `int|bool` Specify one of the following: - Omit to set and use sort value from given $page. - Specify sort value (integer) to save that value. - Specify boolean true to instead rebuild sort for all of $page children.

## Return value

int Number of pages that had sort values adjusted

## Throws

- WireException
