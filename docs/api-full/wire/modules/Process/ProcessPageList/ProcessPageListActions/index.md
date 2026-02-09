# ProcessPageListActions

Source: `wire/modules/Process/ProcessPageList/ProcessPageListActions.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

Actions manager for ProcessPageList

Methods:
- [`setActionLabels(array $actionLabels)`](method-setactionlabels.md) Set action labels
- [`setUseTrash(bool $useTrash)`](method-setusetrash.md) Set whether or not to use trash
- [`getActions(Page $page): array`](method-___getactions.md) (hookable) Get an array of available Page actions, indexed by $label => $url
- [`getExtraActions(Page $page): array`](method-___getextraactions.md) (hookable) Get an array of available extra Page actions
- [`processAction(Page $page, string $action): array`](method-___processaction.md) (hookable) Process action
