# Copyright (c) 2022 The Regents of the University of California.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# Importing the required python packages here
import os
import argparse
# We need to first determine which ISA that we want to use. Then we have to
# make sure that we are using the correct ISA while executing this script.
from gem5.isas import ISA
from gem5.utils.requires import requires
from gem5.resources.resource import CustomResource
from gem5.resources.resource import DiskImageResource
from gem5.resources.resource import Resource 
# We import various parameters of the machine.
from gem5.components.cachehierarchies.classic\
    .private_l1_private_l2_cache_hierarchy import (
    PrivateL1PrivateL2CacheHierarchy,
)

from gem5.components.memory.ramulator_2 import Ramulator2System
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.boards.arm_board import ArmBoard
from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.processors.simple_processor import SimpleProcessor
# We will use the new simulator module to simulate this task.
from gem5.simulate.simulator import Simulator
from gem5.simulate.exit_event import ExitEvent
from m5.util import fatal
import m5.objects

# We have PrivateL1PrivateL2CacheHierarchy
cache_hierarchy = PrivateL1PrivateL2CacheHierarchy(
    l1d_size="16kB",
    l1i_size="16kB",
    l2_size="256kB",
)

memory = Ramulator2System("../example/DDR4.yaml", "ramulator_out", "2GB")

# We have a TIMING CPU. 
processor = SimpleProcessor(
    cpu_type=CPUTypes.TIMING,
    isa=ISA.ARM,
    num_cores=1
)


board = ArmBoard(
    clk_freq = "3GHz",
    processor = processor,
    memory = memory,
    cache_hierarchy = cache_hierarchy,
)

kernel      = Resource("arm64-linux-kernel-4.14.134")
bootloader  = Resource("arm64-bootloader-foundation")
disk_image  = Resource("arm64-ubuntu-18.04-img")

# Set the Full Systen workload
board.set_kernel_disk_workload(
        kernel = kernel, 
        bootloader = bootloader, 
        disk_image = disk_image 
)


# Lastly we instantiate the simulator module and simulate the program.
print("set simulator")
simulator = Simulator(
        board=board,
    )
simulator.run()

# We acknowlwdge the user that the simulation has ended.
print(
    "Exiting @ tick {} because {}.".format(
        simulator.get_current_tick(),
        simulator.get_last_exit_event_cause(),
    )
)
