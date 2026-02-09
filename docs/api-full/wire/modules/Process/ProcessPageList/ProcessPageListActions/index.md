# ProcessPageListActions

Source: `wire/modules/Process/ProcessPageList/ProcessPageListActions.php`

Inherits: `Wire`

## Summary

Actions manager for ProcessPageList

Common methods:
- [`setActionLabels()`](method-setactionlabels.md)
- [`setUseTrash()`](method-setusetrash.md)
- [`getActions()`](method-___getactions.md)
- [`getExtraActions()`](method-___getextraactions.md)
- [`processAction()`](method-___processaction.md)

Groups:
Group: [other](group-other.md)

## Methods
- [`setActionLabels(array $actionLabels)`](method-setactionlabels.md) Set action labels
- [`setUseTrash(bool $useTrash)`](method-setusetrash.md) Set whether or not to use trash
- [`getActions(Page $page): array`](method-___getactions.md) (hookable) Get an array of available Page actions, indexed by $label => $url
- [`getExtraActions(Page $page): array`](method-___getextraactions.md) (hookable) Get an array of available extra Page actions
- [`processAction(Page $page, string $action): array`](method-___processaction.md) (hookable) Process action
