/**
 * Builds the GOAC Parent Feedback survey + a linked response Sheet.
 *
 * Run once, signed in as the ezpzps.com Workspace account:
 *   script.google.com -> New project -> paste this file -> Run buildParentSurvey
 *   -> approve permissions -> open View > Logs (Execution log) for the two URLs.
 *
 * Settings are deliberate: no sign-in, no email collection, no one-response limit.
 * Any of those forces a Google login and parents drop off.
 */
function buildParentSurvey() {
  var form = FormApp.create('Green Oaks Athletic Club — Parent Feedback');
  form.setDescription(
    'Thanks for being part of Green Oaks Athletic Club! This takes about 3 minutes.\n\n' +
    'Your answers help us plan future sessions. Responses may be shared with ' +
    'Oak Grove School administration. Your name is optional.'
  );

  form.setRequireLogin(false);            // Workspace forms default to "domain users only"
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false); // true would force sign-in
  form.setAllowResponseEdits(false);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(false);
  form.setConfirmationMessage('Thank you! We really appreciate it. — Coach Izenstark & Coach Callahan');

  form.addCheckboxItem()
    .setTitle('Which session(s) did your child attend?')
    .setChoiceValues(['Spring 2026 pilot', 'Fall 2026 Session #1 (K–2)'])
    .setRequired(true);

  form.addCheckboxItem()
    .setTitle("Your child's grade this school year")
    .setHelpText('More than one child in GOAC? Check each grade.')
    .setChoiceValues(['K', '1st', '2nd', '3rd', '4th', '5th'])
    .setRequired(true);

  form.addScaleItem()
    .setTitle('Overall, how satisfied are you with GOAC?')
    .setBounds(1, 5)
    .setLabels('Not satisfied', 'Very satisfied')
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('Would you enroll your child again?')
    .setChoiceValues(['Yes', 'Maybe', 'No'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('When you signed up, who did you understand was running GOAC?')
    .setChoiceValues([
      'Oak Grove School / District 68',
      'A private program run by the coaches (Mr. Izenstark and Mr. Callahan)',
      'An outside organization, not sure who',
      "I didn't think about it"
    ])
    .setRequired(true);

  form.addCheckboxItem()
    .setTitle('How did you hear about GOAC?')
    .setChoiceValues(['Another parent', 'A coach', 'Flyer', 'Website or social media'])
    .showOtherOption(true)
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle("If GOAC weren't available, what would your child most likely do after school on Fridays?")
    .setChoiceValues([
      'Another paid program elsewhere',
      'Go home',
      'Nothing comparable exists for us'
    ])
    .showOtherOption(true)
    .setRequired(true);

  form.addParagraphTextItem()
    .setTitle('Was anything about registration or communication unclear?');

  form.addParagraphTextItem()
    .setTitle("Anything else you'd like to share?");

  form.addTextItem()
    .setTitle('Your name and email (optional)')
    .setHelpText("Only if you're open to a follow-up.");

  var sheet = SpreadsheetApp.create('GOAC Parent Feedback (Responses)');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());

  Logger.log('Share this link with parents: ' + form.getPublishedUrl());
  Logger.log('Edit the form:               ' + form.getEditUrl());
  Logger.log('Responses sheet:             ' + sheet.getUrl());
}
