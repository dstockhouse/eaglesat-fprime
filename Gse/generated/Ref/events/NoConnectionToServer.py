'''
Created on Wednesday, 10 April 2019
@author: David

THIS FILE IS AUTOMATICALLY GENERATED - DO NOT EDIT!!!

XML Source: /cygdrive/c/Users/David/Documents/eaglesat/eaglesat-fprime/Svc/GndIf/GndIfComponentAi.xml
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


COMPONENT = "Svc::GndIf"

NAME = "NoConnectionToServer"
ID  = 0x17d
SEVERITY = "WARNING_LO"
FORMAT_STRING = "Unable to connect to the socket server on port %d"
EVENT_DESCRIPTION = "The thread will try to re-connect until a connection is made"

# Set arguments list with default values here.
ARGUMENTS = [
    ("PortNumber","The port number running the socket server",U32Type()), 
    ]

