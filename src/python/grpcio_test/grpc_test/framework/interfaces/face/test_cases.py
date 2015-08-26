# Copyright 2015, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
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

"""Tools for creating tests of implementations of the Face layer."""

# unittest is referenced from specification in this module.
import unittest  # pylint: disable=unused-import

# test_interfaces is referenced from specification in this module.
from grpc_test.framework.interfaces.face import _blocking_invocation_inline_service
from grpc_test.framework.interfaces.face import _event_invocation_synchronous_event_service
from grpc_test.framework.interfaces.face import _future_invocation_asynchronous_event_service
from grpc_test.framework.interfaces.face import _invocation
from grpc_test.framework.interfaces.face import test_interfaces  # pylint: disable=unused-import

_TEST_CASE_SUPERCLASSES = (
    _blocking_invocation_inline_service.TestCase,
    _event_invocation_synchronous_event_service.TestCase,
    _future_invocation_asynchronous_event_service.TestCase,
)


def test_cases(implementation):
  """Creates unittest.TestCase classes for a given Face layer implementation.

  Args:
    implementation: A test_interfaces.Implementation specifying creation and
      destruction of a given Face layer implementation.

  Returns:
    A sequence of subclasses of unittest.TestCase defining tests of the
      specified Face layer implementation.
  """
  test_case_classes = []
  for invoker_constructor in _invocation.invoker_constructors():
    for super_class in _TEST_CASE_SUPERCLASSES:
      test_case_classes.append(
          type(invoker_constructor.name() + super_class.NAME, (super_class,),
               {'implementation': implementation,
                'invoker_constructor': invoker_constructor}))
  return test_case_classes
