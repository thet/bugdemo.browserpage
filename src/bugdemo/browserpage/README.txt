BUGDEMO BROWSERPAGE
===================

Start this test like so:
./bin/test -s bugdemo.browserpage -t README.txt

After this package was installed in plone, 2 different browser:page views are
registered for a folder (configure.zcml and profiles/default/types/types.xml).
There exists one class for each registered view with an init method which prints
the name of the view to stdout (browserpageview.py).

When a folder is created, every init-method of both view-classes are called -
even though the folder's default_view wasn't set to one of those views:
    >>> self.folder.invokeFactory('Folder', 'testfolder', title='testfolder')
    testview_1
    testview_2
    'testfolder'

Lets set the default_view of the folder to one of our registered views:
    >>> self.folder.testfolder.setLayout('testview_1')

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()
    >>> folder_url = self.folder.absolute_url()

After opening the folder in the browser the view is called twice (that's ok):
    >>> browser.open(folder_url + '/testfolder')
    testview_1
    testview_1

But now let's login:
    >>> from Products.PloneTestCase.setup import portal_owner, default_password
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()

After opening the folder again, the folder's defaultview is called five times
and the other view we registered is called three times (that's not ok i suppose)
    >>> browser.open(folder_url + '/testfolder')
    testview_1
    testview_1
    testview_1
    testview_2
    testview_1
    testview_2
    testview_1
    testview_2


#    >>> interact( locals() )
