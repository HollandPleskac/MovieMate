#include <iostream>
#include <string>
#include <vector>
#include <alogirthm>

#ifndef USER_HPP
#define USER_HPP

using namespace std;

class User {
 public:
    User(int id, string name) : id(id), name(name) {}

    int getId() const;
    string getName() const;

    void login();
    void logout();

 private:
    int id;
    string name;
    string email;
    string password;
};

#endif