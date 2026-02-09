# A look at upcoming page export/import functions

Source: https://processwire.com/blog/posts/a-look-at-upcoming-page-export-import-functions/

## Sections


## A look at upcoming page export/import functions

16 June 2017 by Ryan Cramer [ 5 Comments](/blog/posts/a-look-at-upcoming-page-export-import-functions/#comments)


## ProcessWire 3.0.64

Last week I was out of town, and this week I came back to multiple client projects in progress. In one case, developing a login, authentication and download system for an existing ProcessWire powered site in Sweden. In another, developing a custom module for managing Facebook logins, pulling data from Facebook, and connecting them with ProcessWire accounts for a company in the Caribbean. And in yet another case, working on developing a rather complex website on a very short timeline, using Markup Regions for the first time on a client project (and thrilled how much they've simplified development). All of this is to say, I've been in ProcessWire the entire week, actually using it (my favorite tool) more than building it. Nevertheless, we've got a new core version for you, 3.0.64, which contains a few minor fixes and continues progress on our page import/export functions, which we'll talk a bit more about in this post.


### A closer look at page export/import

I mentioned page export/import as one of the current projects in a post a few weeks back. A couple of weeks ago, the ProcessWire Weekly did a [poll](http://weekly.pw/polls/) about what features you are most interested in. I noticed that the page export/import functions led the interest in the poll. I've also had a few people email me asking about it. So it's clear there's strong interest here, and it's probably the core project that deserves the most attention in the short term. I'm glad about that, because it's something I think I'll be using a lot too. Here's a little more about the plans.

The page export/import functions will be available both on the API side, and in the admin interface. It's already partially functional on the API side, which you'll see in the [PagesExportImport](https://github.com/processwire/processwire/blob/dev/wire/core/PagesExportImport.php) class in the core. We've added a lot to that this week in ProcessWire 3.0.64. Though I don't suggest using it just yet, as there's still a lot of work left to do. But it may give you a few hints at what is yet to come:

- You can export/import individual pages, or multiple pages from a PageArray.
- The export/import format is based on JSON converted from PHP arrays.
- The used JSON format supports any number of pages in a single JSON file.
- The JSON format can also be used for copy/paste export and import processes, not unlike what we do with field/template exports and imports.
- Exports that include file/image fields also save to ZIP files, so that the assets can be included.
- The template, parent and other settings can be retained during import, or be modified.
- When a page already exists, you can choose to have it be updated by the import, skip it, or create a new copy of it under a different name.

On the API side have the [PagesExportImport](https://github.com/processwire/processwire/blob/dev/wire/core/PagesExportImport.php) class, and the plan is that once completed, we'll be providing methods in the $pages API variable for interacting with the export/import functions.


### Export and import in the admin

While we will have some really useful API functions for export/import of pages, I imagine most will be using them via the admin interface instead. This part is not yet in development (we've got to finalize the API first), so this is just preliminary and may yet change.

At present, it looks like we'll be developing a Process module for the purpose, that lives at Pages > Export/Import. It will have both Export and Import tabs. From the Export tab, you'll be able to export specific pages, all children of a specific page, or some other group of pages filtered by InpufieldSelector.

On the Import tab, you'll be able to upload a file or paste in the export (JSON). You'll be able to instruct it to import to the locations specified in the export, or override the parent/template and potentially other settings during import.

We may also provide some other shortcuts to export/import. For instance, maybe we'll have buttons for that purpose on the settings tab of a Page. We'll also likely develop a ListerPro action module that provides a shortcut as well. In any case, the goal is to make the export/import process really convenient and easy to use.


### Automation and feeds

I imagine the primary audience for these export/import functions will be web developers pulling and pushing updates between development and staging production sites. But it's worth noting that the API side of this will also be really handy for developing automated feeds for mirroring data between sites... something that I've done a lot of here in the past. Having the export/import functions built into the core API will really make this a lot simpler. I look forward to continuing development on this here and will continue to keep you up-to-date as progress is made. I'll likely have more to report on this next week as well.

Thanks for reading and hope that you all have a great weekend. Be sure to check in at the [ProcessWire Weekly](http://weekly.pw) this weekend for the latest ProcessWire news and updates.
