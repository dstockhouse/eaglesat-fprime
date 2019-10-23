'''
Created on Wednesday, 10 April 2019
@author: David

THIS FILE IS AUTOMATICALLY GENERATED - DO NOT EDIT!!!

XML Source: /cygdrive/c/Users/David/Documents/eaglesat/eaglesat-fprime/Svc/AssertFatalAdapter/AssertFatalAdapterComponentAi.xml
'''

# Import the types this way so they do not need prefixing for execution.
from models.serialize.type_exceptions import *
from models.serialize.type_base import *

from models.serialize.bool_type import *
from models.serialize.enum_type import *
from models.serialize.f32_type import *
from models.serialize.f64_type import *

from models.serialize.u8_type import *
from models.serialize.u16_type import *
from models.serialize.u32_type import *
from models.serialize.u64_type import *

from models.serialize.i8_type import *
from models.serialize.i16_type import *
from models.serialize.i32_type import *
from models.serialize.i64_type import *

from models.serialize.string_type import *
from models.serialize.serializable_type import *

from models.common import event
# Each file represents the information for a single event
# These module variables are used to instance the event object within the Gse


COMPONENT = "Svc::AssertFatalAdapter"

NAME = "AF_ASSERT_4"
ID  = 0x159
SEVERITY = "FATAL"
FORMAT_STRING = "Assert in file %s, line %d: %d %d %d %d"
EVENT_DESCRIPTION = "An assert happened"

# Set arguments list with default values here.
ARGUMENTS = [
    ("file","The source file of the assert",StringType(max_string_len=80)), 
    ("line","Line number of the assert",U32Type()), 
    ("arg1","First assert argument",U32Type()), 
    ("arg2","Second assert argument",U32Type()), 
    ("arg3","Third assert argument",U32Type()), 
    ("arg4","Fourth assert argument",U32Type()), 
    ]

