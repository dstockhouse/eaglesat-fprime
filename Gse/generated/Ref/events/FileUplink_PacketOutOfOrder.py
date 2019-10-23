'''
Created on Wednesday, 10 April 2019
@author: David

THIS FILE IS AUTOMATICALLY GENERATED - DO NOT EDIT!!!

XML Source: /cygdrive/c/Users/David/Documents/eaglesat/eaglesat-fprime/Svc/FileUplink/FileUplinkComponentAi.xml
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


COMPONENT = "Svc::FileUplink"

NAME = "FileUplink_PacketOutOfOrder"
ID  = 0x10b
SEVERITY = "WARNING_HI"
FORMAT_STRING = "Received packet %u after packet %u"
EVENT_DESCRIPTION = "The File Uplink component encountered an out-of-order packet during file receipt"

# Set arguments list with default values here.
ARGUMENTS = [
    ("packetIndex","The sequence index of the out-of-order packet",U32Type()), 
    ("lastPacketIndex","The sequence index of the last packet received before the out-of-order packet",U32Type()), 
    ]

