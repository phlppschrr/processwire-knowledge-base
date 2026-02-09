# DatabaseQuerySelect: other

Source: `wire/core/DatabaseQuerySelect.php`

- [`$select: array`](method-select.md)
- [`$join: array`](method-join.md)
- [`$from: array`](method-from.md)
- [`$leftjoin: array`](method-leftjoin.md)
- [`$where: array`](method-where.md)
- [`$orderby: array`](method-orderby.md)
- [`$groupby: array`](method-groupby.md)
- [`$limit: array`](method-limit.md)
- `$comment: string` Comments for query
- [`select($sql, $params = array()): $this`](method-select.md)
- [`from($sql): $this`](method-from.md)
- [`join($sql, $params = array()): $this`](method-join.md)
- [`leftjoin($sql, $params = array()): $this`](method-leftjoin.md)
- [`where($sql, $params = array()): $this`](method-where.md)
- [`groupby($sql): $this`](method-groupby.md)
- [`limit($sql): $this`](method-limit.md)
- `$field: Field` Field object that is referenced by this query.
- `$group: string` Selector group (for OR-groups) if applicable.
- `$selector: Selector` Selector object referenced by this query.
- `$selectors: Selectors` Original selectors (all) that `$selector` is part of.
- `$parentQuery: DatabaseQuerySelect` Parent query object, if applicable.
