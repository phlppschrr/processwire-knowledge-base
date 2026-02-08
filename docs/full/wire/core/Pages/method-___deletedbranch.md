# $pages->___deletedBranch(Page $page, array $options, $numDeleted)

Source: `wire/core/Pages.php`

Hook called after a a branch of pages has been deleted, called on root page of branch only

Note: this is called only on deletions that had 'recursive' option true and 1+ children.

## Arguments

- `$page` `Page` Page that was the root of the branch
- `$options` `array` Options passed to delete method
- `$numDeleted` `int` Number of pages deleted

## Since

3.0.163
