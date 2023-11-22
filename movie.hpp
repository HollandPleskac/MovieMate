#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#ifndef MOVIE_HPP
#define MOVIE_HPP

using namespace std;

class Movie {
 public:
    Movie(int id, string title, string genre) : id(id), title(title), genre(genre) {}
    int getID() const;
    string getTitle() const;
    string getGenre() const;

 private:
    int id;
    string title;
    string genre;
};

#endif