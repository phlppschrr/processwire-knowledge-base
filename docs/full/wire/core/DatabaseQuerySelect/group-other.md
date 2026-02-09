# DatabaseQuerySelect: other

Source: `wire/core/DatabaseQuerySelect.php`

- $select: array

- $join: array

- $from: array

- $leftjoin: array

- $where: array

- [$orderby: array](method-orderby.md)

- $groupby: array

- $limit: array

- $comment: string Comments for query

- select($sql, $params = array(): $this )

- from($sql): $this

- join($sql, $params = array(): $this )

- leftjoin($sql, $params = array(): $this )

- where($sql, $params = array(): $this )

- groupby($sql): $this

- limit($sql): $this

- $field: Field Field object that is referenced by this query.

- $group: string Selector group (for OR-groups) if applicable.

- $selector: Selector Selector object referenced by this query.

- $selectors: Selectors Original selectors (all) that $selector is part of.

- $parentQuery: DatabaseQuerySelect Parent query object, if applicable.
