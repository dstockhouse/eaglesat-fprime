'''
Created on Wednesday, 10 April 2019
@author: David

THIS FILE IS AUTOMATICALLY GENERATED - DO NOT EDIT!!!

XML Source: /cygdrive/c/Users/David/Documents/eaglesat/eaglesat-fprime/Ref/SignalGen/SignalGenComponentAi.xml
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

from models.common import command
# Each file represents the information for a single command
# These module variables are used to instance the command object within the Gse


COMPONENT = "Ref::SignalGen"

MNEMONIC = "SG4_SignalGen_Settings"

OP_CODE  = 0x141

CMD_DESCRIPTION = "Signal Generator Settings"

# Set arguments list with default values here.
ARGUMENTS = [
    ("Frequency","",U32Type()), 
    ("Amplitude","",U32Type()), 
    ("Phase","",U32Type()), 
    ]

if __name__ == '__main__':
    testcmd = command.Command(COMPONENT, MNEMONIC, OP_CODE, CMD_DESCRIPTION, ARGUMENTS)
    data = testcmd.serialize()
    type_base.showBytes(data)
