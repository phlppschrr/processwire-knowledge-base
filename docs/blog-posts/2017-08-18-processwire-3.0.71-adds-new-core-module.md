# ProcessWire 3.0.72 & 3.0.71 – Pages export/import

Source: https://processwire.com/blog/posts/processwire-3.0.71-adds-new-core-module/

## Sections


## Pages export/import module added to core (continued)

18 August 2017 by Ryan Cramer [ 3 Comments](/blog/posts/processwire-3.0.71-adds-new-core-module/#comments)


## ProcessWire 3.0.72

Last week we added the new core module for pages export/import, and this week I worked to continue building it out. Since it's essentially the same project as last week, I'm updating the existing ProcessWire 3.0.71 post here rather than creating a new blog post for this version. Though there have definitely been a lot of updates in 3.0.72, so if you are using the new Pages Export/Import module you'll definitely want to stay up-to-date with the dev branch as there is a lot of progress.


### What 3.0.72 adds relative to 3.0.71

**Repeater fields are now supported for export and import. **This was going to be the most challenging one to implement and it turned out that development went smoothly and it seems to work quite well. I've been using it all week to update a client's site between my local development environment and the live production site.

**Comments fields are now supported for export and import as well.** This one turned out to be a lot of work too! But like with repeaters, it seems to work great in testing here. That leaves just PageTable as the single remaining Fieldtype not yet implemented for export and import. But with repeaters now working, PageTable should be straightforward to implement and be here soon.

**The Export/Import module now supports ZIP file exports and imports.** This part I literally wrapped up half an hour or so before writing this, so it's not had a lot of testing yet. For this reason, it's labeled as "experimental" when you are using the module. The biggest advantage of ZIP file exports and imports comes when you are dealing with pages containing files and/or images. Those files and images get bundled in the export, ensuring they are present when the pages are imported. When not using a ZIP, you can still export/import pages with files and images, but they must be HTTP accessible in order to be imported. When using a ZIP, the files do not have to be HTTP accessible because they packaged directly into the export file.

Beyond the above updates, version 3.0.72 also includes several fixes related to issue reports. In addition it adds improvements to the image-replace feature in InputfieldImage. Now when you drop-in an image to replace an existing image, it retains the existing file name (an @apeisa suggestion). This is useful if you happen to be using the image in a CKEditor field, as any existing placements of the image will continue to work in CKEditor, but with the new image. If you've got the "fix broken images" option enabled for your CKEditor, it'll even automatically re-create the alternate size variations you may have inserted in CKEditor. This option can be found when editing your field at Setup > Fields > your field > Details (tab) > Markup/HTML Options. In addition, when you replace an image, it now remembers any assigned description and tags.

*The rest of this post below is from last week (August 11th) for ProcessWire 3.0.71. *


## ProcessWire 3.0.71

[Last week's post](/blog/posts/pw-3.0.70/) was about the pages export/import module being developed for ProcessWire. This week we continue that trend. But rather than showing you [screenshots](/blog/posts/pw-3.0.70/) of it, I've added the new pages export/import module to the core so that you can start using it instead!

If you look in the [commit log](https://github.com/processwire/processwire/commits/dev), you'll see there have been quite a lot of core updates today. All of those were developed over the last week, and then all committed this morning. Most of these commits are related to the pages export/import features, which required numerous updates throughout the core, especially to some core Fieldtype modules. This is one of the reasons why the pages export/import module is being added to the core right now–it's pretty well tied to the core version at present. Though this won't be the case as time goes on, but I still think it belongs in the core long term either way. Once you start using pages export/import, chances are you won't want to be without it. At least that's what I've found so far.


### Installing pages export/import

Now you are all set–take it for a spin. However, note that this module is very much a testing version and not yet ready for production use. So if you use it in production (especially for import) just make sure you have the ability to revert if anything gets messed up (always have backups).

Thanks for helping to test this module out. Please report any issues you run into at our GitHub [ProcessWire Issues repository](https://github.com/processwire/processwire-issues/issues).


### What’s been added to export/import since last week's post?

Quite a bit actually:


### What's still left to do?

- Repeater and PageTable support
- Comments field support
- ZIP file export and import
- ProFields support (not yet tested, some may already work)
- Support for paginated exports/imports (when too large to process in one request)

I opted to leave out the ZIP file support for this first version, because I felt like more work was needed there than there was time for this week. In addition, I focused on the JSON export/import support first because I find it a lot more convenient to work with, copying/pasting between systems. JSON is also nice for export/import data because it's a trivial matter to modify it or search/replace things that you want to adjust when migrating data between two different systems. However, ZIP support will be coming soon, and needed especially when migrating data that includes files from a local (non-HTTP accessible) dev environment to a production server. That's one of the big reasons to have ZIP support in a tool like this.


### Support for 3rd party Fieldtypes

Most 3rd party Fieldtypes should already work, but some likely won't and I'm happy to assist in making them work. If a Fieldtype doesn't work for export or import using the default/fallback methods, it's fairly simple to add support for it. The Fieldtype just has to implement exportValue() and importValue() methods. In most cases, it won't be necessary for a Fieldtype to do so unless it storing data outside of the "field_[name]" table. This is why Fieldtypes like Repeater and Comments don't work just yet (but soon will).

If you are a ProFields user, please stay tuned to the ProFields support boards as I'll be posting updates to add export/import support to those that don't yet support it. Repeater Matrix will support export/import on the same timeline as regular core Repeaters.


### Wrapping up

Next week I'll be working through some of the "to do" list above, and also catching up with some client work. With kids back in school (as of August 2), my work days are now a little shorter as my 4-year-old needs me from 2pm onward every day (school gets out at 2). We have a lot of fun! Admittedly it makes it little harder to keep up with the same amount of work (though waking up earlier solves a lot). But with a shorter schedule, next week I need to catch up on some details and communications. Rather than having a full blog post, I'll post a PW version update summary in the forums instead. Then the following week we'll have a full blog post again.

Thanks for reading, and please let us know how the export/import works for you. Stay tuned to the [ProcessWire Weekly](http://weekly.pw) for great new content every weekend.
