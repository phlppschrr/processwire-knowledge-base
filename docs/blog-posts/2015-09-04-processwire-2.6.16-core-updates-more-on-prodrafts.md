# ProcessWire 2.6.16 core updates + ProDrafts Q&A

Source: https://processwire.com/blog/posts/processwire-2.6.16-core-updates-more-on-prodrafts/

## Sections


## ProcessWire 2.6.16 core updates + ProDrafts Q&A

4 September 2015 by Ryan Cramer [ 11 Comments](/blog/posts/processwire-2.6.16-core-updates-more-on-prodrafts/#comments)


## ProcessWire 2.6.16

This week we've got some handy new additions to the core and other tweaks that I think you'll like. We've also got more details about ProDrafts along with some Q&A. Hope you all have a great weekend and week, and hope to see you Saturday morning at [weekly.pw](http://weekly.pw).


### New system "published" date/time property now available on all pages

This week brought a schema change to the pages table which adds a "published" date/time property alongside the existing "created" and "modified" system date/time properties. It works exactly the same as those existing properties except that it represents the date/time the page was published, which may be different from the date/time the page was created or modified.

Why was this needed? Because the "created" property currently gets used for a lot of situations where you really want a "published" property. Take this blog post for example, which shows a date in the top right corner. I might start working on a post a few days before I publish it. If I was using the created date, it would show the end of August rather than the beginning of September. So I have to maintain my own separate/custom date field for this purpose, and manually set it to the proper date.

The above is just an example, but the utility of having a separate published date goes far beyond that example. It can be useful when sorting results of a `$pages->find()` or `$page->children()` operation, outputting RSS feeds, searching pages in Lister, or keeping track of pages in the upcoming ProDrafts module. All in all, it seemed like maintaining a separate published property for all pages was a good idea.

Here's the catch: we don't know when your existing pages were published, because we've not tracked that information before. So when the PW SystemUpdater module runs after you upgrade to 2.6.16, it'll make a best guess by populating the created date for the published date. That means that unless you are building a new site, the published date is more likely to be useful to you in the future than it is right now.

Having a standardized published date also will be helpful to 3rd party modules, which can now make use of the information. For instance, an RSS feed generator module would now have a proper date to use for the RSS `pubDate` property, where it didn't before.

*Warning: if you already have created a field in your site named "published", you'll want to rename it (and update any code referencing it), preferably before upgrading to PW 2.6.16. Though PW 2.6.16 will detect if you have a field with that name and warn you about it too. Hopefully there will be few or no instances where people already have a field with this name, but wanted to mention it just in case. *

How do you access the published property from the API? It works the same as the existing created and modified properties:

```
$unixTimestamp = $page->published; 
$dateString = $page->publishedStr;
```


### Page fields now support custom format labels

Page fields are one of the most common types of fields used in ProcessWire. Any given page might have several fields on it, but you could only make use of one of them for your selectable labels (most commonly "title"). This led to development of the [FieldtypeConcat](http://modules.processwire.com/modules/fieldtype-concat/) module, which provided runtime concatenation of multiple fields, but was also kind of a painful and kludgy workaround for such a simple thing. Having to maintain a separate field just to get the selectable label you wanted never felt quite right.

ProcessWire 2.6.16 adds the ability to specify a custom format for your page labels. This not only enables you to have page labels containing multiple fields from each page, but also gives you the ability to format them the way you want with regard to spacing, punctuation and other characters. Further, you can access properties of other Page fields, like `{parent.title}` or output only the first matching field, like `{headline|title}`.

To use a custom page label, edit any Page field, and click the "Input" tab. Locate the "Page label field" input, and then select "Custom format (multiple fields)". A new "Custom page label format" field is revealed, where you can enter your custom format.

As an example, lets say that I had a "related_products" Page field where I wanted to select products related to the current page. Rather than just showing the product title, I instead want to show the product manufacturer (Apple), product title (Macbook Pro), year (2015) and price ($1200), like this:

```
Apple: Macbook Pro (2015), $1200
```

My custom page label format would be this:

```
{manufacturer.title}: {title} ({year}), ${price}
```

These custom labels will work with any core Page selection Inputfield, and will likely work with most 3rd party ones as well (though there may be exceptions). We had to jump through a few hoops to make this possible in a safe manner with the PageAutocomplete and PageListSelect Inputfields (which pull selectable page data from ajax requests), but we got there, and so we should have 100% core support for this feature now. Please let us know how it works for you.


### AsmSelect gets new option to edit selected pages

When using AsmSelect with a Page field, you now have the option of making the selected labels clickable to open a modal window to the Page editor for that page.

To enable the option, just edit any Page field using AsmSelect, click the "Input" tab and see the new toggle at the bottom that enables you to turn this on or off.

This one came in as a request by a few in the community awhile back, so thanks to those that came up with this good idea.


### ProDrafts Q&A

A couple of weeks ago I wrote quite a bit [about the new ProDrafts module](/blog/posts/processwire-2.6.13-and-a-preview-of-prodrafts/). Since that time, several questions have come up, and the scope of the project has increased a bit as well. So I just wanted to keep you up to date and hopefully answer some of your questions along the way.


### When will ProDrafts be available?

Currently we're aiming for about a month from now, in October. Though the date is not yet fixed. It may be available for testing before that though.


### What version(s) of ProcessWire will ProDrafts support?

The minimum supported version will be ProcessWire 2.6.1 (the current master branch). However, several features will only work if paired with the current ProcessWire dev branch. We're getting close to converting the current dev branch to becoming the current master, which will be ProcessWire 2.7. ProDrafts will likely be released before ProcessWire 2.7, but getting PW 2.7 to be the new master/stable version will be the main focus once the first version of ProDrafts is out.


### Will ProDrafts support versioning of pages?

Yes. Originally the plan was that the first version of ProDrafts would not have full versioning support, but that it would be added at some point in the future. Because there have been a few requests for it already, I've decide to go ahead and add it in the first version of ProDrafts.

Though, as the name suggests, the primary focus of ProDrafts is drafts. We already have Teppo's great versioning module, so felt drafts needed to be the focus of this module. That being said, we're going to have great versioning support in ProDrafts, but entirely different from what you get in Teppo's module.

Here's a screenshot showing the versions field (on the Settings) tab in the page editor:


### How will versioning work?

Whenever you publish a page, a new version is saved. Whereas when working on a draft, versions are not saved. So you can edit and save a draft as much as you'd like, but a version won't be saved until you publish it. When you do publish, the version it saves is the page in the previous state (before you published). This enables you to revert back to the page in any previously published state.

ProDrafts versions are entire copies of the page, including all files that go along with it. That enables them to be restored in full, independent of what happens in any other versions. Unlike Teppo's version module, ProDrafts doesn't version fields individually, nor does it keep versions of unpublished changes. Teppo's module will still provide more granular version control than ProDrafts.


### How are drafts and versions stored?

Drafts and versions are actually not stored as pages, so they do not live in the pages table or consume space in fields. Drafts and versions are stored in a separate ProDrafts table, which isn't loaded unless a draft or version is requested from the API. When one is requested, ProDrafts clones the page in memory and then populates it with all the data from the draft or version. The currently published page never exists in the database with the draft or version data in it, unless you decide to publish the draft/version. Files for drafts or versions are stored in separate directories from a page's main files directory.


### Will ProDrafts work with all field types?

It will work with all field types that I'm aware of, except for PageTable and Repeater. The reason it won't work with those two field types is because they consist of independent pages. The pages in those fields would have to have their own drafts and/or versions recorded separately. So it's entirely possible that ProDrafts will be able to support them in the near future, but version 1 will not have support for them. All other field types are supported, including files/images, all the other core Fieldtypes, ProFields, and everything else I've tried it with.


### How are PageTable and Repeater handled?

PageTable and Repeater can be edited when a page is in an unpublished state (i.e. doesn't appear on the front-end). But as soon as you are editing a draft of an already-published page, a warning is provided next to PageTable and Repeater fields that indicates changes to them will publish immediately. If a user doesn't have page-publish permission, then they won't be able to edit PageTable and Repeater fields except when a page is in an unpublished state. Though that's already the case now even without ProDrafts, as a user without page-publish (on a system that has this permission) cannot edit any part of a published page. So ProDrafts actually opens a lot more options here in that users without page-publish permission can still edit all other field types in a draft, even if a page is already published–they just can't publish them.


### Can you maintain multiple drafts of the same page?

The draft serves as the single staging ground for unpublished changes. There is just one draft allowed per page. Though there can be any number of versions per page.


### Can pages with drafts and/or versions be identified in the PageList, Lister and API?

Yes, pages with drafts and/or versions update the page's status flags to indicate that. This makes it possible to pull (for example) all pages with drafts, or all pages with versions quickly from Lister and/or the API. This is also how we show special icons next to draft pages in PageList and Lister.


### Can drafts and/or versions have their fields independently queried from the API?

Drafts and versions are stored in an encoded/condensed format so that they aren't taking up any of your pages namespace or filling up your field_* tables. That means they are not accessible to page finding operations in the ProcessWire API. So you can't for instance perform a $pages->find() operation that would locate a page that has a title containing the word "ProcessWire" in the draft only. However, you can easily find all pages that have a draft and/or version, and you can easily access the draft and/or versions data from the API once you have a $page for context.


### How do you access a draft or version from the API?

Calling `$page->draft()` on any page will return a ProDraft object with various API functions. And calling `$page->draft->page()` will return a copy of $page, but containing the draft version of it. You can also iterate `$page->versions()` to get all versions of the page (which are also ProDraft objects) and likewise call the page() method on any one of them to get a copy of the $page in that version. I'll get into more details on the API side in future posts as well.

If you have any additional questions about ProDrafts, please use the comments section below. Thanks for your interest!
