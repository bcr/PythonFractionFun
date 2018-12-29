from behave import when, then
import fractionfun

@when(u'we have the input "{input}"')
def step_impl(context, input):
    context.output = fractionfun.process_input(input)

def assert_strings_equal(expected, actual):
    assert expected == actual, "Expected {}, but was {}".format(expected, actual)

@then(u'the output should be "{output}"')
def step_impl(context, output):
    assert_strings_equal(output, context.output)
