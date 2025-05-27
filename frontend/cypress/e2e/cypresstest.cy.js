// Cypress Test Suite for Incident Creation

describe('Incident Creation Form Tests', () => {

    beforeEach(() => {
      cy.visit('http://localhost:8081/incident/create');
    });
  
    it('should show validation errors for empty form submission', () => {
      cy.contains('Create').click();
      cy.get('.error').should('exist');
    });
  
    it('should allow filling the form with valid data', () => {
      cy.get('input[placeholder="Enter incident title"]').type('Server Crash');
      cy.get('select').eq(0).select('High');
      cy.get('select').eq(1).select('Network');
      cy.get('input[type="date"]').type('2025-05-27');
      cy.get('input[type="time"]').type('12:44');
      cy.get('textarea[placeholder="Enter incident description"]').type('Crash due to CPU overuse');
      cy.get('textarea[placeholder="Enter mitigation steps or plan"]').type('Restart server, monitor load');
      cy.get('textarea[placeholder="Enter any additional comments"]').type('Check logs for root cause');
      cy.get('input[placeholder="Enter attachment URL"]').type('https://example.com/report.pdf');
    });
  
    it('should submit form and redirect on success', () => {
      cy.get('input[placeholder="Enter incident title"]').type('Server Crash');
      cy.get('select').eq(0).select('High');
      cy.get('select').eq(1).select('Network');
      cy.get('input[type="date"]').type('2025-05-27');
      cy.get('input[type="time"]').type('12:44');
      cy.get('textarea[placeholder="Enter incident description"]').type('Crash due to CPU overuse');
      cy.get('textarea[placeholder="Enter mitigation steps or plan"]').type('Restart server, monitor load');
      cy.get('textarea[placeholder="Enter any additional comments"]').type('Check logs for root cause');
      cy.get('input[placeholder="Enter attachment URL"]').type('https://example.com/report.pdf');
      cy.contains('Create').click();
      cy.url().should('include', '/incident/list');
      cy.contains('Server Crash').should('exist');
    });
  
  });
  