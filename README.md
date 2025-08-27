# Project Title: MovieMate - A Personalized Movie Recommendation System

**Group Members:** Shivam Singh: https://github.com/ShivamSinghNow Holland Pleskac: https://github.com/HollandPleskac Nashwaan Khan: https://github.com/UnrealN1K Bao: https://github.com/Bao-Huynh888

**Description:** MovieMate aims to create a personalized movie recommendation system, helping users discover movies tailored to their preferences and viewing history. With the overwhelming amount of content available today, having an intelligent recommendation system ensures that users spend less time searching and more time enjoying content.

**Why is it important or interesting to us?** The world of cinema offers a vast array of experiences, emotions, and stories. However, the overwhelming choice can paralyze viewers in their selection process. We are passionate about utilizing data science to enhance user experiences. By developing MovieMate, we aim to bridge the gap between viewers and the perfect movie for their current mood or preference. We are also excited about delving deep into user-movie interaction data, understanding viewing patterns, and deriving meaningful insights from them.

## Languages/tools/technologies:

**Languages:** Python Frameworks/Libraries: scikit-learn (for machine learning algorithms) pandas (for data manipulation) numpy (for numerical operations) Flask (for web application development) Datasets: MovieLens dataset (contains user ratings for movies) Additional metadata from sources like IMDb or TMDb (for more comprehensive data) Database: SQLite or PostgreSQL (to store user profiles, movie details, and ratings) Front-end (optional): HTML/CSS (for designing the web application's interface) JavaScript (for interactive features on the webpage)

**Input:** New user: Demographics (e.g., age, gender), genre preferences, and ratings for a few movies to initialize the recommendation engine. Existing user: Login credentials, new movie ratings, and preferences update. Output: A list of recommended movies ranked by predicted user rating or relevance. Insights into the user's viewing patterns (e.g., most-watched genres, average ratings given). Features:

**User Profiles:** Allow users to create profiles, input demographics, and rate movies. Personalized Recommendations: Based on user input and ratings, provide a list of top recommended movies. Interactive Rating System: Users can rate movies they've watched, which will further refine recommendations. Movie Search and Details: Allow users to search for movies and view detailed information including ratings, genres, and summaries. User Analytics Dashboard: Showcase insights such as most-watched genres, highest-rated movies, and viewing trends. Collaborative Filtering: Implement a collaborative filtering algorithm to recommend movies based on similar user behaviors. Content-based Filtering (optional): Analyze movie metadata to suggest movies similar to the ones the user likes. Hybrid Approach: Combine collaborative and content-based filtering for more accurate recommendations. Feedback System: Users can provide feedback on the accuracy of recommendations, which can be used for system improvement. This is a broad project description that covers the main aspects. Depending on the time and resources available, you can choose to implement the core features or expand with additional functionalities.

## User Interface Specification
 > Include a navigation diagram for your screens and the layout of each of those screens as desribed below. For all the layouts/diagrams, you can use any tool such as PowerPoint or a drawing program. (Specification requirement is adapted from [this template](https://redirect.cs.umbc.edu/~mgrass2/cmsc345/Template_UI.doc))

### Navigation Diagram
![CS100 Project (1)](https://github.com/cs100/final-project-nkhan040-bhuyn048-hples001-ssing299/assets/37969942/591be814-b7b3-4788-a078-795ace23c1b3)

### UML Diagram
![image](https://github.com/cs100/final-project-nkhan040-bhuyn048-hples001-ssing299/assets/146979415/3ee6926c-e5c5-49cc-833e-7baaa96407d4)
> Include the function to display the User's Dashboard. Implement class "User" to get the name, email, password, and the date the account was created for the user; in addition to the liked movies of the specific user. And a "Movie" class that uses variables name and image of the movie


 > ## Phase III


User class is to manage information about each user using the website.  Each user will have a watched movies and a liked/disliked movies list.  This will be used by our algorithm for recommendations.  Each user has a relationship to multiple movie classes.

Movie class is to manage info about movies.  Each class just has basic information about a movie (will be used for our algorithm) and will be used in the user class based on which movies the user likes. 

##### Non-Solid Principles UML Diagram (v1)

![image](https://github.com/cs100/final-project-nkhan040-bhuyn048-hples001-ssing299/assets/56204301/a500d218-a074-4fbe-8cc0-1226eb2f0984)

##### New Navigation Diagram

![image](https://github.com/cs100/final-project-nkhan040-bhuyn048-hples001-ssing299/assets/56204301/f30cd322-e350-46eb-a55b-4b6da06e0c54)

##### Solid Principles UML Diagram

![image](https://github.com/cs100/final-project-nkhan040-bhuyn048-hples001-ssing299/assets/56204301/be732d99-07f5-4b3e-9b3c-2cdfeb7bdff8)



##### What SOLID principle(s) did you apply? How did you apply it? i.e. describe the change.
* We applied Single Responsibility Principle (SRP) because we gave each class only one responsibility. We updated our user class to only manage authentication.  We added more classes to manage user interactions with movies.  We applied Interface Segregation Principle (ISP) because clients aren't forced to depend on interfaces they don't use.  We added compositions only when a class cannot exist without another class and specified relationships between classes.  We also made sure to keep the minimum necessary classes while still adhering to SOLID principles to make development as simple as possible.
##### How did this change help you write better code?
* Our codebase became more modular and maintainable with these changes. By applying the Single Responsibility Principle (SRP), we ensured that each class had only one reason to change. This separation of concerns makes it easier to manage and understand the code. For instance, the User class focusing solely on authentication simplifies its complexity and makes it less prone to errors during future modifications. The application of the Interface Segregation Principle (ISP) improved the overall design by ensuring that classes don't rely on unnecessary interfaces.  Incorporating compositions helped define clear relationships between classes ensuring they are tightly coupled only when necessary.

 
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
 
