import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
  """Tests for the class AnonymousSurvey"""

  #Setup method allows the creation of objects once
  # and then user the in each of the test methods

  def setUp(self):
    '''
    Create a survey and a set of responses for use in all test methods.
    '''
    question = "What language did you first learn to speak?"
    self.my_survey = AnonymousSurvey(question)
    self.responses = ['English','Spanish','Mandarin']

  def test_store_single_response(self):
    '''The that a single response is stored properly'''
    question = "What language did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    my_survey.store_response('Portuguese')

    self.assertIn('Portuguese', my_survey.responses)

  def test_store_three_responses(self):
    '''Test that three individual responses are stored properly.'''
    question = "What question did you first learn to speak?"
    my_survey = AnonymousSurvey(question)
    responses = ['English','Spanish','Portuguese']
    for response in responses:
      my_survey.store_response(response)

    for response in responses:
      self.assertIn(response, my_survey.responses)

unittest.main()