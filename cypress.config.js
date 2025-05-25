const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: "http://localhost:8082",
    specPattern: "frontend/cypress/integration/**/*.js",
    supportFile: "frontend/cypress/support/e2e.js",
    setupNodeEvents(on, config) {
      // ...
    },
  },
});
