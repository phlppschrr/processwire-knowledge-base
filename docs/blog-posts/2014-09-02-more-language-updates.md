# More Language Updates

Source: https://processwire.com/blog/posts/more-language-updates/

## Sections


## More Language Updates

2 September 2014 by Ryan Cramer [ 0 Comments](/blog/posts/more-language-updates/#comments)


### ProcessWire now comes with a multi-language site profile

This morning I finished packaging up a multi-language version of the Default Site Profile for ProcessWire 2.5. This was one of the final tasks to do before putting out the first release candidate of 2.5. This multi-language site profile includes a site in 3 languages: English, German and Finnish. it demonstrates most of the multi-language features available for front-end output in ProcessWire.

On the admin side, I included the German language pack along with all of Manfred62's great updates to it. I didn't include the Finnish language pack because it's not yet updated for PW 2.5, and it might be too much to bundle two language packs in the core. (Language packs are small in file size, but do consist numerous files). By that token, maybe we shouldn't include the German language pack either, but I figured we'd give the idea a test drive and see. It certainly is a better demonstration if you can see PW's admin fully translated.

For the front-end site profile, I copied and pasted translations from Google Translate, so chances are the translations aren't great. If any of you in Germany or Finland want to make a better translation, it would be great. See instructions at the end of this post.


### Language translation files now split by site and core

Something that has come up several times is that people don't like getting their static site translation files mixed in with language pack files. With language packs now having more than a hundred files, it's understandably a bit clumsy to manage these in the same field as your site translation files. We've fixed this so that now you have 2 separate file fields for each language: one for your site files (/site/), and the other for language packs (/wire/). Though you can choose to use them however you wish, as ProcessWire doesn't enforce only /site/ or /wire/ in either one of them… rather it's just a suggestion. But hopefully this will greatly simplify management of static translation files and language packs in ProcessWire.


### How to make a new translation of the multi-language profile

- Grab the [latest dev](https://github.com/ryancramerdesign/ProcessWire/tree/dev) of ProcessWire (currently 2.4.17) and install it with the Multi-Language profile (it asks you which profile at install time).
- Edit and translate any of the pages as you see fit (all of the text fields are multi-language).
- We also have just a couple static translations in two template files: _main.php and search.php. These can be modified in Setup > Languages.
- Install [this latest version](https://github.com/ryancramerdesign/ProcessExportProfile/tree/dev) of the profile exporter ([download ZIP](https://github.com/ryancramerdesign/ProcessExportProfile/archive/dev.zip)) and go to Setup > Export Site Profile.
- Export to a ZIP file and PM to ryan in the forums. Thanks!
