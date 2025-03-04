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
__CHEETAH_genTime__ = 1554930759.917616
__CHEETAH_genTimestamp__ = 'Wed Apr 10 14:12:39 2019'
__CHEETAH_src__ = 'namespaceSerialH.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Apr 10 11:25:47 2019'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class namespaceSerialH(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(namespaceSerialH, self).__init__(*args, **KWs)
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
        
        if VFSL([locals()]+SL+[globals(), builtin],"namespace_list",True) != None: # generated from line 1, col 1
            for n in VFSL([locals()]+SL+[globals(), builtin],"namespace_list",True): # generated from line 2, col 2
                write(u'''namespace ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"n",True) # u'${n}' on line 3, col 11
                if _v is not None: write(_filter(_v, rawExpr=u'${n}')) # from line 3, col 11.
                write(u''' {
''')
        if VFSL([locals()]+SL+[globals(), builtin],"len",False)(VFSL([locals()]+SL+[globals(), builtin],"enum_type_list",True)) > 0: # generated from line 6, col 1
            for e in VFSL([locals()]+SL+[globals(), builtin],"enum_type_list",True): # generated from line 7, col 1
                type_name = VFSL([locals()]+SL+[globals(), builtin],"e",True)[0][1]
                enum_list = VFSL([locals()]+SL+[globals(), builtin],"e",True)[1]
                write(u'''
    typedef enum {
''')
                for item in VFSL([locals()]+SL+[globals(), builtin],"enum_list",True): # generated from line 12, col 1
                    write(u'''        ''')
                    _v = VFSL([locals()]+SL+[globals(), builtin],"item",True) # u'$item' on line 13, col 9
                    if _v is not None: write(_filter(_v, rawExpr=u'$item')) # from line 13, col 9.
                    write(u'''
''')
                write(u'''        ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"type_name",True) # u'${type_name}' on line 15, col 9
                if _v is not None: write(_filter(_v, rawExpr=u'${type_name}')) # from line 15, col 9.
                write(u'''_MAX
    } ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"type_name",True) # u'${type_name}' on line 16, col 7
                if _v is not None: write(_filter(_v, rawExpr=u'${type_name}')) # from line 16, col 7.
                write(u''';
''')
        write(u'''
class ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"name",True) # u'${name}' on line 20, col 7
        if _v is not None: write(_filter(_v, rawExpr=u'${name}')) # from line 20, col 7.
        write(u''' : public Fw::Serializable {

''')
        for (memname,type,size,format,comment) in VFSL([locals()]+SL+[globals(), builtin],"mem_list",True): # generated from line 22, col 1
            if VFSL([locals()]+SL+[globals(), builtin],"type",True) == "string": # generated from line 23, col 1
                write(u'''
  public:
    class ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"memname",True) # u'${memname}' on line 26, col 11
                if _v is not None: write(_filter(_v, rawExpr=u'${memname}')) # from line 26, col 11.
                write(u'''String : public Fw::StringBase {
        public:
        
            enum {
                SERIALIZED_SIZE = ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"size",True) # u'${size}' on line 30, col 35
                if _v is not None: write(_filter(_v, rawExpr=u'${size}')) # from line 30, col 35.
                write(u''' + sizeof(FwBuffSizeType) //!<size of buffer + storage of two size words
            };
        
            ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"memname",True) # u'${memname}' on line 33, col 13
                if _v is not None: write(_filter(_v, rawExpr=u'${memname}')) # from line 33, col 13.
                write(u'''String(const char* src); //!< char array constructor
            ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"memname",True) # u'${memname}' on line 34, col 13
                if _v is not None: write(_filter(_v, rawExpr=u'${memname}')) # from line 34, col 13.
                write(u'''String(const Fw::StringBase& src); //!< string base constructor
            ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"memname",True) # u'${memname}' on line 35, col 13
                if _v is not None: write(_filter(_v, rawExpr=u'${memname}')) # from line 35, col 13.
                write(u'''String(const ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"memname",True) # u'${memname}' on line 35, col 36
                if _v is not None: write(_filter(_v, rawExpr=u'${memname}')) # from line 35, col 36.
                write(u'''String& src); //!< string base constructor
            ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"memname",True) # u'${memname}' on line 36, col 13
                if _v is not None: write(_filter(_v, rawExpr=u'${memname}')) # from line 36, col 13.
                write(u'''String(void); //!< default constructor
            virtual ~''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"memname",True) # u'${memname}' on line 37, col 22
                if _v is not None: write(_filter(_v, rawExpr=u'${memname}')) # from line 37, col 22.
                write(u'''String(void); //!< destructor
            const char* toChar(void) const; //!< retrieves char buffer of string
            NATIVE_UINT_TYPE length(void) const; //!< returns length of string
            bool operator==(const ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"memname",True) # u'${memname}' on line 40, col 35
                if _v is not None: write(_filter(_v, rawExpr=u'${memname}')) # from line 40, col 35.
                write(u'''String& src) const; //!< equality operator
            
            const ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"memname",True) # u'${memname}' on line 42, col 19
                if _v is not None: write(_filter(_v, rawExpr=u'${memname}')) # from line 42, col 19.
                write(u'''String& operator=(const ''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"memname",True) # u'${memname}' on line 42, col 53
                if _v is not None: write(_filter(_v, rawExpr=u'${memname}')) # from line 42, col 53.
                write(u'''String& other); //!< equal operator for other strings

            Fw::SerializeStatus serialize(Fw::SerializeBufferBase& buffer) const; //!< serialization function
            Fw::SerializeStatus deserialize(Fw::SerializeBufferBase& buffer); //!< deserialization function
            
        private:
            void copyBuff(const char* buff, NATIVE_UINT_TYPE size); //!< copy a buffer, overwriting current contents
            NATIVE_UINT_TYPE getCapacity(void) const ; 
            void terminate(NATIVE_UINT_TYPE size); //!< terminate the string

            char m_buf[''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"size",True) # u'${size}' on line 52, col 24
                if _v is not None: write(_filter(_v, rawExpr=u'${size}')) # from line 52, col 24.
                write(u''']; //!< buffer for string storage
               
    };
    
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

    _mainCheetahMethod_for_namespaceSerialH= 'respond'

## END CLASS DEFINITION

if not hasattr(namespaceSerialH, '_initCheetahAttributes'):
    templateAPIClass = getattr(namespaceSerialH, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(namespaceSerialH)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=namespaceSerialH()).run()


