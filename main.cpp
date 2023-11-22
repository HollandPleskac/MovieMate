#include <iostream>
#include <curl/curl.h>
#include <string>

using namespace std;

size.t WriteCallback(void *contents, size_t size, size_t nmmemb, string *output) {
    size_t totle_size = size * nmemb;
    output->append(static_cast<char*>(contents), total_size);
    return total_size;
}

int main () {
    CURL *curl = curl_easy_init();
    if (curl) {
        string apiUrl =; //add url

        curl_easy_setopt(curl, CURLOPT_URL, apiUrl.c_str());

        string responseData;

        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &responseData);

        //HTTP GET request
        CURLcode res = curl_easy_perform(curl);

        //cleanup
        curl_easy_cleanup(curl);
    }
    return 0;
}