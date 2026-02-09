# New paginated Fieldtype support and FieldtypeTable upgrades

Source: https://processwire.com/blog/posts/fieldtype-pagination/

## Sections


## New paginated Fieldtypes & Table field upgrades

15 July 2016 by Ryan Cramer [ 8 Comments](/blog/posts/fieldtype-pagination/#comments)

There's been a lot of work done in the core this week in order to make paginated Fieldtypes a reality. Not sure what that means? Don't worry, we'll cover it below. It's not quite ready for you to use just yet, so we won't bump the core version this week, but wanted to give you a look at how it's coming together. In this post, we'll be looking at the Table field ([ProFields Table](/api/modules/profields/table/)) as the first example. However, because it's being added as a core capability, it's likely we'll be supporting the same in other Fieldtypes like Repeater, [Repeater Matrix](/api/modules/profields/repeater-matrix/), PageTable, [Multiplier](/api/modules/profields/multiplier/), Files and Images.


## Paginated Fieldtypes


### What are they and why would I want them?

In ProcessWire you may be familiar with the concept of [pagination of Page objects](/api/modules/markup-pager-nav/), which is quite a common scenario. But something we've not had before is pagination of content within actual fields. Take a files field as an example – it's unlikely you'd want to have a thousand files in a files field, because it would be too slow to load, and might consume too much memory. Basically, the management of multi-value fields is one area where ProcessWire has not been as scalable as it could be. But now that's changed!


### Example: ProFields Table

The place where this limitation has been felt the most (and place I've heard about it the most from others) is with regard to the [ProFields Table field](/api/modules/profields/table/). The Table field opens all kind of cool possibilities, people get excited, and [understandably] start loading thousands of rows into a table. But then they discover that you can't reasonably edit that much data in a single page editing environment. Nor would you want to load/output that much data on the front end. Up until this week, you really didn't have a choice, because the loading (and saving) of multi-value fields was an all-or-nothing affair. No longer!

Because ProFields Table field is the one where this need has come up the most, I've focused on that first. But what applies to the Table field can potentially apply to any multi-value field in ProcessWire where support is deemed useful. It does take a little bit of code to support it, but we're trying to keep as much of that in the core (FieldtypeMulti) as possible, reducing the requirements on modules that will support it.


### Screencast

Below is a short screencast that demonstrates what pagination brings to field loading. Here is a Table field I created called "subscribers". It has ~41000 rows in it, containing a list of subscribers. This would not have been possible without pagination. In fact, even 1000 rows would have been too much. Now there is literally no limit to the number of rows you can support in a Table field!

When you've got that much data, you need more than just pagination. You need to be able to apply custom sorting (by clicking the column headlines), and be able to the filter the rows. The screencast above demonstrates these features.


### Pagination requirements

When you are working with enough data to need pagination, you are no longer in the territory of manual drag-n-drop sorting of records. This is where things get different from what you may be used to, because just about all multi-value fields in ProcessWire are always managed in a drag-n-drop manner. That's convenient at small scale, but not at all convenient when you are dealing with large scale data. So when you use pagination with a multi-value field, ProcessWire requires that you select one or more default sorts so that it knows how to order the items:

The above screenshot is something that our Field editor automatically adds to Fieldtypes that support pagination (Setup > Fields > field > Details tab).


### How it works on the API side

On a paginated field, when you request the value from a Page, like `$page->subscribers`, ProcessWire gives you a [WireArray](../api-full/wire/core/WireArray/index.md) (or whatever type is used) containing the number of items you've defined for pagination (see screenshot above). The actual pagination that is loaded corresponds to to the current page number of the request (aka [$input->pageNum](../api-full/wire/core/WireInput/method-pagenum.md)). So if the URL was /products/page4 then you'd get the 4th pagination of items when you access the field from a $page.

The point to take from this is that field pagination is just as easy to work with as it is to work with a paginated pages (PageArray). In fact, all the methodology and API calls are identical, so there's nothing new to learn here. Both derive from [PaginatedArray](../api-full/wire/core/PaginatedArray/index.md) objects and implement the *WirePaginatable* interface.


### API-side loading, sorting and filtering

What if you want something different than the current pagination of “subscribers”? Or what if you want to filter the items so that you only get items matching a certain criteria? This is where it gets even more fun! If your field is named “subscribers” for instance, then you'd usually access it as `$page->subscribers`, right? If you want to filter, then access that field as a **method call** instead, i.e. `$page->subscribers(…)`, and pass in a selector as the argument to it. Below are a few examples.

```php
// First lets get a page with lots of subscribers
$p = $pages->findOne("subscribers.count>1000");

// Get 20 items (assuming that is predefined limit)
$items = $p->subscribers;

// Get 50 items, rather than the predefined limit
$items = $p->subscribers("limit=50");

// Get 50 items sorted by birthday
$items = $p->subscribers("limit=50, sort=birthday");

// Get items with first_name "Hanna" and ".edu" in email
$items = $p->subscribers("first_name=Hanna, email%=.edu");

// Get 20 items, sorted last_name, first_name, birthday (reverse)
$p->subscribers("sort=last_name, sort=first_name, sort=-birthday");
```

Note that “subscribers” is just an example of a field name, and it could be anything.

The selectors are identical to those that you would use when finding pages. Only in this case, you aren't finding pages – you are finding items in a field on a page! I'm particularly excited about this upgrade because I think it really takes ProcessWire's scalability to the next level.


### When can you start using this?

I'd hoped to have the Table field updates wrapped up this week, and actually they are. But because there's so much work behind it, I want to do more quality assurance and testing here before I post it in the ProFields board. Because much of the actual code to support it is in the core, this particular upgrade will require ProcessWire core version 3.0.26 or 2.8.26. If all goes well, we should have the Table field update posted for you to download within the next week or so.

After finalizing the Table field updates, we'll likely focus on similar support for either Repeater/RepeaterMatrix, File/Image fields, or maybe there is some other common need for this–feedback is appreciated. Eventually we hope to cover them all.


### Other questions that may arise


### How do you add that much data into a Table field?

Adrian has written a [module](/talk/topic/7905-profields-table-csv-importer-exporter/) that can import data into a Table field from CSV. I've not yet had the opportunity to test it with the latest version of Table, but presumably it should continue to be a good solution.

The Table field also now comes with an API-side solution as well. Given a CSV file with a header row that matches the names of the table columns, it'll import them all to your table with a single API call. This is what I used to import that list of subscribers:

```
$page->subscribers->importCSV('/path/to/file.csv');
```


### How do you delete that much data from a Table field?

On the interactive side, the Table field now supports the double-click to select all items for deletion (just like in file and image fields). In the screencast above you saw that with 40k+ items, I had a few thousand paginations worth of data... not something you'd want to delete pagination-by-pagination. So when you double-click a row to select all, you also get an option to select all rows from all paginations for deletion. This screenshot demonstrates it best:

Hope that you all have a great weekend and enjoy the [ProcessWire Weekly](http://weekly.pw)!
