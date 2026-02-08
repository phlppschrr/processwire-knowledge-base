# Unknown

Source: https://processwire.com/docs/selectors/

Selectors are simple strings of text that specify fields and values. These selectors are used throughout ProcessWire to find pages (and other types of data).

For example, `name=karena` is a simple selector that says: “find items that have the name karena.” Selectors in ProcessWire are loosely based around the idea and syntax of attribute selectors in jQuery.

- [The components of a selector](#components)
- [Where do you use selectors?](#where)
- [Selector fields](#fields)
- [Selector operators](#operators)
- [Selector values](#values)
- [Specifying multiple selectors](#multiple)
- [OR selectors: matching one value or another](#or-selectors1)
- [OR selectors, matching one field or another](#or-selectors2)
- [AND selectors: matching more than one value in the same field](#and-selectors)
- [OR-groups: matching one group of selectors or another](#or-groups)
- [Sub-selectors: selectors within selectors](#sub-selectors)
- [Sorting the results of a selector](#sort)
- [Limiting the number of results returned by a selector](#limit)
- [Count selectors – finding matches by quantity](#count)
- [Subfield selectors](#subfield)
- [Owner selectors](#owner-selectors)
- [Finding pages that use specific templates](#finding1)
- [Finding pages that have specific parents or ancestors](#finding2)
- [Matching different subfields from the same (1) row in a multi-value field](#match-same-row)
- [Access control in selectors](#access_control)
- [API variables in stored selectors](#api-variables-in-selectors)
- [Sanitizing user input in selectors](#sanitizing)
- [Examples of selectors as used in page templates](#examples)

### []()The components of a selector

An individual selector consists of three parts: the field you are looking for, an operator (like an equals '=' sign), and the value you want to match. For example, a basic selector might be:

```
title=products
```

In this example, "title" is the field, the equals sign "=" is the operator, and "products" is the value you want to match. This basic selector would match all pages having a title field of "products", regardless of where they exist in the site. You may also specify multiple selectors by separating each with a comma.

### []()Where do you use selectors?

Selectors are used throughout ProcessWire, typically for getting and finding pages with the [$page](/docs/start/variables/page/) and [$pages](/docs/start/variables/pages/) variables. Below is a list of the most common functions where selectors are used:

```
$pages->find("selector"); 
$pages->get("selector, path or ID");
$page->children("selector");
$page->siblings("selector");
$page->find("selector");
```

Any function that accepts a selector will accept multiple selectors split by a comma.

While you are less likely to use them, most of the other utility objects in ProcessWire, all of the array types, and several field types also accept selectors:

```
$matches = $templates->find("selector"); 
$matches = $users->find("selector");
$matches = $fields->find("selector");
$matches = $page->images->find("selector")->not("selector");
// ...and so on...
```

Below we examine the 3 parts of a selector in more detail: fields, operators and values.

### []()Selector fields

The field portion of a selector may refer to any field of a page. If you want to know what fields you can use for matching, see "Setup > Fields" in your ProcessWire admin. All custom fields are typically optimized for fast matches.

If you want to match a value in one field or another, you may specify multiple fields separated by a pipe "|" symbol, i.e.

```
title|name|headline=products
```

Using the above syntax, the selector will match any pages that have a title, name, or headline field of "products" or "Products". Selector values are not case sensitive unless you configure your MySQL with a case sensitive collation.

### []()Selector operators

The [operator](/docs/selectors/operators/) portion of a selector may be one of the following:

``[/docs/selectors/operators/#equal](/docs/selectors/operators/#equal)``[/docs/selectors/operators/#not-equal](/docs/selectors/operators/#not-equal)``[/docs/selectors/operators/#less-than](/docs/selectors/operators/#less-than)``[/docs/selectors/operators/#greater-than](/docs/selectors/operators/#greater-than)``[/docs/selectors/operators/#less-than-equal](/docs/selectors/operators/#less-than-equal)``[/docs/selectors/operators/#greater-than-equal](/docs/selectors/operators/#greater-than-equal)``[/docs/selectors/operators/#contains](/docs/selectors/operators/#contains)``[/docs/selectors/operators/#contains-words](/docs/selectors/operators/#contains-words)``[/docs/selectors/operators/#contains-like](/docs/selectors/operators/#contains-like)``[/docs/selectors/operators/#starts](/docs/selectors/operators/#starts)``[/docs/selectors/operators/#ends](/docs/selectors/operators/#ends)``[#starts-like](#starts-like)``[#ends-like](#ends-like)``[/docs/selectors/operators/#contains-advanced](/docs/selectors/operators/#contains-advanced)``[/docs/selectors/operators/#contains-expand](/docs/selectors/operators/#contains-expand)``[/docs/selectors/operators/#contains-words-partial](/docs/selectors/operators/#contains-words-partial)``[/docs/selectors/operators/#contains-words-live](/docs/selectors/operators/#contains-words-live)``[/docs/selectors/operators/#contains-words-like](/docs/selectors/operators/#contains-words-like)``[/docs/selectors/operators/#contains-words-expand](/docs/selectors/operators/#contains-words-expand)``[/docs/selectors/operators/#contains-any-words](/docs/selectors/operators/#contains-any-words)``[/docs/selectors/operators/#contains-any-words-partial](/docs/selectors/operators/#contains-any-words-partial)``[/docs/selectors/operators/#contains-any-words-like](/docs/selectors/operators/#contains-any-words-like)``[/docs/selectors/operators/#contains-any-words-expand](/docs/selectors/operators/#contains-any-words-expand)``[/docs/selectors/operators/#contains-match](/docs/selectors/operators/#contains-match)``[/docs/selectors/operators/#contains-match-expand](/docs/selectors/operators/#contains-match-expand)``[/docs/selectors/operators/#bitwise-and](/docs/selectors/operators/#bitwise-and)[/docs/selectors/operators/#general-operators](/docs/selectors/operators/#general-operators)[/docs/selectors/operators/#phrase-matching-operators](/docs/selectors/operators/#phrase-matching-operators)[/docs/selectors/operators/#word-matching-operators](/docs/selectors/operators/#word-matching-operators)[/docs/selectors/operators/#using-more-than-one-operator-at-a-time](/docs/selectors/operators/#using-more-than-one-operator-at-a-time)```

``````

``````

```````[http://dev.mysql.com/doc/refman/5.5/en/fulltext-stopwords.html](http://dev.mysql.com/doc/refman/5.5/en/fulltext-stopwords.html)````````[http://dev.mysql.com/doc/refman/5.1/en/fulltext-fine-tuning.html](http://dev.mysql.com/doc/refman/5.1/en/fulltext-fine-tuning.html)[http://dev.mysql.com/doc/refman/5.5/en/fulltext-stopwords.html](http://dev.mysql.com/doc/refman/5.5/en/fulltext-stopwords.html)```````````````````

``````

```### []()```

```[/api/ref/sanitizer/selector-value/](/api/ref/sanitizer/selector-value/)### []()```

```### []()```

```### []()```

```### []()```

```### []()```

``````

```

```

```### []()```

``````

`````#### [/blog/posts/processwire-3.0.6-brings-pages-upgrades-and-link-abstraction/#improvements-to-sub-selectors](/blog/posts/processwire-3.0.6-brings-pages-upgrades-and-link-abstraction/#improvements-to-sub-selectors)```

```### []()```

``````

``````

```````#### ``````````````````#### ````````### []()```

``````

```### []()`````

``````

```### []()[/blog/categories/repeaters/](/blog/categories/repeaters/)[/docs/modules/guides/comments/](/docs/modules/guides/comments/)```

``````

``````

``````

```[#match-same-row](#match-same-row)### []()[/blog/posts/processwire-3.0.95-core-updates/#owner-selectors](/blog/posts/processwire-3.0.95-core-updates/#owner-selectors)### []()```

``````

```### []()```

``````

``````

``````

``````

``````

```### []()```

````````

````````


```### []()[/api/ref/page-array/](/api/ref/page-array/)````- ``- ``- ``- `````

```[/api/ref/pages/get/](/api/ref/pages/get/)``[/api/ref/pages/find-one/](/api/ref/pages/find-one/)- ``- ``- ``### []()`````````````````````

```````````### []()```

```[/docs/start/variables/sanitizer/](/docs/start/variables/sanitizer/)[/api/ref/sanitizer/selector-value/](/api/ref/sanitizer/selector-value/)```

```[/api/ref/sanitizer/selector-field/](/api/ref/sanitizer/selector-field/)```

```### []()```

``````

``````

``````

``````

``````

``````

```- #### [/docs/selectors/operators/](/docs/selectors/operators/)- [/docs/selectors/](/docs/selectors/)- [/docs/selectors/operators/](/docs/selectors/operators/)- [/docs/](/docs/)- [/api/ref/](/api/ref/)- [/docs/start/](/docs/start/)- [/docs/front-end/](/docs/front-end/)- [/docs/tutorials/](/docs/tutorials/)- [/docs/selectors/](/docs/selectors/)- [/docs/modules/](/docs/modules/)- [/docs/fields/](/docs/fields/)- [/docs/user-access/](/docs/user-access/)- [/docs/security/](/docs/security/)- [/docs/multi-language-support/](/docs/multi-language-support/)- [/docs/more/](/docs/more/)
