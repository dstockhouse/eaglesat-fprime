#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1554930776.084352
__CHEETAH_genTimestamp__ = 'Wed Apr 10 14:12:56 2019'
__CHEETAH_src__ = 'publicInstanceTopologyH.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr 10 11:25:47 2019'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class publicInstanceTopologyH(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(publicInstanceTopologyH, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        # 
        #  This template will produce the constructArchitecture() global function that instances components and connects them.
        # 
        write(u'''
void setRef_Ids(void);

void ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'$(name)' on line 7, col 6
        if _v is not None: write(_filter(_v, rawExpr=u'$(name)')) # from line 7, col 6.
        write(u'''Init(void);

void ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'$(name)' on line 9, col 6
        if _v is not None: write(_filter(_v, rawExpr=u'$(name)')) # from line 9, col 6.
        write(u'''Start(void);

void ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'$(name)' on line 11, col 6
        if _v is not None: write(_filter(_v, rawExpr=u'$(name)')) # from line 11, col 6.
        write(u'''Register(void);

void construct''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'$(name)' on line 13, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'$(name)')) # from line 13, col 15.
        write(u'''Architecture(void);

void exitTasks(void) ;''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_publicInstanceTopologyH= 'respond'

## END CLASS DEFINITION

if not hasattr(publicInstanceTopologyH, '_initCheetahAttributes'):
    templateAPIClass = getattr(publicInstanceTopologyH, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(publicInstanceTopologyH)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=publicInstanceTopologyH()).run()


