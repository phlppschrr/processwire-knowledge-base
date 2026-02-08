# DatabaseQuerySelect: other

Source: `wire/core/DatabaseQuerySelect.php`

@property array $select

@property array $join

@property array $from

@property array $leftjoin

@property array $where

@property array $orderby

@property array $groupby

@property array $limit

@property string $comment Comments for query

@method $this select($sql, $params = array())

@method $this from($sql)

@method $this join($sql, $params = array())

@method $this leftjoin($sql, $params = array())

@method $this where($sql, $params = array())

@method $this groupby($sql)

@method $this limit($sql)

@property Field $field Field object that is referenced by this query.

@property string $group Selector group (for OR-groups) if applicable.

@property Selector $selector Selector object referenced by this query.

@property Selectors $selectors Original selectors (all) that $selector is part of.

@property DatabaseQuerySelect $parentQuery Parent query object, if applicable.
