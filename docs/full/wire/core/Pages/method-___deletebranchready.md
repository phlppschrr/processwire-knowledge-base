# $pages->___deleteBranchReady(Page $page, array $options)

Source: `wire/core/Pages.php`

Hook called before a branch of pages is about to be deleted, called on root page of branch only

Note: this is called only on deletions that had 'recursive' option true and 1+ children.

## Arguments

- Page $page Page that was deleted
- array $options Options passed to delete method

## Meta

- @since 3.0.163
