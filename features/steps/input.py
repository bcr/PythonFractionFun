from behave import when, then
import fractionfun

@when(u'we have the input "{input}"')
def step_impl(context, input):
    context.output = fractionfun.process_input(input)

@then(u'the output should be "{output}"')
def step_impl(context, output):
    assert output == context.output
