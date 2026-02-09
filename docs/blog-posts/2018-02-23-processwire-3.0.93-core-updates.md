# ProcessWire 3.0.93 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.93-core-updates/

## Sections


## ProcessWire 3.0.93 core updates

23 February 2018 by Ryan Cramer [ 0 Comments](/blog/posts/processwire-3.0.93-core-updates/#comments)


## ProcessWire 3.0.93

ProcessWire 3.0.93 contains just minor tweaks and fixes as we prepare the code to be the next master release version, which could be as soon as next week or the week after. The focus here has been on making sure we've got any significant issues taken care of in the GitHub issue reports. If you are aware of any significant and reproducible bugs in the core that affect multiple people (rather than isolated to one instance), those are the issues we want to make sure are covered first, so please be sure to submit them in [GitHub issue reports](https://github.com/processwire/processwire-issues/issues). Or, if there already is an issue report open, please double check that it is still applicable on the current dev branch of ProcessWire. If it is, please let us know that the issue remains active in 3.0.93 by replying to it so that we'll be pinged on it. Thanks for your help in testing and reporting.

Some other work in progress here is that Horst and I are still tweaking the [zoom](/blog/posts/pw-3.0.92/) and [focus](/blog/posts/pw-3.0.89/) image field interactive behavior, as introduced last week. Horst has made some nice improvements to it, and most likely we'll have those present in next week's version, as this is the last new feature added before the next master version, and we want to make sure it's as good as it can be.

Also in progress here is a new version of [ProCache](/blog/categories/procache/). This new version includes automatic cache busting of file-based assets, both in your HTML output and in your stylesheets. This ensures that when the contents of a file changes and the filename doesn't, there's no chance of the user seeing the older version of it as a result of browser caching. ProCache can take care of this automatically simply by you checking a box in the ProCache configuration screen. But it also includes API functions for handling it as well. This new version of ProCache also includes various other minor tweaks and optimizations, and should be available for download as soon as next week.

Thanks for reading this short update, and enjoy reading the latest edition of the [ProcessWire Weekly](http://weekly.pw) this weekend.
