 Project Title: MovieMate - A Personalized Movie Recommendation System

Group Members: Shivam Singh: https://github.com/ShivamSinghNow Holland Pleskac: https://github.com/HollandPleskac Nashwaan Khan: https://github.com/UnrealN1K Bao: https://github.com/Bao-Huynh888

Description: MovieMate aims to create a personalized movie recommendation system, helping users discover movies tailored to their preferences and viewing history. With the overwhelming amount of content available today, having an intelligent recommendation system ensures that users spend less time searching and more time enjoying content.

Why is it important or interesting to you? The world of cinema offers a vast array of experiences, emotions, and stories. However, the overwhelming choice can paralyze viewers in their selection process. We are passionate about utilizing data science to enhance user experiences. By developing MovieMate, we aim to bridge the gap between viewers and the perfect movie for their current mood or preference. We are also excited about delving deep into user-movie interaction data, understanding viewing patterns, and deriving meaningful insights from them.

Languages/tools/technologies:

Languages: Python Frameworks/Libraries: scikit-learn (for machine learning algorithms) pandas (for data manipulation) numpy (for numerical operations) Flask (for web application development) Datasets: MovieLens dataset (contains user ratings for movies) Additional metadata from sources like IMDb or TMDb (for more comprehensive data) Database: SQLite or PostgreSQL (to store user profiles, movie details, and ratings) Front-end (optional): HTML/CSS (for designing the web application's interface) JavaScript (for interactive features on the webpage)

Input: New user: Demographics (e.g., age, gender), genre preferences, and ratings for a few movies to initialize the recommendation engine. Existing user: Login credentials, new movie ratings, and preferences update. Output: A list of recommended movies ranked by predicted user rating or relevance. Insights into the user's viewing patterns (e.g., most-watched genres, average ratings given). Features:

User Profiles: Allow users to create profiles, input demographics, and rate movies. Personalized Recommendations: Based on user input and ratings, provide a list of top recommended movies. Interactive Rating System: Users can rate movies they've watched, which will further refine recommendations. Movie Search and Details: Allow users to search for movies and view detailed information including ratings, genres, and summaries. User Analytics Dashboard: Showcase insights such as most-watched genres, highest-rated movies, and viewing trends. Collaborative Filtering: Implement a collaborative filtering algorithm to recommend movies based on similar user behaviors. Content-based Filtering (optional): Analyze movie metadata to suggest movies similar to the ones the user likes. Hybrid Approach: Combine collaborative and content-based filtering for more accurate recommendations. Feedback System: Users can provide feedback on the accuracy of recommendations, which can be used for system improvement. This is a broad project description that covers the main aspects. Depending on the time and resources available, you can choose to implement the core features or expand with additional functionalities.
 > ## Phase II
 > In addition to completing the "User Interface Specification" and "Class Diagram" sections below, you will need to:
 > * Create an "Epic" (note) for each feature. Place these epics in the `Product Backlog` column
 > * Complete your first *sprint planning* meeting to plan out the next 7 days of work.
 >   * Break down the "Epics" into smaller actionable user stories (i.e. smaller development tasks). Convert them into issues and assign them to team members. Place these in the `TODO` (aka Sprint Backlog) column.
 >   * These cards should represent roughly 7 days worth of development time for your team. Then, once the sprint is over you should be repeating these steps to plan a new sprint, taking you until your second scrum meeting with the reader in phase III.
 > * Schedule two check-ins using Calendly. You need to pick both time slots on Tuesday of week 6. The check-ins will occur on Zoom. Your entire team must be present for both check-ins.
 >   * The first check-in needs to be scheduled with your lab TA. During that meeting, you will discuss your project design/class diagram from phase II.
 >   * The second check-in should be scheduled with a reader. During that meeting you will discuss:
 >     * The tasks you are planning for the first sprint
 >     * How work will be divided between the team members
## User Interface Specification
 > Include a navigation diagram for your screens and the layout of each of those screens as desribed below. For all the layouts/diagrams, you can use any tool such as PowerPoint or a drawing program. (Specification requirement is adapted from [this template](https://redirect.cs.umbc.edu/~mgrass2/cmsc345/Template_UI.doc))

### Navigation Diagram
![CS100 Project (1)](https://github.com/cs100/final-project-nkhan040-bhuyn048-hples001-ssing299/assets/37969942/591be814-b7b3-4788-a078-795ace23c1b3)

### Screen Layouts
> Include the layout of each of your screens. The layout should describe the screen’s major components such as menus and prompts for user inputs, expected output, and buttons (if applicable). Explain what is on the layout, and the purpose of each menu item, button, etc. If many screens share the same layout, start by describing the general layout and then list the screens that will be using that layout and the differences between each of them.

## Class Diagram
 > Include a **class diagram(s)** for your project and a **description** of the diagram(s). Your class diagram(s) should include all the main classes you plan for the project. This should be in sufficient detail that another group could pick up the project this point and successfully complete it. Use proper UML notation (as discussed in the course slides).
 
 > ## Phase III
 > You will need to schedule a check-in for the second scrum meeting with the same reader you had your first scrum meeting with (using Calendly). Your entire team must be present. This meeting will occur on Zoom and should be conducted by Wednesday of week 8.
 
 > BEFORE the meeting you should do the following:
 > * Update your class diagram from Phase II to include any feedback you received from your TA/grader.
 > * Considering the SOLID design principles, reflect back on your class diagram and think about how you can use the SOLID principles to improve your design. You should then update the README.md file by adding the following:
 >   * A new class diagram incorporating your changes after considering the SOLID principles.
 >   * For each update in your class diagram, you must explain in 3-4 sentences:
 >     * What SOLID principle(s) did you apply?
 >     * How did you apply it? i.e. describe the change.
 >     * How did this change help you write better code?
 > * Perform a new sprint plan like you did in Phase II.
 > * You should also make sure that your README file (and Project board) are up-to-date reflecting the current status of your project and the most recent class diagram. Previous versions of the README file should still be visible through your commit history.
 
> During the meeting with your reader you will discuss: 
 > * How effective your last sprint was (each member should talk about what they did)
 > * Any tasks that did not get completed last sprint, and how you took them into consideration for this sprint
 > * Any bugs you've identified and created issues for during the sprint. Do you plan on fixing them in the next sprint or are they lower priority?
 > * What tasks you are planning for this next sprint.

 
 > ## Final deliverable
 > All group members will give a demo to the reader during lab time. ou should schedule your demo on Calendly with the same reader who took your second scrum meeting. The reader will check the demo and the project GitHub repository and ask a few questions to all the team members. 
 > Before the demo, you should do the following:
 > * Complete the sections below (i.e. Screenshots, Installation/Usage, Testing)
 > * Plan one more sprint (that you will not necessarily complete before the end of the quarter). Your In-progress and In-testing columns should be empty (you are not doing more work currently) but your TODO column should have a full sprint plan in it as you have done before. This should include any known bugs (there should be some) or new features you would like to add. These should appear as issues/cards on your Project board.
 > * Make sure your README file and Project board are up-to-date reflecting the current status of your project (e.g. any changes that you have made during the project such as changes to your class diagram). Previous versions should still be visible through your commit history. 
 
 ## Screenshots
 > Screenshots of the input/output after running your application
 ## Installation/Usage
 > Instructions on installing and running your application
 ## Testing
 > How was your project tested/validated? If you used CI, you should have a "build passing" badge in this README.
 
