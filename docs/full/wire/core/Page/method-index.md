# $page->index($selector = ''): int

Source: `wire/core/Page.php`

Return the index/position of this page relative to siblings.

If given a hidden or unpublished page, that page would not usually be part of the group of siblings.
As a result, such pages will return what the value would be if they were visible (as of 3.0.121). This
may overlap with the index of other pages, since indexes are relative to visible pages, unless you
specify an include mode (see next paragraph).

If you want this method to include hidden/unpublished pages as part of the index numbers, then
specify boolean true for the $selector argument (which implies "include=all") OR specify a
selector of "include=hidden", "include=unpublished" or "include=all".

~~~~~
$i = $page->index();
$n = $page->parent->numChildren();
echo "This page is $i out of $n total pages";
~~~~~

## Arguments

- bool|string|array Specify one of the following (since 3.0.121): - Boolean true to include hidden and unpublished pages as part of the index numbers (same as "include=all"). - An "include=hidden", "include=unpublished" or "include=all" selector to include them in the index numbers. - A string selector or selector array to filter the criteria for the returned index number.

## Return value

int Returns index number (zero-based)

## Since

3.0.24
