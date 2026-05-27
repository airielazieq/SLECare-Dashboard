/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "Segoe UI", "Arial", "sans-serif"],
      },
      colors: {
        ink: "#172026",
        clinical: "#0f766e",
        consult: "#2563eb",
        warning: "#b45309",
      },
    },
  },
  plugins: [],
};
