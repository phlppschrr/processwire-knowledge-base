# $page->rootParent(): Page

Source: `wire/core/Page.php`

Get the lowest-level, non-homepage parent of this page

The rootParents typically comprise the first level of navigation on a site, and in many cases are considered
the "section" pages of the site.

## Example

~~~~~
// Determine if we are in the "products" section of the site
if($page->rootParent()->template == 'products') {
  // we are in the products section
} else {
  // we are in some other section of the site
}
~~~~~

## Usage

~~~~~
// basic usage
$page = $page->rootParent();
~~~~~

## Hookable

- Hookable method name: `rootParent`
- Implementation: `___rootParent`
- Hook with: `$page->rootParent()`

## Return value

- `Page`
