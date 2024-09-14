# Setting up the EventSchedule React Project

Follow these steps to set up the EventSchedule project on your local machine:

1. Create a new directory for your project:
   ```
   mkdir golffest-schedule
   cd golffest-schedule
   ```

2. Initialize a new React project using Create React App:
   ```
   npx create-react-app .
   ```

3. Once the project is created, install additional dependencies:
   ```
   npm install lucide-react tailwindcss@latest postcss@latest autoprefixer@latest
   ```

4. Set up Tailwind CSS:
   ```
   npx tailwindcss init -p
   ```

5. Replace the content of `tailwind.config.js` with:
   ```javascript
   module.exports = {
     content: [
       "./src/**/*.{js,jsx,ts,tsx}",
     ],
     theme: {
       extend: {},
     },
     plugins: [],
   }
   ```

6. Replace the content of `src/index.css` with:
   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

7. Create a new file `src/components/EventSchedule.js` and paste the EventSchedule component code into it.

8. Replace the content of `src/App.js` with:
   ```jsx
   import React from 'react';
   import EventSchedule from './components/EventSchedule';

   function App() {
     return (
       <div className="App">
         <EventSchedule />
       </div>
     );
   }

   export default App;
   ```

9. Start the development server:
   ```
   npm start
   ```

Your project should now be running on `http://localhost:3000`.

## Troubleshooting

If you encounter any issues:

1. Ensure all dependencies are installed correctly.
2. Check for any error messages in the terminal or browser console.
3. Verify that all file paths are correct.
4. Make sure you've saved all changes to your files.

## Next Steps

- Customize the `events` array in the `EventSchedule` component with your actual event data.
- Adjust styles as needed to fit your design preferences.
- Consider adding additional features or interactivity to the schedule.