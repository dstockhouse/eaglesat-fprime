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
__CHEETAH_genTime__ = 1554930776.509951
__CHEETAH_genTimestamp__ = 'Wed Apr 10 14:12:56 2019'
__CHEETAH_src__ = 'publicTopologyCpp.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr 10 11:25:47 2019'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class publicTopologyCpp(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(publicTopologyCpp, self).__init__(*args, **KWs)
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
        write(u'''void construct''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'$(name)' on line 4, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'$(name)')) # from line 4, col 15.
        write(u'''Architecture(void) {  
''')
        if VFSL([locals()]+SL+[globals(), builtin],"connect_only",True): # generated from line 6, col 1
            pass
        else: # generated from line 8, col 1
            write(u'''    Fw::PortBase::setTrace(true);
''')
            if VFSL([locals()]+SL+[globals(), builtin],"is_ptr",True): # generated from line 11, col 1
                write(u'''    simpleReg_ptr = new Fw::SimpleObjRegistry();
''')
            else: # generated from line 13, col 1
                write(u'''    ''')
                # If objects are being generated as instances they were instansiated in includes. 
                pass
            if VFN(VFSL([locals()]+SL+[globals(), builtin],"kind",True),"get_comment",False)(): # generated from line 16, col 1
                write(u'''// ''')
                _v = VFN(VFSL([locals()]+SL+[globals(), builtin],"kind",True),"get_comment",False)() # u'$kind.get_comment()' on line 17, col 4
                if _v is not None: write(_filter(_v, rawExpr=u'$kind.get_comment()')) # from line 17, col 4.
                write(u'''
''')
            for declaration_template in VFSL([locals()]+SL+[globals(), builtin],"component_declarations",True): # generated from line 19, col 1
                if VFSL([locals()]+SL+[globals(), builtin],"declaration_template",True) is None: # generated from line 20, col 1
                    pass
                else: # generated from line 22, col 1
                    write(u'''    ''')
                    _v = VFSL([locals()]+SL+[globals(), builtin],"declaration_template",True) # u'${declaration_template}' on line 23, col 5
                    if _v is not None: write(_filter(_v, rawExpr=u'${declaration_template}')) # from line 23, col 5.
                    write(u'''
''')
                write(u'''
''')
            write(u'''    
    // Component initialization
''')
            for init_template in VFSL([locals()]+SL+[globals(), builtin],"component_inits",True): # generated from line 29, col 1
                write(u'''    ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"init_template",True) # u'${init_template}' on line 30, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'${init_template}')) # from line 30, col 5.
                write(u''' 
''')
        write(u'''
    // Port connections
''')
        for comment, connection in VFSL([locals()]+SL+[globals(), builtin],"port_connections",True): # generated from line 36, col 1
            write(u'''    ''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"comment",True) # u'${comment}' on line 37, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'${comment}')) # from line 37, col 5.
            write(u'''
    ''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"connection",True) # u'${connection}' on line 38, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'${connection}')) # from line 38, col 5.
            write(u'''
''')
        write(u'''
''')
        if VFSL([locals()]+SL+[globals(), builtin],"connect_only",True): # generated from line 42, col 1
            pass
        else: # generated from line 44, col 1
            write(u'''    // Active component startup
    // start(identifier, priority, stack_size)
''')
            for startup_template  in VFSL([locals()]+SL+[globals(), builtin],"component_startups",True): # generated from line 48, col 1
                write(u'''    ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"startup_template",True) # u'${startup_template}' on line 49, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'${startup_template}')) # from line 49, col 5.
                write(u''' 
''')
            write(u'''
    dumparch();

    // Command registration
''')
            for cmdReg in VFSL([locals()]+SL+[globals(), builtin],"command_registrations",True): # generated from line 56, col 1
                write(u'''    ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"cmdReg",True) # u'${cmdReg}' on line 57, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'${cmdReg}')) # from line 57, col 5.
                write(u'''
''')
        write(u'''}


''')
        if VFSL([locals()]+SL+[globals(), builtin],"connect_only",True): # generated from line 64, col 1
            pass
        else: # generated from line 66, col 1
            write(u'''void exitTasks(void) {
   // Task cleanup
''')
            for teardown_template in VFSL([locals()]+SL+[globals(), builtin],"component_teardowns",True): # generated from line 69, col 1
                write(u'''    ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"teardown_template",True) # u'${teardown_template}' on line 70, col 5
                if _v is not None: write(_filter(_v, rawExpr=u'${teardown_template}')) # from line 70, col 5.
                write(u'''
''')
            write(u'''}
''')
        write(u'''


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

    _mainCheetahMethod_for_publicTopologyCpp= 'respond'

## END CLASS DEFINITION

if not hasattr(publicTopologyCpp, '_initCheetahAttributes'):
    templateAPIClass = getattr(publicTopologyCpp, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(publicTopologyCpp)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=publicTopologyCpp()).run()


