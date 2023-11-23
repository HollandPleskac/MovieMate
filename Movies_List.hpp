#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#ifndef RECOMMENDATIONENGINE_HPP
#define RECOMMENDATIONENGINE_HPP

using namespace std;

class RecommenationEngine {
 public:
    //Should be able to take from movie class
    void addToLikedMovies(const Movie &movie) {
      likedMovies.push_back(movie);
    }

    //Should be able to take from movie class
    vector<Movie> getLikedMovies() const {
      return likedMovies;
    }

    void addToWatchedMovies(const Movie &movie) {
      watchedMovies.push_back(movie);
    }

    vector<Movie> getWatchedMovies() const {
      return watchedMovies;
    }

    void addToDislikedMovies(const Movie &movie) {
      dislikeMovies.push_back(movie);
    }

    vector<Movie> getDislikedMovies() const {
      return dislikeMovies;
    }

 private:
    vector<Movie> likedMovies;
    vector<Movie> watchedMovies;
    vector<Movie> dislikedMovies;
};

#endif