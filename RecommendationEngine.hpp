#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#ifndef RECOMMENDATIONENGINE_HPP
#define RECOMMENDATIONENGINE_HPP

using namespace std;

class RecommenationEngine {
 public:
    //Should be able to take from user class
    void addUser(const User& user);
    //Should be able to take from movie class
    void addMovie(const Movie& movie);
    void rateMovie(int userID, int movieID, int rating);

    vector<Movie> getRecommendedMovies(int userID);

 private:
    vector<User> users;
    vector<Movie> movies;
};

#endif