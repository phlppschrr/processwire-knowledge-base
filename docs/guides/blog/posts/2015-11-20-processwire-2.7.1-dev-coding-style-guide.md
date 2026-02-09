# ProcessWire 2.7.1 dev + coding style guide

Source: https://processwire.com/blog/posts/processwire-2.7.1-dev-coding-style-guide/

## Sections


## ProcessWire 2.7.1 dev + coding style guide

20 November 2015 by Ryan Cramer [ 1 Comment](/blog/posts/processwire-2.7.1-dev-coding-style-guide/#comments)

This week several minor bug fixes were applied to the dev branch as version 2.7.1 and this will likely be pulled into the master branch next week, replacing the current 2.7.0 stable version. The big news of this week is the introduction of the ProcessWire PHP Coding Style Guide, which is something that several have asked for over time, and now we've finally published it!


### Introducing the ProcessWire PHP coding style guide

The [ProcessWire PHP coding style guide](/api/coding-style-guide/) represents the coding style preferred for the ProcessWire core. It is also *recommended* (though certainly not required) for 3rd party modules and other code using the ProcessWire API, unless an existing coding standard is already in place or preferred. Use of the coding style guide is however requested for code submissions (pull requests) to the ProcessWire core.

The ProcessWire coding style guide is based on [PSR-1](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-1-basic-coding-standard.md) and [PSR-2](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-2-coding-style-guide.md), but with several important differences and additions (some ProcessWire specific). Some notable differences from the PSR style guides include:

In general, we feel that for developers using ProcessWire, the ProcessWire coding style guide offers a more consistent vision of code style relative to the PSR guides. That's in large part because we don't advocate changing usages of spacing, brackets, parenthesis or naming conventions for different code contexts. Perhaps there is value in having such context changes in the bigger PHP picture, but when it comes to ProcessWire we prefer greater consistency in these areas, and you'll see that reflected in the style guide.

It's worth noting that the PSR-2 standard has wide adoption and is used by many projects. If the Processwire Coding Style Guide doesn't suit your needs, we'd certainly suggest using the PSR-2 style guide. While we feel PSR-2 is a compromise in many ways, that can also be a good thing in the bigger PHP context.

Consider this version 1 of the coding style guide, and we may have more to add or change as time goes on. If there's anything you think we've missed or anything you have reactions to, please let us know too.

**[See the ProcessWire Coding Style Guide](/api/coding-style-guide/)**


### Do as we say, not as we do ;-)

After looking at the coding style guide, you might notice that even the ProcessWire core doesn't always follow these rules, at least not *all* of the time. We wrote it as much for us as we did for others that have requested it. As we shift more into ProcessWire 3.0 development we'll be putting more emphasis on making sure our own code always lives up to all the recommendations in the style guide. We have a lot of optimizations still to make, especially when it comes to making sure everything is covered with PHPDoc.


### Vote for ProcessWire as “Best CMS for Developers” at CMS Critic

ProcessWire has been nominated as the Best CMS for Developers at CMS Critic, and the awards are now open for voting. If you have a minute, and believe ProcessWire is the Best CMS for Developers (we do!) please [go there and vote for ProcessWire](http://awards.cmscritic.com/vote/). Thanks for voting!

That's all for this week! Hope that you all have a great weekend/week ahead and remember to visit the [ProcessWire Weekly](http://weekly.pw) this weekend.
