# New Site Profiles, Site Exporter and more…

Source: https://processwire.com/blog/posts/new-site-profiles-exporter-for-2.5/

## Sections


## New Site Profiles, Site Exporter and more…

27 August 2014 by Ryan Cramer [ 1 Comment](/blog/posts/new-site-profiles-exporter-for-2.5/#comments)

A few interesting mid-week updates for those following ProcessWire 2.5 development (aka the [dev branch](https://github.com/ryancramerdesign/ProcessWire/tree/dev)).


### The ProcessWire installer now lets you choose a site profile

When the ProcessWire installer runs, it now looks for any other profiles that might be available. Profiles are directories that start with "site-" and have site profile files in them. Today we added the Blank and Classic profiles to the dev branch, while the Languages and Iridium profiles are still in the works. Here is a description of each:

- **Default:** A minimal responsive site profile that serves as a good starting point for new sites or for learning about ProcessWire.
- **Classic:** This was the default site profile from ProcessWire versions 2.0 through 2.4. While now a little older in appearance, it is a great starting point for learning about ProcessWire.
- **Blank:** This profile includes only the bare minimum pages, fields and templates, giving you essentially a blank slate.
- **Languages:** Just like the default profile, but as multi-language version. [this one is not yet on the dev branch]
- **Iridium:** A site demonstrating more concepts and integration with existing CSS/JS frameworks ([preview](/iridium/)). [this one is not yet on the dev branch]

If you want to create a new profile for the installer, just use the new profile exporter (described further down). Older/existing site profiles should work too.


### New site profile exporter is far better than the previous

Related to the above, we now have a new site profile exporter that is far better than the previous. In fact, all of the above profiles were exported using it. Here are a few highlights:

- Ability to export profile to ZIP file that you can download.
- It now creates ready-to-go site profiles, needing no additions or modifications. Simply unzip the profile onto your server where ProcessWire is located, and ProcessWire's new installer can install it.
- Support for profile meta data including title, summary and screenshot image.
- Full Multi-language support! (the old profile exporter didn't support multi-language sites)
- Selective config.php export: you now have checkboxes to choose which site/config.php properties you want to end up in the profile.
- Uses ProcessWire's new WireDatabaseBackup class to handle the export (while PW's new installer uses it to handle the import).

The new profile exporter is available as the [dev](https://github.com/ryancramerdesign/ProcessExportProfile/tree/dev) branch of the existing profile exporter. If you want to give it a try, grab the latest ProcessWire dev version (2.4.15) and [Download ZIP](https://github.com/ryancramerdesign/ProcessExportProfile/archive/dev.zip) of the new profile exporter.


### Support for append/prepend files on a per-template basis

You may already know about the `$config->prependTemplateFile` and `$config->appendTemplateFile` options available in the /site/config.php file. They are used by a lot of site profiles, and they do what their name implies: prepend or append another file to all of your site template files.

Now you have the option of specifying them on a per-template basis. You also have the option of disabling the site-wide prepend/append options on a per-template basis as well. A screenshot explains it best:

As you can see in the screenshot above, these new options live under a new "Files" tab in the template edit screen.
