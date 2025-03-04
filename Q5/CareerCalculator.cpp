#include "CareerCalculator.h"

CareerCalculator::CareerCalculator() {
}

using namespace std;

bool CareerCalculator::CalculateMaxCareer(const std::vector<int>& steps) {

    int step = 0;
    bool feasable = true;

    while (feasable && step < steps.size()) {	// O(n) pire cas, si le vecteur contient que des 1
        step += steps[step];	// On avance de steps[step] pas (le int à l'index 'step' du vecteur 'steps')
        if (steps[step] == 0) {
            feasable = false;	// Si on tombe sur un 0, on avance plus
        }
    }
    return feasable;
}