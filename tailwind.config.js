/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  content: [],
  theme: {
    colors: {
      transparent: 'transparent',
      white: '#FFFFFF',
      primary: '#3498db',
      secondary: '#77bce9',
      dark: '#1c3144',
      light: '#ecf0f1'
    }
  },
  plugins: []
}
