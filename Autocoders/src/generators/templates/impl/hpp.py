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
__CHEETAH_genTime__ = 1554930773.925955
__CHEETAH_genTimestamp__ = 'Wed Apr 10 14:12:53 2019'
__CHEETAH_src__ = 'hpp.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr 10 11:25:47 2019'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class hpp(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(hpp, self).__init__(*args, **KWs)
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
        
        write(u'''// ====================================================================== 
// \\title  ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'${name}' on line 2, col 12
        if _v is not None: write(_filter(_v, rawExpr=u'${name}')) # from line 2, col 12.
        write(u'''Impl.hpp
// \\author ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"user",True) # u'$user' on line 3, col 12
        if _v is not None: write(_filter(_v, rawExpr=u'$user')) # from line 3, col 12.
        write(u'''
// \\brief  hpp file for ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'${name}' on line 4, col 25
        if _v is not None: write(_filter(_v, rawExpr=u'${name}')) # from line 4, col 25.
        write(u''' component implementation class
//
// \\copyright
// Copyright 2009-2015, by the California Institute of Technology.
// ALL RIGHTS RESERVED.  United States Government Sponsorship
// acknowledged. Any commercial use must be negotiated with the Office
// of Technology Transfer at the California Institute of Technology.
// 
// This software may be subject to U.S. export control laws and
// regulations.  By accepting this document, the user agrees to comply
// with all U.S. export laws and regulations.  User has the
// responsibility to obtain export licenses, or other export authority
// as may be required before exporting such information to foreign
// countries or providing access to foreign persons.
// ====================================================================== 

#ifndef ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'${name}' on line 20, col 10
        if _v is not None: write(_filter(_v, rawExpr=u'${name}')) # from line 20, col 10.
        write(u'''_HPP
#define ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'${name}' on line 21, col 10
        if _v is not None: write(_filter(_v, rawExpr=u'${name}')) # from line 21, col 10.
        write(u'''_HPP

#include "''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"include_path",True) # u'${include_path}' on line 23, col 12
        if _v is not None: write(_filter(_v, rawExpr=u'${include_path}')) # from line 23, col 12.
        write(u'''/''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"include_name",True) # u'${include_name}' on line 23, col 28
        if _v is not None: write(_filter(_v, rawExpr=u'${include_name}')) # from line 23, col 28.
        write(u'''ComponentAc.hpp"

''')
        if VFSL([locals()]+SL+[globals(), builtin],"namespace_list",True) != None: # generated from line 25, col 1
            for namespace in VFSL([locals()]+SL+[globals(), builtin],"namespace_list",True): # generated from line 26, col 3
                write(u'''namespace ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"namespace",True) # u'${namespace}' on line 27, col 11
                if _v is not None: write(_filter(_v, rawExpr=u'${namespace}')) # from line 27, col 11.
                write(u''' {
''')
        write(u'''
  class ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'${name}' on line 31, col 9
        if _v is not None: write(_filter(_v, rawExpr=u'${name}')) # from line 31, col 9.
        write(u'''ComponentImpl :
    public ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"component_base",True) # u'$component_base' on line 32, col 12
        if _v is not None: write(_filter(_v, rawExpr=u'$component_base')) # from line 32, col 12.
        write(u'''
  {

    public:

      // ----------------------------------------------------------------------
      // Construction, initialization, and destruction
      // ----------------------------------------------------------------------

      //! Construct object ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'$name' on line 41, col 28
        if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 41, col 28.
        write(u'''
      //!
      ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'${name}' on line 43, col 7
        if _v is not None: write(_filter(_v, rawExpr=u'${name}')) # from line 43, col 7.
        write(u'''ComponentImpl(
#if FW_OBJECT_NAMES == 1
''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"emit_non_port_params",False)([ VFSL([locals()]+SL+[globals(), builtin],"param_compName",True) ]) # u'$emit_non_port_params([ $param_compName ])' on line 45, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$emit_non_port_params([ $param_compName ])')) # from line 45, col 1.
        write(u'''
#else
          void
#endif
      );

      //! Initialize object ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'$name' on line 51, col 29
        if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 51, col 29.
        write(u'''
      //!
      void init(
''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"emit_non_port_params",False)(VFSL([locals()]+SL+[globals(), builtin],"params_init_hpp",True)) # u'$emit_non_port_params($params_init_hpp)' on line 54, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$emit_non_port_params($params_init_hpp)')) # from line 54, col 1.
        write(u'''
      );

      //! Destroy object ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'$name' on line 57, col 26
        if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 57, col 26.
        write(u'''
      //!
      ~''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'${name}' on line 59, col 8
        if _v is not None: write(_filter(_v, rawExpr=u'${name}')) # from line 59, col 8.
        write(u'''ComponentImpl(void);

''')
        if len(VFSL([locals()]+SL+[globals(), builtin],"typed_user_input_ports",True)) > 0: # generated from line 61, col 1
            write(u'''    PRIVATE:

      // ----------------------------------------------------------------------
      // Handler implementations for user-defined typed input ports
      // ----------------------------------------------------------------------

''')
            for instance, type, sync, priority, full, role, max_num in VFSL([locals()]+SL+[globals(), builtin],"typed_user_input_ports",True): # generated from line 68, col 3
                write(u'''      //! Handler implementation for ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"instance",True) # u'$instance' on line 69, col 38
                if _v is not None: write(_filter(_v, rawExpr=u'$instance')) # from line 69, col 38.
                write(u'''
      //!
      void ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"instance",True) # u'${instance}' on line 71, col 12
                if _v is not None: write(_filter(_v, rawExpr=u'${instance}')) # from line 71, col 12.
                write(u'''_handler(
''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"emit_port_params",False)([ VFSL([locals()]+SL+[globals(), builtin],"param_portNum",True) ] + VFSL([locals()]+SL+[globals(), builtin],"port_params",True)[VFSL([locals()]+SL+[globals(), builtin],"instance",True)]) # u'$emit_port_params([ $param_portNum ] + $port_params[$instance])' on line 72, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'$emit_port_params([ $param_portNum ] + $port_params[$instance])')) # from line 72, col 1.
                write(u'''
      );

''')
        if len(VFSL([locals()]+SL+[globals(), builtin],"serial_input_ports",True)) > 0: # generated from line 77, col 1
            write(u'''    PRIVATE:

      // ----------------------------------------------------------------------
      // Handler implementations for user-defined serial input ports
      // ----------------------------------------------------------------------

''')
            for instance, sync, priority, full, max_num in VFSL([locals()]+SL+[globals(), builtin],"serial_input_ports",True): # generated from line 84, col 3
                write(u'''      //! Handler implementation for ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"instance",True) # u'$instance' on line 85, col 38
                if _v is not None: write(_filter(_v, rawExpr=u'$instance')) # from line 85, col 38.
                write(u'''
      //!
      void ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"instance",True) # u'${instance}' on line 87, col 12
                if _v is not None: write(_filter(_v, rawExpr=u'${instance}')) # from line 87, col 12.
                write(u'''_handler(
        NATIVE_INT_TYPE portNum, ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"doxygen_post_comment",False)("The port number") # u'$doxygen_post_comment("The port number")' on line 88, col 34
                if _v is not None: write(_filter(_v, rawExpr=u'$doxygen_post_comment("The port number")')) # from line 88, col 34.
                write(u'''
        Fw::SerializeBufferBase &Buffer ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"doxygen_post_comment",False)("The serialization buffer") # u'$doxygen_post_comment("The serialization buffer")' on line 89, col 41
                if _v is not None: write(_filter(_v, rawExpr=u'$doxygen_post_comment("The serialization buffer")')) # from line 89, col 41.
                write(u'''
      );

''')
        if VFSL([locals()]+SL+[globals(), builtin],"has_commands",True): # generated from line 94, col 1
            write(u'''    PRIVATE:

      // ----------------------------------------------------------------------
      // Command handler implementations 
      // ----------------------------------------------------------------------

''')
            for mnemonic, opcode, sync, priority, full, comment in VFSL([locals()]+SL+[globals(), builtin],"commands",True): # generated from line 101, col 3
                params = VFSL([locals()]+SL+[globals(), builtin],"command_params",True)[VFSL([locals()]+SL+[globals(), builtin],"mnemonic",True)]
                write(u'''      //! Implementation for ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"mnemonic",True) # u'$mnemonic' on line 103, col 30
                if _v is not None: write(_filter(_v, rawExpr=u'$mnemonic')) # from line 103, col 30.
                write(u''' command handler
      //! ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"comment",True) # u'$comment' on line 104, col 11
                if _v is not None: write(_filter(_v, rawExpr=u'$comment')) # from line 104, col 11.
                write(u'''
      void ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"mnemonic",True) # u'${mnemonic}' on line 105, col 12
                if _v is not None: write(_filter(_v, rawExpr=u'${mnemonic}')) # from line 105, col 12.
                write(u'''_cmdHandler(
''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"emit_non_port_params",False)([ VFSL([locals()]+SL+[globals(), builtin],"param_opCode",True), VFSL([locals()]+SL+[globals(), builtin],"param_cmdSeq",True) ] + VFSL([locals()]+SL+[globals(), builtin],"params",True)) # u'$emit_non_port_params([ $param_opCode, $param_cmdSeq ] + $params)' on line 106, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'$emit_non_port_params([ $param_opCode, $param_cmdSeq ] + $params)')) # from line 106, col 1.
                write(u'''
      );

''')
        write(u'''
    };

''')
        if VFSL([locals()]+SL+[globals(), builtin],"namespace_list",True) != None: # generated from line 114, col 1
            for namespace in VFSL([locals()]+SL+[globals(), builtin],"namespace_list",True): # generated from line 115, col 3
                write(u'''} // end namespace ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"namespace",True) # u'$namespace' on line 116, col 20
                if _v is not None: write(_filter(_v, rawExpr=u'$namespace')) # from line 116, col 20.
                write(u'''
''')
        write(u'''
#endif
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

    _mainCheetahMethod_for_hpp= 'respond'

## END CLASS DEFINITION

if not hasattr(hpp, '_initCheetahAttributes'):
    templateAPIClass = getattr(hpp, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(hpp)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=hpp()).run()


