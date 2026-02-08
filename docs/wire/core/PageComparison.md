# PageComparison

Source: `wire/core/PageComparison.php`

ProcessWire Page Comparison

Provides implementation for Page comparison functions.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## is()

Is this page of the given type? (status, template, etc.)

@param Page $page

@param int|string|array|Selectors|Page|Template $status One of the following:
 - Status expressed as int (using Page::status* constants)
 - Status expressed as string/name, i.e. "hidden" (3.0.150+)
 - Template name, indicating page type
 - Page or Template object (3.0.150+)
 - Selector string or Selectors object that must match
 - Array of any of the above where all have to match (3.0.150+)

@return bool

## _if()

If value is available for $key return or call $yes condition (with optional $no condition)

This merges the capabilities of an if() statement, get() and getMarkup() methods in one,
plus some useful PW type-specific logic, providing a useful output shortcut.

See phpdoc in `Page::if()` for full details.

@param Page $page

@param string|bool|int $key Name of field to check, selector string to evaluate, or boolean/int to evalute

@param string|callable|mixed $yes If value for $key is present, return or call this

@param string|callable|mixed $no If value for $key is empty, return or call this

@return mixed|string|bool

@since 3.0.126

## matches()

Given a Selectors object or a selector string, return whether this Page matches it

@param Page $page

@param string|array|Selectors $s

@param array $options Options to modify behavior (3.0.225+ only):
 - `useDatabase` (bool|null): Use database for matching rather than in-memory? (default=false)

@return bool

## selectorMatches()

Return whether individual Selector object matches Page

@param Page $page

@param Selector $selector

@return bool

@since 3.0.231

## selectorMatchesProperty()

Return whether single property from individual Selector matches Page

@param Page $page

@param Selector $selector

@param string $property

@return bool

@since 3.0.231

## getObjectValueArray()

Given an object, return the value(s) it represents (optionally from a property in the object)

This method is setup for the matches() method above this. It will go recursive when given a property
that resolves to another object.

@param Wire|object $object

@param string $property Optional property to pull from object (may also be property.subproperty, and so on)

@return array Always returns an array, which may be empty or populated

## isEqual()

Is $value1 equal to $value2?

@param string $key Name of the key that triggered the check (see WireData::set)

@param mixed $value1

@param mixed $value2

@return bool
