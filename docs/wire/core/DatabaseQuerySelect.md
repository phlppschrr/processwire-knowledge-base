# DatabaseQuerySelect

Source: `wire/core/DatabaseQuerySelect.php`

ProcessWire DatabaseQuerySelect

A wrapper for SELECT SQL queries.

The intention behind these classes is to have a query that can safely
be passed between methods and objects that add to it without knowledge
of what other methods/objects have done to it. It also means being able
to build a complex query without worrying about correct syntax placement.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com



Below are Properties populated by DatabaseQuerySelect objects created by PageFinder.
This is what gets passed to Fieldtype::getMatchQuery() method calls as properties
available from the $query argument.

## other

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

## __construct()

Setup the components of a SELECT query

## getQuery()

Return the resulting SQL ready for execution with the database

## orderby()

Add an ORDER BY section to the query

@param string|array $value

@param bool $prepend Should the value be prepended onto the existing value? default is to append rather than prepend.
	Note that $prepend is applicable only when you pass this method a string. $prepend is ignored if you pass an array.

@return $this

## getQuerySelect()

Get SELECT portion of SQL

@return string

## getQueryGroupby()

Get GROUP BY section of SQL

@return string

## getQueryLimit()

Get LIMIT section of SQL

@return string
