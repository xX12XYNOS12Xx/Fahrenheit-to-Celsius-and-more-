#include <iostream>
#include <string>

int main() {
    std::string sud;
    std::cout << "Celsius or Fahrenheit: ";
    std::cin >> sud;

    if (sud == "celsius") {
        std::string celsius;
        std::cout << "Fahrenheit to Celsius: ";
        std::cin >> celsius;
        double fahrenheit = std::stod(celsius) * (9.0 / 5.0) + 32;
        std::cout << "Fahrenheit: " << fahrenheit << std::endl;
    } else if (sud == "fahrenheit") {
        std::string fahrenheit;
        std::cout << "Celsius to Fahrenheit: ";
        std::cin >> fahrenheit;
        double celsius = (std::stod(fahrenheit) - 32) * (5.0 / 9.0);
        std::cout << "Celsius: " << celsius << std::endl;
    }

    return 0;
}
