# Rebuilding the ProcessWire.com website (part 2)

Source: https://processwire.com/blog/posts/rebuilding-pw-website-part2/

## Sections


## Rebuilding the ProcessWire.com website (part 2)

26 October 2018 by Ryan Cramer [ 4 Comments](/blog/posts/rebuilding-pw-website-part2/#comments)

I've been continuing to work on the new processwire.com website this week and spent nearly the entire week working on the documentation section. It feels like Monday afternoon and it's already Friday, time flies. I had thought that I'd be primarily just importing and moving stuff around. But instead I'm rewriting a lot of existing content, as well as adding a lot of new content, and deleting some outdated content as well.

As I go through each page of the existing documentation, I find that many are missing certain aspects that perhaps were only present in the blog posts before. For instance, the page on Hooks didn't yet cover conditional hooks. But that's just one example of many. There are just a lot of gaps that need to be filled, more than I had realized, so this week I've been doing as much (or more) writing and modifying content as I have been development. Almost all of the content is getting a nice refresh.

Despite putting nearly the entire week into it, I'm still not finished with the documentation section, though getting close. There's just a lot to it. So next week I'm going to finish that off hopefully and then work on the more marketing oriented side of the site, in the “About ProcessWire” section. The good news is that the new website is going to be far more than just a visual and technical upgrade, it's also going to be a real upgrade in terms of the site's content quality and scope.

One thing that is different about the new site is that the entire site uses categories/topics for every page, much like a blog post might. Though the blog posts here have not used them in the past. But because so much important stuff ends up in these blog posts, I wanted to have a way to categorize them so that they could be automatically connected with the relevant documentation pages. For instance, if some new hooks were added and mentioned in a blog post, they would be cross referenced automatically from the main hooks documentation page. Likewise for all documentation topics (selectors, security, access control, modules, multi-language, and on and on…).


### Documentation pages structure

Below is the current draft on documentation structure in terms of the page tree. All of it is located under a /docs/ page.

```
Docs
  API reference
    …existing API ref pages
    Cheatsheet
  Getting started
    Installation
      Install
      Upgrade
      Troubleshoot
    Structure
      Pages
      Templates
      Fields
      Files and directories
    The API
    Template files
    Output strategies
      Direct output
      Delayed output
      Markup regions
    API variables
      …one page for every API variable -> API reference
    URL segments and routing
    Include and bootstrap
  Modules
    Introduction to modules
    Module types
    Module development
    Module guides and docs
      …several pages in here
    Third-party modules
    Pro modules
      …one doc page for each Pro module
  Selectors
  Hooks
    …cross reference with API reference
    Captain Hook
  Access
    Users
    Roles
    Permissions
  Tutorials
    …several tutorials
  Security
    Securing file permissions
    Securing your admin
    Web hosting security
    Migrating to production
    Remove unnecessary files
    Database-driven sessions
    Running ProcessWire alongside other software
    Third party modules
  Multi-language
    Code internationalization
    Multi-language fields
    Multi-language URLs
    Language Packs
  Coding style guide
```

It sounds like last week's version 3.0.117 additions to WireArray may have caused issues in PHP versions prior to 7.x. Sorry about that—it has been hopefully fixed on the dev branch. The culprit was a method that I added primarily for phpdoc purposes so that it would be picked up in the automatically generated ProcessWire API Reference site. It wasn't too important, and I simply removed it. Everything mentioned in last week's blog post still works. While I'm not yet bumping the core version number on the dev branch till next week, there are still several small updates and fixes on the dev branch this week, but I'll save the details on those, as well as some other nice additions in progress, for next week's blog post.

Thanks for reading, have a good weekend and like every week, be sure to check in and read the [ProcessWire Weekly](http://weekly.pw) for the latest ProcessWire news.
