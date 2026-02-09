# ProcessWire 3.0.68 – More on page export/import

Source: https://processwire.com/blog/posts/processwire-3.0.68-and-more-on-page-export-import/

## Sections


## ProcessWire 3.0.68 – More on page export/import

21 July 2017 by Ryan Cramer [ 2 Comments](/blog/posts/processwire-3.0.68-and-more-on-page-export-import/#comments)


## ProcessWire 3.0.68

A few weeks ago we told you about our upcoming [page export/import feature](/blog/posts/a-look-at-upcoming-page-export-import-functions/). Progress continues, and this week we wanted to tell (and show) a little more about it.


### Page export/import continued

Like mentioned in that previous post, the API side functionality of exporting and importing comes from the *PagesExportImport* class, already present on the PW3 dev branch. While it's still not yet ready for anything other than the basics and testing, I was happy to see a [post from Horst](/talk/topic/16554-pw-3064-page-exportimport-details/?do=findComment&comment=147966) this morning that he'd had a successful experiment with it. I'm not suggesting others use it yet though, as there's still a lot of work left to be done, but it's coming along well.

This week I pushed some more updates to the class, adding support for export/import from ZIP files, and adding the ability for exports/imports to focus in on specific fields. This is all API side stuff. But at the same time, I'm also working on a companion Process module for providing an interactive interface to the export/import functions. When this module is far enough along, it'll likely be added to the core. This week I'll walk you through a bit about how it works with a few screenshots.

The interactive export/import functions are accessed from Pages > Export/Import. When you click to it, you arrive at a screen with two tabs: Export and Import. In the screenshot below, we see the Export tab. The first thing this module wants to know is what pages you want to export. You can choose specific pages, children of a parent page, or pages that match a search (selector). I've selected the first option below:

In the screenshot above, note the “Export Now” button gives you the choice of exporting to a ZIP file or to a JSON string for copy/paste.

**Exporting to a ZIP** is preferable for exports that may contain file or image fields. In this way, the files that those fields reference can be included in the export, and thus included anywhere you might later do an import. ZIP exports are also preferable for large exports, like those that might not be practical for copy/paste. Lastly, ZIP exports are great for cases where you want to archive to a file that may or may not be imported later (i.e. backups).

**Exporting to a JSON** string is preferable for quick and easy or common updates, where you don't want to hassle with files, and would rather just copy and paste pages from one installation another. It is very much similar to the exports that you might have already used for templates or fields. I like using this type of copy/paste process when creating pages on my local dev server and migrating them to my production server. It provides a very simple way to create or update pages.

In this next screenshot, I've selected the second option (pages having parent). In this case, I can select the parent for the children I want to export, and I also get a few additional options. The most interesting one to note is the “Recursive” option, which would let me export an entire tree of pages.

Next is the 3rd option, where I can select pages matching a search. This uses the InputfieldSelector module to let me build a selector to match pages. This gives you a lot of flexibility in deciding what you want included in our export.

One other thing I want to mention on the Export tab is the “Export fields” option. By default, an export includes all supported fields on a page. However, if you prefer it, you can choose the specific fields that you want to include in the export.

Screenshot above cropped half way to save space.

Once you hit the “Export Now” button, it starts downloading a ZIP file of the export immediately, unless you chose the JSON option, in which case it takes you to another screen where you can copy the export from your browser:

Next lets look at the Import tab. I don't have as much to show you here just because this is still very much a work in progress, but here's what we've got so far:

As you can see, you can upload a ZIP file containing the pages to import, or you can paste in the JSON string of pages. With the pages that are imported, you have the option of creating new pages, updating existing pages, or both.

I don't have any more screenshots because the rest is still a work in progress, so I'll write about the rest rather than show it. The import process involves a second step, so when you click the “Continue” button, you get an overview of what will be imported before you commit to it. You get to see what pages will be updated and what pages will be created. Like with the export option, you also have the option of overriding what fields get imported. If you've used the field or template export functions in ProcessWire, our plan is to approach it in a similar manner. In a future post (hopefully soon) we'll be covering the rest, at which time I hope to have the module in the core and ready for basic use and testing as well.

Thanks for reading, and have a great weekend, and hope to see you at the [ProcessWire Weekly](http://weekly.pw).
