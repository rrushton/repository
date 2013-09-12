# SolusOS 2 Package Repository
==============================
Please help us by doing code-reviews and audits on our server.

Want to get started? Check http://inf.solusos.com/w/quick_start/ for
a real quick how-to on SolusOS contribution


Versioning and Specifics
------------------------
SolusOS versioning uses the following scheme:

 $MAJOR.$ISOYEAR$ISOWEEK.$ISODAY.$PATCHLEVEL

All changes should initially be made to the volatile branch, enabling us to
maintain a static master for the majority of the time. If today's date is
the 12th of September, 2013, we can say that our base version number would be:

    2.201337.4.0

Once packages have survived testing in volatile, they can then be merged into
master. A new version number does not need to be generated unless a build has
been queued, which will push the packages into the public binary repositories.

At this point, a new tag with the current version number should be created and
pushed to the repository, and a ChangeLog should accompany this tag, listing all
changes between this tag and the last. This enables real tracking of the repository
between different releases, and different upgrades. Using the ISO date system also
enables us to quickly identify exactly which update caused any issue.

If a security update or patch is pushed to volatile, it again must go through the
stability testing process. Should only an update that affects either a bug or security
issue, without changing the major version number of affected packages (this means excluding
other package updates from the queue) be then merged into the repository, the original
queue ISO date should be retained, with an increment to the patch level.

For instance, if the last release was 2.201337.4.0, and we push a patch fixing a security
issue in glibc, the new version number would be:

    2.201337.4.1

This will hold true regardless of the current ISO date. If the only manner in which the issue
could be resolved was a glibc update (i.e. 2.17 to 2.18), the patch level should be reset and
a new version number shall be calculated using the current ISO date. Note that the MAJOR
version is always that of the distribution release, in this case that is 2.

Shortening versions
-------------------
During the current working year it may sometimes be appropriate to commonly refer to versions
without using the ISO year, especially for conversational uses. Official publications will always
refer to the full SolusOS version number for the sake of professionalism.

To use the above version numbers as an example, a user may refer to an update as:

    2.37.4.1

Helpful commit messages
-----------------------
In time many changelogs will be generated using automated tools, to determine if version numbering
is correct, and to asssociate the correct tags. In order to help with this your commit message
must now *always* be appropriately prefixed with one of the following:

 * [NEW] indicates a new package being added to the repo
 * [UPDATE] indicates a package upgrade
 * [FIX] indicates a security or bugfix, which warrant only patch level and not new version
 * [REMOVE] used to remove a package from the repository


Authors
-------

 * Ikey Doherty <ikey@solusos.com>
