const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: "http://localhost:8081",
    specPattern: "frontend/cypress/integration/**/*.js",
    supportFile: "frontend/cypress/support/e2e.js",
    setupNodeEvents(on, config) {
      // your node event handlers here
    },
  },
});
