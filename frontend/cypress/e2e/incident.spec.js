describe('Incident Management Module - With Mock Data', () => {
    beforeEach(() => {
      cy.intercept('GET', '**/incidents/', { fixture: 'incidents.json' }).as('getIncidents');
      cy.visit('http://localhost:8080/incidents');
      cy.wait('@getIncidents');
    });
  
    it('loads and displays mock incidents', () => {
      cy.contains('Unauthorized Access Detected');
      cy.contains('Data Export Without Encryption');
    });
  
    it('filters based on search query', () => {
      cy.get('.incident-search-input').type('Unauthorized');
      cy.get('.incident-checklist-item, .incident-card').should('contain', 'Unauthorized Access Detected');
      cy.get('.incident-checklist-item, .incident-card').should('not.contain', 'Data Export Without Encryption');
    });
  
    it('opens and closes solve modal', () => {
      cy.get('.solve-btn').first().click();
      cy.get('.solve-container').should('exist');
      cy.get('.modal-close-btn').click();
      cy.get('.solve-container').should('not.exist');
    });
  });
  