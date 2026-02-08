# $pages->deleteBranchReady(Page $page, array $options)

Source: `wire/core/Pages.php`

Hook called before a branch of pages is about to be deleted, called on root page of branch only

Note: this is called only on deletions that had 'recursive' option true and 1+ children.

## Usage

~~~~~
// basic usage
$result = $pages->deleteBranchReady($page, $options);

// usage with all arguments
$result = $pages->deleteBranchReady(Page $page, array $options);
~~~~~

## Hookable

- Hookable method name: `deleteBranchReady`
- Implementation: `___deleteBranchReady`
- Hook with: `$pages->deleteBranchReady()`

## Arguments

- `$page` `Page` Page that was deleted
- `$options` `array` Options passed to delete method

## Since

3.0.163
