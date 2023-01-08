/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['templates/*.html', '**/templates/**/*.html'],
  theme: {
    extend: {
      colors: {
        base: '#3B5998',
      }
    },
  },
  plugins: [],
}
