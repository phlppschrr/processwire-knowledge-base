# ProcessWire 3.0.107 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.107-core-updates/

## Sections


## ProcessWire 3.0.107 core updates

29 June 2018 by Ryan Cramer [ 2 Comments](/blog/posts/processwire-3.0.107-core-updates/#comments)


## ProcessWire 3.0.107 core updates

This week we've got a lot of updates on our core dev branch, including new features, issue resolutions and more. For starters, we've added support for making the Trash and Restore features available to non-superusers, along with related improvements. Plus we've got several new useful and interesting page traversal methods and properties added to our $page API.


### Trash for all

In all versions of ProcessWire up till now, the Trash item (in the PageList) has only been available to the superuser. When an editor would delete a page, it would go into the trash, but they wouldn't be able to see it there or restore it. That was always a job for superuser. But in ProcessWire 3.0.107, now you can optionally make Trash available to non-superusers. To enable it, to go Modules > Configure > ProcessPageList, and click the checkbox at the top to “Allow non-superuser editors to use Trash?”

Once enabled, non-superuser users that have “page-delete” permission somewhere will now see a Trash item in their page list. However, they will only see pages in the trash that they have delete permission to (and thus restore permission). Meaning, they can only see pages in the trash that they would have been able to place there (or restore from there) in the first place. So the Trash is still quite access protected (a good thing), and if you want to make it available to non-superusers, now you can.

Beyond just showing the Trash item in the page list, enabling it for non-superusers also enables them to use the “Trash” and “Restore” page list actions. Those are the little actions that appear when you hover over a page in the page list, and you click the ">" item to reveal more actions.


### Dumpster dive assistant

Want to get something out of the Trash? ProcessWire 3.0.107 also adds a new “Restore” tab, visible when editing a page that is in the trash. This tab works much like the Delete tab, and it contains a checkbox that you can check to restore the page to its original location. This tab also tells you where it's going to restore the page to. Previously, the Restore option has only been available from the Page List as one of the hover actions, and the location it would be restored to was not available.


### What pages point to this one?

Have you ever wondered what other pages are referencing another, either with Page reference fields, or href links in textarea/HTML fields? Now this information is built-in to the page editor and is available on the Settings tab in the field labeled “What pages point to this one?”

The information shown in this field is rendered on-demand, so like some other fields in the page editor, it won't be loaded until you actually click the field to open it. This ensures it doesn't add any overhead in the page editor. Once opened, it shows you a combination of two new Page API methods added this week: $page->references() and $page->links(). For more details about these, see the reference later in this blog post.


## New Page API methods


### $page->restorable()

This accompanies the existing `$page->trashable()` method and it returns a boolean indicating whether or not the Page it was called from can be restored from the trash to its original location, by the current user. This was added to support the other trashy features added this week.

```
if($page->restorable()) {
  // page is in the trash, and is restorable to its original location
} else if($page->isTrash()) {
  // page is in the trash, but is not restorable either due to access
  // or perhaps the parent is no longer present
} else {
  // page is not restorable because it is not in the trash
}
```


### $page->references()

This new method returns a PageArray of all pages referencing the one it was called from, in Page fields. It optionally accepts $selector and $field arguments.

The `$selector` argument (1) enables you to specify a selector string to filter the results. By default, results are like those from $page->children() or $pages->find(), so if you want it to also include hidden and unpublished pages, you'll want to specify an "include=unpublished" or "include=all" as your selector. There's also a shortcut, in that you can specify boolean true and "include=all" will be assumed.

The `$field` argument (2) lets you specify that you only want it to include results from a particular Page field, rather than all Page fields. Or you can specify boolean true to make the references() method return an array of PageArray objects where each is indexed by field name—this enables you to easily identify not just what pages are referencing your $page, but also from what fields.

The references() method is hookable so that the definition of what it represents can be expanded by modules and hooks.

```
// get all visible pages referencing this page
$items1 = $page->references();

// get visible pages and hidden pages referencing this page
$items2 = $page->references("include=hidden");

// get all pages referencing this, shortcut for "include=all"
$items3 = $page->references(true);

// get pages referencing this in field "cats", sort by title
$items4 = $page->references("sort=title", "cats");

// get an array of PageArray objects indexed by field name
$array = $page->references(true, true);
```

**Related properties:**

- `$page->references;` Same as a call to $page->references() with no arguments.
- `$page->referencing; `Get PageArray of outbound page references on $page.
- `$page->numReferences;` Get quantity of inbound references, no exclusions.
- `$page->hasReferences;` Get quantity of inbound references visible to $user.


### $page->links()

This method works very much like the references() method mentioned above, except that it returns pages that are linking to $page with `<a href="…">` links. It searches all Textarea fields that have an HTML content-type, and that have link abstraction enabled in their HTML options. Most commonly, this would be your CKEditor fields.

The links() method also accepts $selector and $field arguments like the references() method does, and they work exactly the same, with one exception: the $field argument doesn't have the boolean option. Like the references() method, this links() method is also hookable so that modules can expand upon the definition of what is included in the return value.

```
$links = $page->links(); 
if($links->count()) {
  echo "<h3>You might also like:</h3>";
  echo $links->each("<li><a href={url}>{title}</a></li>");
}
```

**Related properties:**

- `$page->links;` Same as a call to $page->links() with no arguments.
- `$page->numLinks;` Get quantity of inbound links with no exclusions.
- `$page->hasLinks;` Get quantity of inbound links visible to $user.


### $page->urls()

This method returns an array of all URLs that the page is accessible from. You might be wondering: how is a page accessible from more than one URL? There are a couple of cases that this method covers: First is multi-language—the return value includes URLs for the page in all languages it is enabled for, and the returned array is indexed by language name.

Next are URLs that the page was previously available at (past URLs, which would 301 redirect to the current URL), whether due to page movements or changes to the page name over time. So the urls() return value also includes past URLs of the page it was called from, and in any language. Past URLs are indexed by last date that they were available at that URL (ISO-8601 date format). You can optionally specify an $options argument to this method in order to limit what it returns.

There were also some other core updates this week, including a few issue resolutions, new $modules->getModuleInfoProperty() method, new lazy-loading option for WireInput, and more. But these are more internal use things that aren't likely to interesting here, but if you are interested, see the [commit log](https://github.com/processwire/processwire/commits/dev). Thanks for reading and be sure to check out the [ProcessWire Weekly](http://weekly.pw) while you enjoy your weekend as well.
