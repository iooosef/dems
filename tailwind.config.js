/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  content: [],
  theme: {
    colors: {
      transparent: 'transparent',
      white: '#FFFFFF',
      primary: {
        500: '#3498db',
        700: '#2b7dbf'
      },
      secondary: {
        500: '#77bce9',
        700: '#619ed2'
      },
      dark: {
        500: '#1c3144',
        700: '#172838'
      },
      light: {
        500: '#ecf0f1',
        700: '#d6ddde'
      }
    },
    extend: {
      dropShadow: {
        border: '0px 3px 8px rgba(0, 0, 0, 0.2)'
      },
      boxShadow: {
        inner: 'inset 0px 5px 7px rgba(0, 0, 0, 0.125);'
      }
    }
  },
  plugins: []
}
