describe('Create and Submit Incident Record', () => {
  const baseUrl = 'http://localhost:8080';  // Your frontend URL

  it('should create a new incident via the UI form and confirm submission', () => {
    cy.visit(baseUrl);

    // Assumes you have a button/link to open the create incident form
    cy.get('button#create-incident-btn').click();

    // Fill the incident form fields (adjust selectors to match your form)
    cy.get('input[name="incidenttitle"]').type('Test Incident from Cypress');
    cy.get('textarea[name="description"]').type('This is a test incident created by Cypress E2E.');
    cy.get('input[name="mitigation"]').type('Test mitigation steps.');

    // Submit the form
    cy.get('button[type="submit"]').click();

    // After submit, check for confirmation UI or success message
    cy.contains('Incident created successfully').should('be.visible');

    // Optionally verify the incident appears in the incident list
    cy.get('.incidents-table').contains('Test Incident from Cypress').should('exist');
  });
});
