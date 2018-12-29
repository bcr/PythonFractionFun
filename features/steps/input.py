from behave import when, then

@when(u'we have the input "{input}"')
def step_impl(context, input):
    raise NotImplementedError(u'STEP: When we have the input "{input}"')

@then(u'the output should be "{output}"')
def step_impl(context, output):
    raise NotImplementedError(u'STEP: Then the output should be "{output}"')
