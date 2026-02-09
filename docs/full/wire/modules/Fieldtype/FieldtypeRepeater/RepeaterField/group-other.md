# RepeaterField: other

Source: `wire/modules/Fieldtype/FieldtypeRepeater/RepeaterField.php`

- $type: FieldtypeRepeater
- $parent_id: int Parent page ID for repeater items.
- $template_id: int Template ID used by repeater items.
- $repeaterFields: array Array of field IDs used in repeater.
- $repeaterMaxItems: int Maximum number of items allowed.
- $repeaterMinItems: int Minimum number of items allowed.
- $repeaterDepth: int|string Max allowed depth for repeater items.
- $familyFriendly: bool|int Use family friendly depth? Maintains expected parent/child relationships.
- $repeaterLoading: int Dynamic loading (ajax) in editor, see `FieldypeRepeater::loading*` constants.
- $repeaterCollapse: int Item collapse state, see `FieldtypeRepeater::collapse*` constants
- $repeaterAddLabel: string Label to use for adding new items.
- $repeaterTitle: string Field name to use for repeater item labels or format string with {fields}.
- $rememberOpen: int|bool Remember which items are open between requests?
- $accordionMode: int|bool Use accordion mode where only 1 item open at a time?
- $lazyParents: int|bool Avoid creating parents when there are no items to store?
- $repeaterReadyItems: int (deprecated)
