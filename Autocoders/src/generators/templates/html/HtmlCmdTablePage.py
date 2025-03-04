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
__CHEETAH_genTime__ = 1554930768.887957
__CHEETAH_genTimestamp__ = 'Wed Apr 10 14:12:48 2019'
__CHEETAH_src__ = 'HtmlCmdTablePage.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr 10 11:25:47 2019'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class HtmlCmdTablePage(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(HtmlCmdTablePage, self).__init__(*args, **KWs)
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
        
        write(u'''<!DOCTYPE html>
<html>
<head>
<title>''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'${name}' on line 4, col 8
        if _v is not None: write(_filter(_v, rawExpr=u'${name}')) # from line 4, col 8.
        write(u''' Component Dictionary</title>
</head>
<body>

<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 5px;
}
th {
    text-align: left;
}
html {
    font-family: Arial, sans-serif ;
    font-size: 90% ;
}
</style>

''')
        if VFSL([locals()]+SL+[globals(), builtin],"has_commands",True): # generated from line 25, col 1
            write(u'''
<h1><b>Command: ''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'${name}' on line 27, col 17
            if _v is not None: write(_filter(_v, rawExpr=u'${name}')) # from line 27, col 17.
            write(u'''</b></h1>



<table>
\t<thead>
\t\t<tr style = "border-right: 2px solid black; border-left: 2px solid black; border-top: 2px solid black;">
\t\t\t<th rowspan = "2">Mnemonic</th>
\t\t\t<th rowspan = "2">ID</th>
\t\t\t<th rowspan = "2">Description</th>
\t\t\t<th rowspan = "1" colspan = "3">Arguments</th>
\t\t</tr>
\t\t<tr style = "border-right: 2px solid black; ">
\t\t\t<th>Argument</th>
\t\t\t<th>Type</th>
\t\t\t<th>Description</th>
\t\t<tr>
\t</thead>
\t<tbody>
\t
''')
            for mnemonic, opcode, sync, priority, full, comment in VFSL([locals()]+SL+[globals(), builtin],"commands",True): # generated from line 47, col 1
                args = VFSL([locals()]+SL+[globals(), builtin],"command_args",True)[VFSL([locals()]+SL+[globals(), builtin],"mnemonic",True)]
                args_length = len(VFSL([locals()]+SL+[globals(), builtin],"args",True)) + 1
                if len(VFSL([locals()]+SL+[globals(), builtin],"opcode",True)) == 1: # generated from line 50, col 2
                    opcode = VFSL([locals()]+SL+[globals(), builtin],"opcode",True)[0]
                    if "x" in VFSL([locals()]+SL+[globals(), builtin],"opcode",True): # generated from line 52, col 5
                        opcode = int(VFSL([locals()]+SL+[globals(), builtin],"opcode",True), 16) + VFSL([locals()]+SL+[globals(), builtin],"base_id",True)
                    else: # generated from line 54, col 5
                        opcode = int(VFSL([locals()]+SL+[globals(), builtin],"opcode",True)) + VFSL([locals()]+SL+[globals(), builtin],"base_id",True)
                    hexopcode = hex(VFSL([locals()]+SL+[globals(), builtin],"opcode",True))
                write(u'''\t\t<tr style = "border: 2px solid black;">
\t\t\t<td rowspan="''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"args_length",True) # u'$args_length' on line 60, col 17
                if _v is not None: write(_filter(_v, rawExpr=u'$args_length')) # from line 60, col 17.
                write(u'''">''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"mnemonic",True) # u'${mnemonic}' on line 60, col 31
                if _v is not None: write(_filter(_v, rawExpr=u'${mnemonic}')) # from line 60, col 31.
                write(u'''</td>
\t\t\t<td rowspan="''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"args_length",True) # u'$args_length' on line 61, col 17
                if _v is not None: write(_filter(_v, rawExpr=u'$args_length')) # from line 61, col 17.
                write(u'''">''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"opcode",True) # u'${opcode}' on line 61, col 31
                if _v is not None: write(_filter(_v, rawExpr=u'${opcode}')) # from line 61, col 31.
                write(u''' (''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"hexopcode",True) # u'${hexopcode}' on line 61, col 42
                if _v is not None: write(_filter(_v, rawExpr=u'${hexopcode}')) # from line 61, col 42.
                write(u''')</td>
\t\t\t<td rowspan="''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"args_length",True) # u'$args_length' on line 62, col 17
                if _v is not None: write(_filter(_v, rawExpr=u'$args_length')) # from line 62, col 17.
                write(u'''">''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"comment",True) # u'${comment}' on line 62, col 31
                if _v is not None: write(_filter(_v, rawExpr=u'${comment}')) # from line 62, col 31.
                write(u'''</td>
''')
                if VFSL([locals()]+SL+[globals(), builtin],"args_length",True) > 1: # generated from line 63, col 6
                    args_index = 1
                    for arg_name, arg_type, comment, typeinfo in VFSL([locals()]+SL+[globals(), builtin],"args",True): # generated from line 65, col 7
                        arg_style = "border-right: 2px solid black;"
                        if VFSL([locals()]+SL+[globals(), builtin],"args_index",True) == 1: # generated from line 67, col 8
                            arg_style += "border-top: 2px solid black;"
                        if VFSL([locals()]+SL+[globals(), builtin],"args_index",True) + 1 == VFSL([locals()]+SL+[globals(), builtin],"args_length",True): # generated from line 70, col 6
                            arg_style += "border-bottom: 2px solid black;"
                        write(u'''\t\t\t\t\t<tr style = "''')
                        _v = VFSL([locals()]+SL+[globals(), builtin],"arg_style",True) # u'$arg_style' on line 73, col 19
                        if _v is not None: write(_filter(_v, rawExpr=u'$arg_style')) # from line 73, col 19.
                        write(u'''">\t\t\t\t\t
\t\t\t\t\t\t<td>''')
                        _v = VFSL([locals()]+SL+[globals(), builtin],"arg_name",True) # u'$arg_name' on line 74, col 11
                        if _v is not None: write(_filter(_v, rawExpr=u'$arg_name')) # from line 74, col 11.
                        write(u'''</td>
\t\t\t\t\t\t<td>''')
                        _v = VFSL([locals()]+SL+[globals(), builtin],"arg_type",True) # u'$arg_type' on line 75, col 11
                        if _v is not None: write(_filter(_v, rawExpr=u'$arg_type')) # from line 75, col 11.
                        write(u'''</td>
\t\t\t\t\t\t<td>''')
                        _v = VFSL([locals()]+SL+[globals(), builtin],"comment",True) # u'$comment' on line 76, col 11
                        if _v is not None: write(_filter(_v, rawExpr=u'$comment')) # from line 76, col 11.
                        write(u'''</td>
\t\t\t\t\t</tr>
''')
                        args_index += 1
                else: # generated from line 80, col 4
                    write(u'''\t\t\t\t<td></td>
\t\t\t\t<td></td>
\t\t\t\t<td></td>
''')
                write(u'''\t\t</tr>
''')
            write(u'''\t</tbody>
</table>   


''')
        write(u'''</body>
</html>
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

    _mainCheetahMethod_for_HtmlCmdTablePage= 'respond'

## END CLASS DEFINITION

if not hasattr(HtmlCmdTablePage, '_initCheetahAttributes'):
    templateAPIClass = getattr(HtmlCmdTablePage, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(HtmlCmdTablePage)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=HtmlCmdTablePage()).run()


