# ProcessWire 3.0.121 core updates and more

Source: https://processwire.com/blog/posts/processwire-3.0.121-core-updates-and-more/

## Sections


## ProcessWire 3.0.121 core updates and more

7 December 2018 by Ryan Cramer [ 6 Comments](/blog/posts/processwire-3.0.121-core-updates-and-more/#comments)


## ProcessWire 3.0.121

ProcessWire 3.0.121 is on the dev branch and this should be considered release candidate 1 (RC1) of our next master branch version. Relative to 3.0.120 this version fixes a few minor issues, though nothing big enough to document here.

I know I've mentioned it before, but just to repeat: if you come across any issues that are not present on the current master version (version 3.0.98) please let me know. A good way to do this is to [post the issue report](https://github.com/processwire/processwire-issues/issues) and indicate that it is exclusive to the dev branch.

Of course, it's always worthwhile to post issue reports regardless of how long they've been around. But with release candidate versions, at minimum we want to make sure the next master version doesn't introduce any new issues relative to the existing master.

If you've already posted such an issue and it's not been fixed yet, please post a reply in the report and indicate it's an issue on the dev branch that's not in the master, and I'll be specifically looking for any of these this week.

I've been scouting all over the issue reports this week looking for anything that fits this criteria (dev branch specific), and I've actually not found any issues that do yet (that I can remember). Though there's plenty of issue reports, so I've been focused on fixing those that have little possibility of introducing new issues or need significant post-fix testing. I'll save fixing any issues that might need more marination time on the dev branch until after the next master is out. Thanks to all of you that have been helping out in our issues repository!


### Clear image variations (Page Action module)

Today I posted a new *PageAction* module in the *ListerPro* board. This one is called *PageActionClearImageVariations*. When installed with [ListerPro](/store/lister-pro/), this page action enables you to clear variation files of images on any pages. This is useful if you've got extra image files lying around, perhaps containing old image sizes no longer in use.

This was originally developed for the ProcessWire sites directory, where we generate a couple different sizes of each image, for more than 800 sites. When working on the site redesign, the needed dimensions changed. All the files having the old dimensions were no longer needed, so this tool helped clear out hundreds of megabytes of unnecessary images. The following screenshot outlines the filters available to select which images should be cleared:

This module is available for download now to ListerPro subscribers in the support board in the [ProcessWire forums](/talk/topic/20471-listerpro-page-action-clear-image-variations/) (requires login). This accompanies the other existing PageAction modules for ListerPro which enable you to apply actions to any number of pages at once. These include:

- CSV Page Export
- Set Field Values
- Delete/Trash Pages
- Send Emails
- Move Pages
- Set Page Status
- Clear image variations (new)


### A couple new modules in production

Some of you asked about the search engine demonstrated in the screenshots last week. I've developed it as a module and am likely going to add it to the ProDevTools set of modules once completed. The module lets you search not just pages, but any other kind of data you want to search. That's how we've got it searching the ProcessWire API and modules directory right now, which aren't searched as pages. It does this by letting you add the implementation for performing the search, while it handles the the logic for determining when and where each part should be called. You add new search types and provide the implementation for each like this:

```
$search = $modules->get('ProSiteSearch');
$search->add('Name of search', function($q, $limit){
 // find & return results ($q is the search text)
});
```

Here's an abbreviated version of what my /site/templates/search.php on the new ProcessWire.com website looks like:

```
$search = $modules->get('ProSiteSearch');

$search->add('Showcase', function($q, $limit) {
  return pages()->find("template=sites, limit=$limit, title~=$q");
});

$search->add('API', function($q, $limit) {
  $api = wire('modules')->get('ProcessWireAPI');
  return $api->search($q, [ 'limit' => $limit ]);
});

// and so on...
$search->add('Modules', function($q, $limit) { ... });
$search->add('Blog', function($q, $limit) { ... });
$search->add('General', function($q, $limit) { ... });
```

The module handles the rest in terms of AJAX/JSON output and provides all the data necessary for your regular search results output. It comes with examples using Uikit 3, but does not have any framework-specific dependencies.

In addition to that, I've also recently been working on *ProMailer* which is a module I developed for managing the weekly newsletter distribution. This is something I actually developed a few years ago, but have recently been improving it and making it more into something that might also be helpful to others. The module is useful if you want to do your email newsletter production, distribution and subscriber management in-house, rather than outsourcing to an external service like MailChimp. That's how we do it at processwire.com, and have for several years. Though the module has been kind of bare-bones (since I've been the only user of it), but I've been recently improving upon it not just for the new website, but also hopefully to share too.

Thanks for reading, have a great weekend and enjoy the [ProcessWire Weekly](http://weekly.pw)!
