# Pages::___deletedBranch()

Source: `wire/core/Pages.php`

Hook called after a a branch of pages has been deleted, called on root page of branch only

Note: this is called only on deletions that had 'recursive' option true and 1+ children.


@param Page $page Page that was the root of the branch

@param array $options Options passed to delete method

@param int $numDeleted Number of pages deleted

@since 3.0.163
