# ProcessWire 3.0.91 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.91-core-updates/

## Sections


## ProcessWire 3.0.91 core updates

9 February 2018 by Ryan Cramer [ 4 Comments](/blog/posts/processwire-3.0.91-core-updates/#comments)


## ProcessWire 3.0.91

This latest version on the dev branch continues resolving GitHub issue reports as the last few versions have done. A new page finding capability has been added as well, and that's what we'll focus on in this post. We didn't have a blog post last week for version 3.0.90, but instead had a short update in the forum, so if you missed that, check out [ProcessWire Weekly #195](https://weekly.pw/issue/195/) or this [forum post](https://processwire.com/talk/topic/18387-pw-3090-%E2%80%93-core-updates/).


### A new way of finding pages: by Fieldtype

When you use ProcessWire's API to find pages, you typically pass a selector string to a function like $pages->find(), $page->children(), or one of the others, to find pages matching the selector. For instance, `$pages->find("body%=coffee");` would return all pages containing a "body" field with the text "coffee" present somewhere in the text.

Lately I've had cases where I want to know if a value like "coffee" appears not just in a particular field like "body", but rather, whether it appears in any field that might have text in it. Of course, you can use OR fields in your selector, like `body|sidebar%=coffee`, which would search body and sidebar for coffee. But some sites I work on have a whole lot of fields and it's a bit cumbersome to track them all down for things like this. Not to mention, if I later add another field, I'd have to go back and update the selector.

In ProcessWire 3.0.91, you can now replace your usual usage of a field in a selector with the name of a Fieldtype. And in doing so, it's a shortcut that will search all fields using that Fieldtype. For instance, now I can search all of my Textarea fields at once for Coffee:

```php
$items = $pages->find("FieldtypeTextarea%=coffee");
```

In my case, that's returning pages containing the term "coffee" on fields: body, sidebar, summary, intro, meta_description, and whatever else I might have Textarea fields for.

You can specify multiple Fieldtypes too (just like with fields), by separating them with a pipe "|":

```php
$pages->find("FieldtypeTextarea|FieldtypeText|FieldtypePageTitle%=coffee");
```

Note that if you are using multi-language text fields, a search for any of the above Fieldtypes is also inclusive of the multi-language versions. So it's not necessary to specify something like FieldtypeTextLanguage separately, because it's already assumed if you specify FieldtypeText.

Now I'm a bit lazy and having to specify FieldtypeTextarea, FieldtypeText and FieldtypePageTitle is a bit more than I want to type still. So there's yet another useful shortcut. We can ask it to include any Fieldtype that extends another one. Since FieldtypeTextarea and FieldtypePageTitle extend FieldtypeText, we can ask it to include any fields that are FieldtypeText, *and* fields that *extend* FieldtypeText, by appending "extends" to the field portion of our query:

```php
$pages->find("FieldtypeText.extends%=coffee");
```

The above will find all pages containing "coffee" on any fields using FieldtypeText, FieldtypeTextarea, FieldtypePageTitle, or any other Fieldtype that extends FieldtypeText.

There's also another useful keyword we can append—"fields":

```php
$items = $pages->find("FieldtypeTextarea.fields");
```

When we include the "fields" keyword, it makes the page finder use a different method of finding the pages, and the resulting $items PageArray includes a data property "fields" that contains details about how many pages were found for each of the matching fields:

```
print_r($items->data('fields')); 

Array (
  [body] => 70
  [itinerary] => 48
  [sidebar] => 23
  [extra_notes] => 5
  [meta_description] => 2
  [intro] => 2
  [accommodations] => 1
  [climate_notes] => 1
  [editor_notes] => 1
  [summary] => 1
)
```

Now if we don't need the pages in $items and instead just want that array of info above, then there's no reason to load all the pages. So append a "limit=1" to your selector, which will speed it up, and still give you the same array of info:

```php
$items = $pages->find("FieldtypeText.fields, limit=1");
$info = $items->data('fields');
```

My examples in this post so far are all using Text fields, because they are the simplest way to introduce this feature. But this works for any Fieldtype. For instance, if I wanted to find all pages having any checkbox field with a checked value:

```php
$items = $pages->find("FieldtypeCheckbox=1");
```

Or maybe I want to find all pages having any Integer fields with a value greater than 0, including pages that are hidden or unpublished:

```php
$items = $pages->find("FieldtypeInteger>0, include=unpublished");
```

Or, maybe I want to find all pages referencing the current $page from any Page field (a very simple *related pages* feature):

```php
$items = $pages->find("FieldtypePage=$page");
```

Lets jump into something a bit more contrived, just to demonstrate something. Lets say I want to find any File fields (including Image fields, and anything else that extends File fields) that have a "description" mentioning the word "beer", and I want it to include a count of how many pages it found for each matching field:

```php
$items = $pages->find("FieldtypeFile.description.extends.fields%=beer");
```

Yes, the above is a more complicated example, but I figured we should have at least one like that just to demonstrate that you can search subfields, just like you can when using field names. While the optional "extends" and "fields" keywords aren't technically subfields, they can accompany subfields like this example demonstrates.

There are a few considerations to mention about this new feature:

First is that there is overhead in doing this—it still has to determine what all the matching fields are, and search them. Meaning, don't count on it to be particularly fast at larger scale. In testing here on a site with several thousand pages, and 7-10 fields matching the Fieldtype (including multi-language fields), my $pages->find() calls were coming in around 100 to 500 milliseconds, depending on how many pages were matched. That's reasonably fast still, but still something to keep in mind—this isn't going to be as fast a searching a single field.

If you've got a whole lot of fields matching a particular Fieldtype, you may run up against some limits on how much can be joined in a particular query. By using the "fields" keyword after the Fieldtype, as mentioned earlier (i.e. FieldtypeText.fields) it will make PageFinder determine the matching fields ahead of time, and only include the ones that will definitely match in the final query. This makes for maybe a 20% slower query, but one that can likely scale a lot further. So if you get an exception about too many database joins, you'll want to use the "fields" keyword. Of course, like mentioned earlier, using the "fields" keyword also makes it return some useful info in the returned PageArray's data.

In my testing on searching text fields here, I found that the %= (contains text like) performed a lot faster than the *= (contains phrase) or ~= (contains words) operators. This is likely due to a limitation on how indexes can be used in a query, so it's something to keep in mind—the %= operator seems to be a better fit when searching text Fieldtypes.

I've actually got another useful $pages->find() selector improvement to tell you about in the near future too, but we'll save that for another post. By the way, if you haven't stopped by our sites directory recently, you should, there's some really impressive sites in the [recent site submissions](https://processwire.com/about/sites/). Hope that you all have a great weekend and enjoy reading the [ProcessWire Weekly](http://weekly.pw)!
