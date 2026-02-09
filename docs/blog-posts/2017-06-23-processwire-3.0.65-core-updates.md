# ProcessWire 3.0.65 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.65-core-updates/

## Sections


## ProcessWire 3.0.65 core updates

23 June 2017 by Ryan Cramer [ 8 Comments](/blog/posts/processwire-3.0.65-core-updates/#comments)


## ProcessWire 3.0.65

This week we have ProcessWire 3.0.65 on the dev branch. This version primarily focuses on bug fixes, covering issue reports from our issues repository on GitHub. While there weren't any major issues, we were able to cover quite a few items, so if you are following the dev branch it's worthwhile to grab this week's version.

ProcessWire 3.0.65 also upgrades the CKEditor version from 4.6.2 to 4.7.0. While it might look like there were several minor versions in between those two, there aren't. Version 4.7.0 is the version that follows 4.6.2. In my opinion, the most interesting additions in 4.7.0 were the addition of a [Table Selection plugin](http://ckeditor.com/addon/tableselection) that lets you “select and manipulate an arbitrary rectangular table fragment (a few cells, a row or a column)” and the new added support for pasting from Microsoft Excel. For a full list of changes, seek the [CKEditor 4.7.0 release notes](http://ckeditor.com/release-notes).


### New multi-language URL field

A need that sometimes comes up on multi-language sites is to have a multi-language URL field. You might need to store URLs or link to URLs that are specific to the language the user is viewing your page in. Anywhere that multiple languages are involved, sooner or later you are going to need the ability to store different URLs for each language. We've not had this in the past, so your best bet was just to repurpose the existing multi-language text field. But now we've got a dedicated multi-language URL field available called [FieldtypeURLLanguage](https://github.com/ryancramerdesign/FieldtypeURLLanguage), which provides a much better solution.

The multi-language URL fieldtype works essentially the same as the existing URL fieldtype. In fact, it extends the existing core URL fieldtype, so it shares all of the same features. But it also works the same as the existing multi-language text field, enabling you to use it (from the API side) exactly the same way that you use the FieldtypeTextLanguage field included with the core. Which is to say, it's very simple to use.

I decided not to add this as a core module since not everyone needs a multi-language URL field. Instead, I've released it as a module in our [modules directory](https://modules.processwire.com/modules/fieldtype-urllanguage/) and on my [GitHub account](https://github.com/ryancramerdesign/FieldtypeURLLanguage). Though if there's a strong need, we might always add it to the core later. I would also be interested in learning what other simple Fieldtypes you might find useful to have multi-language variations of.

*I hope that you all have a great weekend and enjoy the *[ProcessWire Weekly](http://weekly.pw)*. We'll see you back here next week, when we hope to make a little more progress on the page export/import features that we talked about last week. *
