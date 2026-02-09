# SelectorContainsMatchExpand

Source: `wire/core/Selector.php`

Inherits: `SelectorContainsMatch`

Selector that uses standard MySQL MATCH/AGAINST behavior with implied DB-score sorting

This selector is only useful for database $pages->find() queries.
