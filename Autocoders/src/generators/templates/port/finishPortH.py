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
__CHEETAH_genTime__ = 1554930755.86825
__CHEETAH_genTimestamp__ = 'Wed Apr 10 14:12:35 2019'
__CHEETAH_src__ = 'finishPortH.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr 10 11:25:47 2019'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class finishPortH(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(finishPortH, self).__init__(*args, **KWs)
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
        
        write(u'''    /// Input ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'$name' on line 1, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 1, col 15.
        write(u''' port description
    /// ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"desc",True) # u'$desc' on line 2, col 9
        if _v is not None: write(_filter(_v, rawExpr=u'$desc')) # from line 2, col 9.
        write(u'''
    
    class Output''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'${name}' on line 4, col 17
        if _v is not None: write(_filter(_v, rawExpr=u'${name}')) # from line 4, col 17.
        write(u'''Port : public Fw::OutputPortBase {
      public: 
        Output''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'${name}' on line 6, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'${name}')) # from line 6, col 15.
        write(u'''Port(void);
        void init(void);
        void addCallPort(Input''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'${name}' on line 8, col 31
        if _v is not None: write(_filter(_v, rawExpr=u'${name}')) # from line 8, col 31.
        write(u'''Port* callPort);
        ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"return_type",True) # u'${return_type}' on line 9, col 9
        if _v is not None: write(_filter(_v, rawExpr=u'${return_type}')) # from line 9, col 9.
        write(u'''invoke(''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"args_string",True) # u'$args_string' on line 9, col 30
        if _v is not None: write(_filter(_v, rawExpr=u'$args_string')) # from line 9, col 30.
        write(u''');
      protected:
      private:
        Input''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'${name}' on line 12, col 14
        if _v is not None: write(_filter(_v, rawExpr=u'${name}')) # from line 12, col 14.
        write(u'''Port* m_port;
    };
''')
        if VFSL([locals()]+SL+[globals(), builtin],"namespace_list",True) != None: # generated from line 14, col 1
            for namespace in VFSL([locals()]+SL+[globals(), builtin],"namespace_list",True): # generated from line 15, col 2
                write(u'''} // end namespace ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"namespace",True) # u'$namespace' on line 16, col 20
                if _v is not None: write(_filter(_v, rawExpr=u'$namespace')) # from line 16, col 20.
                write(u'''
''')
        write(u'''#endif /* ''')
        _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"name",True),"upper",False)() # u'${name.upper()}' on line 19, col 12
        if _v is not None: write(_filter(_v, rawExpr=u'${name.upper()}')) # from line 19, col 12.
        write(u'''_HPP_ */

''')
        
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

    _mainCheetahMethod_for_finishPortH= 'respond'

## END CLASS DEFINITION

if not hasattr(finishPortH, '_initCheetahAttributes'):
    templateAPIClass = getattr(finishPortH, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(finishPortH)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=finishPortH()).run()


